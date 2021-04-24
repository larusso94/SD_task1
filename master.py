import grpc
from concurrent import futures
import time
import methods_pb2
import methods_pb2_grpc
import ast
import redis
import worker
import json

WORKERS = {}
CONNECTION = redis.Redis(host='localhost', port=6379)

WORKER_ID = 0
JOB_ID = 0
REQUEST_ID = 0

def enqueue(op, data, id, result):
    global CONNECTION
    global JOB_ID
    JOB_ID+=1
    data = {
        'op' : op,
        'data' : data,
        'id' : id,
        'result' : result
    }
    CONNECTION.rpush('queue:jobs',json.dumps(data))

def job(request, operation):
    global REQUEST_ID
    response = methods_pb2.message()
    response.error = -1
    try :
        files = ast.literal_eval(request.url)
    except :
        print("Url wrong format")
    
    for file in files:
        enqueue(operation, file, REQUEST_ID, False)
    enqueue(operation, '', REQUEST_ID, True)

    result = CONNECTION.blpop('queue:result'+str(REQUEST_ID),0)
    result = json.loads(result[1])

    response.result = str(result['result'])
    response.error = 0
    
    REQUEST_ID+=1

    return response
    
#comunicación grpc 
#----------------------------------------------------------------------------------------------------
def error(request):
    request.error = -1
    return request

def workerCreate(request):
    global WORKER_ID
    global WORKERS
    global CONNECTION
    response = methods_pb2.message()
    try :
        WORKERS[WORKER_ID] = worker.new_worker(WORKER_ID, CONNECTION)
        WORKER_ID+=1
        response.error = 0
    except :
        response.error = 1
    return response

def workerDelete(request):
    global WORKER_ID
    global WORKERS
    response = methods_pb2.message()
    try :
        WORKERS[request.worker].terminate()
        WORKERS[request.worker].join()
        del WORKERS[request.worker]
        response.error = 0
    except :
        response.error = -1
    return response

def listWorkers(request):
    global WORKERS
    response = methods_pb2.message()
    response.list = str(WORKERS)
    return response

def countWords(request):
    return job(request, 'count')

def enumerateWords(request):
    return job(request, 'enum')

class operationServicer(methods_pb2_grpc.operationServicer):
    def operation(self, request, context):
        switch = {
            1 : workerCreate,
            2 : workerDelete,
            3 : listWorkers,
            4 : countWords,
            5 : enumerateWords,
        }
        return switch.get(request.command, error)(request)

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