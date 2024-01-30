import discord
from discord.ext import commands
from helpers.ssh import SSH

class Mods(commands.Cog, name="Mods"):
    def __init__(self, bot):
        self.bot = bot
        self.ssh = SSH()
        self.mods_path = 'assets/mods/'
        self.mods_zip_path = 'mods.zip'

    @commands.group(name='mods', invoke_without_command=True)
    async def mods(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Mods command group. Use `mods <subcommand>`.')

    @mods.command(name='installer', help='Downloads mods installer.')
    async def installer(self, ctx):
        await ctx.send('Executable has been generated. Download and run to install all mods currently used on the server.')
        await ctx.send(file=discord.File('app/Palworld Mod Installer.exe'))
