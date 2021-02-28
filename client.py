import click
@click.group()
def cli():
    pass

@cli.command('create')
def workerCreate():
    click.echo('worker create')
    return 0

@click.command('delete')
@click.argument('num')
def workerDelete(num):
    click.echo('worker delete {}', num)
    return 0
cli.add_command(workerDelete)

@cli.command('list')
def workerList():
    click.echo('worker list')
    return 0

@cli.command()
def wordCount(num, files):
    click.echo('word count method')
    return 0

@cli.command()
def countWords(num, files):
    click.echo('count words method')
    return 0

if __name__ == '__main__':
    cli()