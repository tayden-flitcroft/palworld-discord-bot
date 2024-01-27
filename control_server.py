from ssh import SSH
from discord.ext import commands

class ControlServer(commands.Cog, name='Control Server ("Palworld Pals" role required)'):
    def __init__(self, bot):
        self.bot = bot
        self.ssh = SSH()

    def check_server_is_running(self):
        return self.ssh.send_command(open('docs/scripts/is_server_running.sh').read()).strip() == 'true'
    
    def start_server(self):
        self.ssh.send_command(open('docs/scripts/start_server.sh').read())
        return self.check_server_is_running()

    def stop_server(self):
        self.ssh.send_command(open('docs/scripts/stop_server.sh').read())
        return self.check_server_is_running()
    
    def restart_server(self):
        self.ssh.send_command(open('docs/scripts/restart_server.sh').read())
        return self.check_server_is_running()

    async def cog_check(self, ctx):
        return any(role.name == 'Palworld Pals' for role in ctx.author.roles)

    @commands.command(name='startserver', help='Starts the server.')
    @commands.has_permissions(administrator=True)
    async def start_server_command(self, ctx):
        if self.start_server():
            await ctx.send("Server started successfully.")
        else:
            await ctx.send("Failed to start the server.")

    @commands.command(name='stopserver', help='Stops the server.')
    @commands.has_permissions(administrator=True)
    async def stop_server_command(self, ctx):
        if not self.stop_server():
            await ctx.send("Server stopped successfully.")
        else:
            await ctx.send("Failed to stop the server or server is already stopped.")

    @commands.command(name='restartserver', help='Restarts the server.')
    @commands.has_permissions(administrator=True)
    async def restart_server_command(self, ctx):
        if self.restart_server():
            await ctx.send("Server restarted successfully.")
        else:
            await ctx.send("Failed to restart the server.")

    @commands.command(name='serverstatus', help='Checks if the server is running.')
    async def check_server_command(self, ctx):
        if self.check_server_is_running():
            await ctx.send("Server is currently running.")
        else:
            await ctx.send("Server is not running.")
