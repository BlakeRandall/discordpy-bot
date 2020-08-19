"""
cogs
"""

import discord
import discord.ext.commands
import discord.ext.tasks

class BasicCog(discord.ext.commands.Cog):
    """
    cogs
    """
    def __init__(self, client):
        self.client = client

    @discord.ext.commands.command()
    async def ping(self, ctx):
        """
        ping pong command
        """
        async with ctx.typing():
            await ctx.send('pong')
