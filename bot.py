import os
import discord
from discord.ext import commands
from dotenv_vault import load_dotenv
from server_info import ServerInfo
from control_server import ControlServer

load_dotenv()

bot = commands.Bot('!pal ', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')
    await bot.add_cog(ServerInfo(bot))
    await bot.add_cog(ControlServer(bot))

bot.run(os.environ['TOKEN'])
