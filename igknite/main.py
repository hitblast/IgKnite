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
    if keychain.disabled:
        print(
            'One or more secrets are undefined. Consider filling in the .env first (read README.md for more info).'
        )
        return

    bot_instance = IgKnite()
    bot_instance.run(keychain.discord_token)


if __name__ == '__main__':
    cli()
