from discord.ext import commands
from helpers.game_settings import GameSettings
from helpers.rcon import RCON
from helpers.ssh import SSH

class ServerInfo(commands.Cog, name='Server Information'):
    def __init__(self, bot):
        self.bot = bot
        self.rcon = RCON()
        self.ssh = SSH()

    def check_server_is_running(self):
        return self.ssh.send_command(open('helpers/scripts/is_server_running.sh', encoding='utf-8').read()).strip() == 'true'
    
    @commands.command(name="viewsettings", help="View the current game settings.")
    async def view_settings(self, ctx: commands.Context):
        settings = GameSettings()
        settings_messages = settings.format_settings_for_discord()
        for msg in settings_messages:
            await ctx.send(msg)

    @commands.command(name='location', help='Get the location of the server. ("Palworld Pals" role required)')
    @commands.has_role('Palworld Pals')
    async def location(self, ctx: commands.Context):
        settings = GameSettings().settings
        await ctx.author.send(f'The Palworld server IP address is: {settings["PublicIP"]}:{settings["PublicPort"]}')
        await ctx.send(f"{ctx.author.mention}, I have sent you a direct message with the server information. Please share sparingly! 😊")

    @commands.command(name='version', help='View the current game version running on the server.')
    async def version(self, ctx: commands.Context):
        info = RCON().info()
        parts = info.split(']')
        await ctx.send(f"Game Version: {parts[0].split('[')[-1]}")

    @commands.command(name='servername', help='View the current the name of the server.')
    async def servername(self, ctx: commands.Context):
        info = self.rcon.info()
        parts = info.split(']')
        await ctx.send(f"Server Name: {parts[1].strip()}")

    @commands.command(name='serverstatus', help='Checks if the server is running.')
    async def check_server_command(self, ctx):
        if self.check_server_is_running():
            await ctx.send("Server is currently running.")
        else:
            await ctx.send("Server is not running.")