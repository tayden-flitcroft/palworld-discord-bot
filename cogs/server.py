import csv
from io import StringIO
from discord.ext import commands
from helpers.ssh import SSH
from helpers.rcon import RCON
from helpers.game_settings import GameSettings

class Server(commands.Cog, name='Server'):
    def __init__(self, bot):
        self.bot = bot
        self.ssh = SSH()
        self.rcon = RCON()

    def check_server_is_running(self):
        return self.ssh.send_command(open('helpers/scripts/is_server_running.sh', encoding='utf-8').read()).strip() == 'true'
    
    def start_server(self):
        self.ssh.send_command(open('helpers/scripts/start_server.sh', encoding='utf-8').read())
        return self.check_server_is_running()

    def stop_server(self):
        self.ssh.send_command(open('helpers/scripts/stop_server.sh', encoding='utf-8').read())
        return self.check_server_is_running()
    
    def restart_server(self):
        self.ssh.send_command(open('helpers/scripts/restart_server.sh', encoding='utf-8').read())
        return self.check_server_is_running()
    
    @commands.group(name='server', invoke_without_command=True)
    async def server(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Server command group. Use `server <subcommand>`. For list of subcommands, use `!pal help server`.')

    @server.command(name='start', help='Starts the server. ("Palworld Pals" role required)')
    @commands.has_role('Palworld Pals')
    async def start_server_command(self, ctx):
        if self.start_server():
            await ctx.send("Server started successfully.")
        else:
            await ctx.send("Failed to start the server.")

    @server.command(name='stop', help='Stops the server. ("Palworld Pals" role required)')
    @commands.has_role('Palworld Pals')
    async def stop_server_command(self, ctx):
        self.rcon.save()
        if not self.stop_server():
            await ctx.send("Server stopped successfully.")
        else:
            await ctx.send("Failed to stop the server or server is already stopped.")

    @server.command(name='restart', help='Restarts the server. ("Palworld Pals" role required)')
    @commands.has_role('Palworld Pals')
    async def restart_server_command(self, ctx):
        self.rcon.save()
        if self.restart_server():
            await ctx.send("Server restarted successfully.")
        else:
            await ctx.send("Failed to restart the server.")

    @server.command(name='save', help='Saves game.')
    async def save_game(self, ctx):
        save = self.rcon.save()
        if save.strip() == 'Complete Save':
            await ctx.send('Save completed successfully.')
        else:
            await ctx.send('Failed to save game.')

    @server.command(name='players', help='Shows all active players.')
    async def show_players(self, ctx):
        players = self.rcon.show_players()
        f = StringIO(players)
        reader = csv.DictReader(f, delimiter=',')
        all_online_characters = [player['name'] for player in reader]

        await ctx.send(f'Total Players Online: {len(all_online_characters)}')
        await ctx.send(f'Players Online: {", ".join(all_online_characters)}')

    @server.command(name="settings", help="View the current game settings.")
    async def view_settings(self, ctx: commands.Context):
        settings = GameSettings()
        settings_messages = settings.format_settings_for_discord()
        for msg in settings_messages:
            await ctx.send(msg)

    @server.command(name='location', help='Get the location of the server. ("Palworld Pals" role required)')
    @commands.has_role('Palworld Pals')
    async def location(self, ctx: commands.Context):
        settings = GameSettings().settings
        await ctx.author.send(f'The Palworld server IP address is: {settings["PublicIP"]}:{settings["PublicPort"]}')
        await ctx.send(f"{ctx.author.mention}, I have sent you a direct message with the server information. Please share sparingly! 😊")

    @server.command(name='version', help='View the current game version running on the server.')
    async def version(self, ctx: commands.Context):
        info = RCON().info()
        parts = info.split(']')
        await ctx.send(f"Server Game Version: {parts[0].split('[')[-1]}")

    @server.command(name='name', help='View the current the name of the server.')
    async def servername(self, ctx: commands.Context):
        info = self.rcon.info()
        parts = info.split(']')
        await ctx.send(f"Server Name: {parts[1].strip()}")

    @server.command(name='status', help='Checks if the server is running.')
    async def check_server_command(self, ctx):
        if self.check_server_is_running():
            await ctx.send("Server is currently running.")
        else:
            await ctx.send("Server is not running.")
