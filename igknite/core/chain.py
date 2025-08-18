# Imports.
import logging

from decouple import config, UndefinedValueError
from disnake.message import Message


class KeyChain:
    '''
    Core keychain of IgKnite for keeping secrets.

    `keychain.disabled` will be True if one or more required secrets for IgKnite cannot be initialized
    for a particular launch session.
    '''
    def __init__(self) -> None:
        self.snipeables: list[Message] = []
        self.disabled = False

        try:
            self.discord_token = config('DISCORD_TOKEN', cast=str)
            self.discord_owner_id = config('DISCORD_OWNER_ID', cast=int)
            self.spotify_client_secret = config(
                'SPOTIFY_CLIENT_SECRET', cast=str
            )
            self.spotify_client_id = config('SPOTIFY_CLIENT_ID', cast=str)

            for item in [self.discord_token, self.discord_owner_id, self.spotify_client_secret, self.spotify_client_id]:
                if str(item).strip() == "" and not self.disabled:
                    self.disabled = True


        except UndefinedValueError:
            self.disabled = True


# Initializing it.
keychain = KeyChain()
