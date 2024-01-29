import discord
from discord.ext import commands
from helpers.ssh import SSH
from zipfile import ZipFile
from glob import glob
import os

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

    @mods.command(name='download', help='Downloads all mods required for the server.')
    async def download(self, ctx):
       if os.path.exists(self.mods_zip_path):
            os.remove(self.mods_zip_path)
        
       zip = ZipFile(self.mods_zip_path, 'x')

       for file in glob(self.mods_path + '*'):
           zip.write(file, os.path.basename(file))
           
       await ctx.send(file=discord.File(self.mods_zip_path))
