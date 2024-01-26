from game_settings import GameSettings
import discord
from discord.ext import commands
from dotenv_vault import load_dotenv
from os import environ

load_dotenv()

bot = commands.Bot('!pal ', intents=discord.Intents.all())

@bot.command()
async def view_settings(ctx: commands.context):
    settings = GameSettings()
    settings_messages = settings.format_settings_for_discord()
    for msg in settings_messages:
        await ctx.send(msg)

@bot.command()
async def location(ctx: commands.context):
    settings = GameSettings().settings
    await ctx.send('Server IP is: ' + settings['PublicIP'] + ':' + settings['PublicPort'])

@bot.command()
async def test(ctx: commands.context):
    await ctx.send('test')

bot.run(environ['TOKEN'])

