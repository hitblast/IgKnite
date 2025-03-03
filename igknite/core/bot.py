# Imports.
import asyncio

import disnake
from disnake.ext import commands

from igknite.cogs import EXTENTIONS
from igknite.core.chain import keychain


# Set up a custom class for core functionality.
class IgKnite(commands.AutoShardedBot):
    """
    A subclassed version of `commands.AutoShardedBot`.\n
    Basically works as the core class for all-things IgKnite!
    """

    def __init__(
        self,
        *args,
        ignored_extensions: set[str] | None = None,
        **kwargs,
    ) -> None:
        super().__init__(
            command_prefix=commands.when_mentioned_or('.igkn.'),
            command_sync_flags=commands.CommandSyncFlags(
                sync_commands=True,
                allow_command_deletion=True,
            ),
            strip_after_prefix=True,
            case_insensitive=True,
            intents=disnake.Intents.all(),
            owner_ids={keychain.discord_owner_id},  # retrieve from KeyChain instance
            *args,
            **kwargs,
        )

        to_load = EXTENTIONS
        if ignored_extensions is not None:
            # ignored_extensions need's to be a set, can add a check
            # but not worth it since these are gonna be passed by a
            # developer
            to_load -= ignored_extensions

        for extension in to_load:
            self.load_extension(extension)

    async def _update_presence(self) -> None:
        """
        Updates the rich presence of IgKnite.
        """

        await self.change_presence(
            status=disnake.Status.dnd,
            activity=disnake.Activity(
                type=disnake.ActivityType.listening,
                name=f'/play & more',
            ),
        )

    async def on_connect(self) -> None:
        print(f'\nConnected to Discord as: {self.user}')

    async def on_ready(self) -> None:
        print(f'Server count: {len(self.guilds)} | Shard count: {self.shard_count}')
        await self._update_presence()

    async def on_guild_join(self, _: disnake.Guild) -> None:
        await self._update_presence()

    async def on_guild_remove(self, _: disnake.Guild) -> None:
        await self._update_presence()

    async def on_message_delete(self, message: disnake.Message) -> None:
        keychain.snipeables.append(message)
        await asyncio.sleep(25)
        keychain.snipeables.remove(message)
