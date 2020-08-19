"""
client
"""

import os
import sys
import inspect
import dotenv
import discord
import discord.ext.commands
import discord.ext.tasks

import discordpybot.cogs # pylint: disable=unused-import
import discordpybot.exts # pylint: disable=unused-import

class Client(discord.ext.commands.Bot):
    """
    client
    """
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            command_prefix=discord.ext.commands.when_mentioned_or('!')
        )
        dotenv.load_dotenv(dotenv.find_dotenv())
        parent_name = '.'.join(__name__.split('.')[:-1])
        for module_name, module in sys.modules.items():
            if f"{parent_name}.exts." in module_name:
                super().load_extension(module_name)
            elif f"{parent_name}.cogs." in module_name:
                for _, member in inspect.getmembers(module, inspect.isclass):
                    super().add_cog(member(self))

    async def start(self, *args, **kwargs):
        await super().start(os.getenv('TOKEN'))
