import click
from click.decorators import argument
import grpc
import methods_pb2
import methods_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')

@click.group()
def cli():
    pass

@cli.command('create',help='Creates new work node.')
def workerCreate():
    stub = methods_pb2_grpc.workerCreateStub(channel)
    message = methods_pb2.createMessage(error = 0)
    response = stub.workerCreate(message)
    print(response.error)
    return 0

@cli.command('list', help='List all work nodes.')
def workerList():
    stub = methods_pb2_grpc.listWorkersStub(channel)
    message = methods_pb2.listMessage(error = 0, result = '')
    response = stub.listWorkers(message)
    print(response.result)
    return 0

@click.command('delete',help='Deletes work node by given index.')
@click.argument('num')
def workerDelete(num):
    stub = methods_pb2_grpc.workerDeleteStub(channel)
    message = methods_pb2.deleteMessage(error = 0, index = int(num))
    response = stub.workerDelete(message)
    print(response.error)
    return 0

@click.command('count', help='Count number of words of a text file by given url.')
@click.argument('files')
def wordCount(files):
    stub = methods_pb2_grpc.countWordsStub(channel)
    message = methods_pb2.countMessage(error = 0, url = files, result = 0)
    response = stub.countWords(message)
    print(response.result)
    return 0

@click.command('enumerate', help='Enumerate repeated words in a text file by given url.')
@click.argument('files')
def countWords(files):
    stub = methods_pb2_grpc.enumerateWordsStub(channel)
    message = methods_pb2.enumerateMessage(error = 0, url = files, result = '')
    response = stub.enumerateWords(message)
    print(response.result)
    return 0

cli.add_command(wordCount)
cli.add_command(countWords)
cli.add_command(workerDelete)

if __name__ == '__main__':
    cli()