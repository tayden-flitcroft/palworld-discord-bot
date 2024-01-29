import os
import discord
from discord.ext import commands
from dotenv_vault import load_dotenv
from cogs.bot import Bot
from cogs.server import Server
from cogs.mods import Mods

load_dotenv()

bot = commands.Bot('!pal ', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')
    await bot.add_cog(Bot(bot))
    await bot.add_cog(Server(bot))
    await bot.add_cog(Mods(bot))

bot.run(os.environ['TOKEN'])
