# Imports.
import click

from igknite.core import IgKnite
from igknite.core.chain import keychain


@click.group()
def cli() -> None:
    """Primary CLI entrypoint for IgKnite."""
    pass


@cli.command()
def run() -> None:
    bot_instance = IgKnite()
    bot_instance.run(keychain.discord_token)


if __name__ == '__main__':
    cli()
