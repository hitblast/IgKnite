# Imports.
import click

from .core import IgKnite


@click.group()
def cli() -> None:
    """Primary CLI entrypoint for IgKnite."""
    pass


@cli.command()
def run() -> None:
    bot_instance = IgKnite()
    bot_instance.run()


if __name__ == '__main__':
    cli()
