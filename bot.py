from game_settings import GameSettings
import discord
from discord.ext import commands
from dotenv_vault import load_dotenv
from os import environ

load_dotenv()

bot = commands.Bot('!pal ', intents=discord.Intents.all())

@bot.command(help="View the current game settings.")
async def view_settings(ctx: commands.Context):
    settings = GameSettings()
    settings_messages = settings.format_settings_for_discord()
    for msg in settings_messages:
        await ctx.send(msg)

@bot.command(help="Get the IP address of the server. (Admin Only)")
@commands.has_role('Admin')
async def location(ctx: commands.Context):
    settings = GameSettings().settings
    await ctx.author.send(f'The Palworld server IP address is: {settings["PublicIP"]}:{settings["PublicPort"]}')
    await ctx.send(f"{ctx.author.mention}, I have sent you a direct message with the server information. Please share sparingly! 😊")


bot.run(environ['TOKEN'])

