import grpc
from concurrent import futures
import time

import methods_pb2
import methods_pb2_grpc

import worker
import countWords
import enumerateWords
import multiprocessing as mp

MAX_WORKERS = mp.cpu_count()
POOL = mp.Pool(MAX_WORKERS)
MANAGER = mp.Manager()
EVENTS = {}
WORKERS = {}
WORKER_ID = 1



#comunicación grpc 
#----------------------------------------------------------------------------------------------------
class workerCreateServicer(methods_pb2_grpc.workerCreateServicer):
    def workerCreate(self, request, context):
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
class workerDeleteServicer(methods_pb2_grpc.workerDeleteServicer):
    def workerDelete(self, request, context):
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
class listWorkersServicer(methods_pb2_grpc.listWorkersServicer):
    def listWorkers(self, request, context):
        response = methods_pb2.message()
        response.list = str(WORKERS)
        return response
class countWordsServicer(methods_pb2_grpc.countWordsServicer):
    def countWords(self, request, context):
        response = methods_pb2.message()
        response.result = countWords.countWords(request)
        return response
class enumerateWordsServicer(methods_pb2_grpc.enumerateWordsServicer):
    def enumerateWords(self, request, context):
        response = methods_pb2.message()
        response.result = enumerateWords.enumerateWords(request)
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

methods_pb2_grpc.add_workerCreateServicer_to_server(
    workerCreateServicer(), server)
methods_pb2_grpc.add_workerDeleteServicer_to_server(
    workerDeleteServicer(), server)
methods_pb2_grpc.add_listWorkersServicer_to_server(
    listWorkersServicer(), server)
methods_pb2_grpc.add_countWordsServicer_to_server(
    countWordsServicer(), server)
methods_pb2_grpc.add_enumerateWordsServicer_to_server(
    enumerateWordsServicer(), server)
#----------------------------------------------------------------------------------------------------

print('Starting server. Listing on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)