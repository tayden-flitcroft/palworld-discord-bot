from discord.ext import commands
from helpers.ssh import SSH

class ControlBot(commands.Cog, name="Control Bot"):
    def __init__(self, bot):
        self.bot = bot
        self.ssh = SSH()

    @commands.command(name='updatebot', help='Temporarily shuts down the bot to update it. ("Palworld Pals" role required)')
    @commands.has_role("Palworld Pals")
    def update_bot(self):
        self.ssh.send_command(open('helpers/scripts/update_bot.sh').read())
        return