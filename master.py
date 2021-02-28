import grpc
from concurrent import futures
import time

import methods_pb2
import methods_pb2_grpc

import workerCreate
import workerDelete
import listWorkers
import countWords
import enumerateWords

class workerCreateServicer(methods_pb2_grpc.workerCreateServicer):
    def workerCreate(self, request, context):
        response = methods_pb2.createMessage()
        response.error = workerCreate.workerCreate(request.error)
        return response
class workerDeleteServicer(methods_pb2_grpc.workerDeleteServicer):
    def workerDelete(self, request, context):
        response = methods_pb2.deleteMessage()
        response.error = workerDelete.workerDelete(request.index)
        return response
class listWorkersServicer(methods_pb2_grpc.listWorkersServicer):
    def listWorkers(self, request, context):
        response = methods_pb2.listMessage()
        response.result = listWorkers.listWorkers(request.result)
        return response
class countWordsServicer(methods_pb2_grpc.countWordsServicer):
    def countWords(self, request, context):
        response = methods_pb2.countMessage()
        response.result = countWords.countWords(request.url)
        return response
class enumerateWordsServicer(methods_pb2_grpc.enumerateWordsServicer):
    def enumerateWords(self, request, context):
        response = methods_pb2.enumerateMessage()
        response.result = enumerateWords.enumerateWords(request.url)
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

print('Starting server. Listing on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)