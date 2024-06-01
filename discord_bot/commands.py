from converters import Slapper
from pathbuilder2 import *
from display import *
from error_handlers import *

import discord
from dotenv import load_dotenv
from discord.ext import commands
import os
import logging

load_dotenv()
DISCORD_BOT_SECRET = os.getenv("DISCORD_BOT_SECRET")
intents = discord.Intents.all()
log_handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents.message_content = True

client = commands.Bot(command_prefix="|", intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await missing_required_arguments(ctx)
    if isinstance(error, commands.UserNotFound):
        await user_not_found(ctx)
    if isinstance(error, commands.ArgumentParsingError):
        await argument_parsing_error(ctx)
    if isinstance(error, commands.BadArgument):
        await bad_argument(ctx)


@client.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f"Hello {author}!")


@client.command()
async def slap(ctx, reason = Slapper()):
    await ctx.send(reason)


@client.command(aliases=['importchar', 'charimport', 'ic'])
async def importcharacter(ctx, pathbuilder_code: int):
    # author = ctx.message.author
    # commands = str(ctx.message.content).split()
    # if len(commands) >= 2:
    #     embed = discord.Embed(
    #             title="Success",
    #             description=f"Nice arguments:\n{commands[0]}\n{commands[1]}",
    #             color=discord.Color.green(),
    #             timestamp=ctx.message.created_at
    #             )
    # else:
    #     embed = discord.Embed(
    #             title="Error",
    #             description="Not enough valid arguments",
    #             color=discord.Color.red(),
    #             timestamp=ctx.message.created_at
    #             )
    embed = discord.Embed(
                title="Success",
                description=f"Nice arguments:\n{pathbuilder_code}",
                color=discord.Color.green(),
                timestamp=ctx.message.created_at
                )
    await ctx.send(embed=embed)


client.run(f'{DISCORD_BOT_SECRET}', log_handler=log_handler, log_level=logging.DEBUG)

