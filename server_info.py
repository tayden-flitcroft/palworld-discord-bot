from discord.ext import commands
from game_settings import GameSettings

class ServerInfo(commands.Cog, name='Server Information'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="View the current game settings.")
    async def view_settings(self, ctx: commands.Context):
        settings = GameSettings()
        settings_messages = settings.format_settings_for_discord()
        for msg in settings_messages:
            await ctx.send(msg)

    @commands.command(help="Get the location of the server in a private message.")
    @commands.has_role('Admin')
    async def location(self, ctx: commands.Context):
        settings = GameSettings().settings
        await ctx.author.send(f'The Palworld server IP address is: {settings["PublicIP"]}:{settings["PublicPort"]}')
        await ctx.send(f"{ctx.author.mention}, I have sent you a direct message with the server information. Please share sparingly! 😊")
