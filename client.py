import click
from click.decorators import argument
import grpc
import methods_pb2
import methods_pb2_grpc


# message
# int32 error = 1;
# int32 node = 2;
# int32 count = 3;
# string url = 4;
# string list = 5;
# string enum = 6;    


channel = grpc.insecure_channel('localhost:50051')

@click.group()
def cli():
    pass

@cli.command('create',help='Creates new work node.')
def workerCreate():
    stub = methods_pb2_grpc.workerCreateStub(channel)
    message = methods_pb2.message()
    response = stub.workerCreate(message)
    print(response.error)
    return 0

@cli.command('list', help='List all work nodes with ID.')
def workerList():
    stub = methods_pb2_grpc.listWorkersStub(channel)
    message = methods_pb2.message()
    response = stub.listWorkers(message)
    print(response.list)
    return 0

@click.command('delete',help='Deletes work node by given ID.')
@click.argument('num')
def workerDelete(num):
    stub = methods_pb2_grpc.workerDeleteStub(channel)
    message = methods_pb2.message(node = int(num))
    response = stub.workerDelete(message)
    print(response.error)
    return 0

@click.command('count', help='Count number of words of a text file by given urls.')
@click.argument('files', nargs=-1)
def wordCount(files):
    stub = methods_pb2_grpc.countWordsStub(channel)
    message = methods_pb2.message(url = str(files))
    response = stub.countWords(message)
    print(response.count)
    return 0

@click.command('enumerate', help='Enumerate repeated words in a text file by given urls.')
@click.argument('files', nargs=-1)
def countWords(files):
    stub = methods_pb2_grpc.enumerateWordsStub(channel)
    message = methods_pb2.message(url = str(files))
    response = stub.enumerateWords(message)
    print(response.enum)
    return 0

cli.add_command(wordCount)
cli.add_command(countWords)
cli.add_command(workerDelete)

if __name__ == '__main__':
    cli()