from discord.ext import commands
from helpers.ssh import SSH

class Bot(commands.Cog, name="Bot"):
    def __init__(self, bot):
        self.bot = bot
        self.ssh = SSH()

    @commands.group(name='bot', invoke_without_command=True)
    async def bot(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Bot command group. Use `bot <subcommand>`.')

    @bot.command(name='update', help='Temporarily shuts down the bot to update it. ("Palworld Pals" role required)')
    @commands.has_role("Palworld Pals")
    async def update_bot(self, ctx):
        await ctx.send('Shutting down to update. This should take <30 seconds. Please wait...')
        self.ssh.send_command(open('helpers/scripts/update_bot.sh', encoding='utf-8').read())
