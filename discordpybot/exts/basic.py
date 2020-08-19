"""
basic extension
"""

import logzero

import discord
import discord.ext.commands
import discord.ext.tasks

class BasicExtension(discord.ext.commands.Cog):
    """
    basic extension
    """
    def __init__(self, client):
        self.client = client

    @discord.ext.commands.Cog.listener()
    async def on_ready(self):
        """
        event listener for on ready
        """
        logzero.logger.info('Ready')

def setup(client):
    """
    basic extension setup
    """
    client.add_cog(BasicExtension(client))

def teardown(client):
    """
    basic extension teardown
    """
    client.remove_cog('BasicExtension')
