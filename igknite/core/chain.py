# Imports.
import logging

from decouple import config
from disnake.message import Message


# Custom class for handling environment secrets and global variables..
class KeyChain:
    def __init__(self) -> None:
        self.snipeables: list[Message] = []

        try:
            self.discord_token = config('DISCORD_TOKEN', default=None, cast=str)
            self.discord_owner_id = config('DISCORD_OWNER_ID', default=None, cast=int)
            self.spotify_client_secret = config(
                'SPOTIFY_CLIENT_SECRET', default=None, cast=str
            )
            self.spotify_client_id = config('SPOTIFY_CLIENT_ID', default=None, cast=str)

        except ValueError:
            logging.error(
                'One or more secrets have been left undefined. '
                + 'Consider going through the README.md file for '
                + 'proper instructions on setting IgKnite up.'
            )


# Initializing it.
keychain = KeyChain()
