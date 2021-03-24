import grpc
from concurrent import futures
import time
import methods_pb2
import methods_pb2_grpc
import ast
import redis
import worker
import multiprocessing as mp
import json

MAX_WORKERS = mp.cpu_count()
POOL = mp.Pool(MAX_WORKERS)
MANAGER = mp.Manager()
EVENTS = {}
WORKERS = {}
WORKER_ID = 1

CONNECTION = redis.Redis(host='localhost', port=6379)
JOB_COUNT = 0
#comunicación grpc 
#----------------------------------------------------------------------------------------------------
def error(request):
    request.error = -1
    return request

def workerCreate(request):
    global WORKER_ID
    global WORKERS
    global MAX_WORKERS
    global POOL
    global MANAGER
    global EVENTS
    response = methods_pb2.message()
    if(len(WORKERS) < MAX_WORKERS):
        EVENTS[WORKER_ID] = MANAGER.Event()
        result = POOL.apply_async(worker.worker,args=(WORKER_ID,EVENTS[WORKER_ID]))
        WORKERS[WORKER_ID] = result
        WORKER_ID += 1
        response.error = 0
        return response
    response.error = -1
    return response

def workerDelete(request):
    global WORKER_ID
    global WORKERS
    global MAX_WORKERS
    global EVENTS
    response = methods_pb2.message()
    if (len(WORKERS) > 0 and request.node in WORKERS):
        EVENTS[request.node].set()
        WORKERS[request.node].get()
        del(WORKERS[request.node])
        response.error = 0
        return response
    response.error = -1
    return response

def listWorkers(request):
    response = methods_pb2.message()
    response.list = str(WORKERS)
    return response

def enqueue(op, data):
    global CONNECTION
    data = {
        'op' : op,
        'data' : data, 
    }
    CONNECTION.rpush('queue:jobs',json.dumps(data))

def countWords(request):
    global JOB_COUNT
    response = methods_pb2.message()
    files = ast.literal_eval(request.url)
    
    for file in files:
        JOB_COUNT+=1
        enqueue('count', file)
    JOB_COUNT+=1
    enqueue('result', None)

    end = False
    while(not end):
        time.sleep(1)
    return response

def enumerateWords(request):
    global JOB_COUNT
    response = methods_pb2.message()
    files = ast.literal_eval(request.url)
    
    for file in files:
        JOB_COUNT+=1
        enqueue('enum', file)
    JOB_COUNT+=1
    enqueue('result', None)

    end = False
    while(not end):
        time.sleep(1)
    return response

class operationServicer(methods_pb2_grpc.operationServicer):
    def operation(self, request, context):
        switch = {
            1 : workerCreate,
            2 : workerDelete,
            3 : listWorkers,
            4 : countWords,
            5 : enumerateWords,
        }
        return switch.get(request.op, error)(request)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

methods_pb2_grpc.add_operationServicer_to_server(
    operationServicer(), server)
#----------------------------------------------------------------------------------------------------

print('Starting server. Listing on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()
CONNECTION.ping()
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    CONNECTION.flushall()
    server.stop(0)