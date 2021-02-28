import click
from click.decorators import argument
@click.group()
def cli():
    pass

@cli.command('create',help='Creates new work node.')
def workerCreate():
    click.echo('worker create')
    return 0

@click.command('delete',help='Deletes work node by given index.')
@click.argument('num')
def workerDelete(num):
    click.echo(num)
    return 0

@cli.command('list', help='List all work nodes.')
def workerList():
    click.echo('worker list')
    return 0

@click.command('count', help='Count number of words of a text file by given url.')
@click.argument('files')
def wordCount(files):
    click.echo('word count method')
    return 0

@click.command('enumerate', help='Enumerate repeated words in a text file by given url.')
@click.argument('files')
def countWords(files):
    click.echo('count words method')
    return 0

cli.add_command(wordCount)
cli.add_command(countWords)
cli.add_command(workerDelete)

if __name__ == '__main__':
    cli()