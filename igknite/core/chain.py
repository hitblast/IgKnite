# Imports.
import logging
from typing import List

from decouple import config
from disnake import Message


# Custom class for handling environment secrets and global variables..
class KeyChain:
    def __init__(self) -> None:
        self.discord_token = None
        self.discord_owner_id = None
        self.spotify_client_secret = None
        self.spotify_client_id = None
        self.snipeables: List[Message] = []

        try:
            self.discord_token = config('DISCORD_TOKEN', cast=str)
            self.discord_owner_id = config('DISCORD_OWNER_ID', cast=int)
            self.spotify_client_secret = config('SPOTIFY_CLIENT_SECRET', cast=str)
            self.spotify_client_id = config('SPOTIFY_CLIENT_ID', cast=str)

        except ValueError:
            logging.error(
                'One or more secrets have been left undefined. '
                + 'Consider going through the README.md file for '
                + 'proper instructions on setting IgKnite up.'
            )


# Initializing it.
keychain = KeyChain()
