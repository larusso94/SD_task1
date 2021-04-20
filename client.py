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
    stub = methods_pb2_grpc.operationStub(channel)
    message = methods_pb2.message(command = 1)
    response = stub.operation(message)
    print(response.error)
    return 0

@click.command('delete',help='Deletes work node by given ID.')
@click.argument('num')
def workerDelete(num):
    stub = methods_pb2_grpc.operationStub(channel)
    message = methods_pb2.message(command = 2, worker = int(num))
    response = stub.operation(message)
    print(response.error)
    return 0

@cli.command('list', help='List all work nodes with ID.')
def workerList():
    stub = methods_pb2_grpc.operationStub(channel)
    message = methods_pb2.message(command = 3)
    response = stub.operation(message)
    print(response.list)
    return 0

@click.command('count', help='Count number of words of a text file by given urls.')
@click.argument('files', nargs=-1)
def wordCount(files):
    stub = methods_pb2_grpc.operationStub(channel)
    message = methods_pb2.message(command = 4, url = str(files))
    response = stub.operation(message)
    print(response.count)
    return 0

@click.command('enumerate', help='Enumerate repeated words in a text file by given urls.')
@click.argument('files', nargs=-1)
def countWords(files):
    stub = methods_pb2_grpc.operationStub(channel)
    message = methods_pb2.message(command = 5, url = str(files))
    response = stub.operation(message)
    print(response.enum)
    return 0

cli.add_command(wordCount)
cli.add_command(countWords)
cli.add_command(workerDelete)

if __name__ == '__main__':
    cli()