from pathbuilder2 import *
from display import *

import discord
from dotenv import load_dotenv
from discord.ext import commands
import os
import logging

load_dotenv()
DISCORD_BOT_SECRET = os.environ["DISCORD_BOT_SECRET"]
intents = discord.Intents.all()
log_handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents.message_content = True

client = commands.Bot(command_prefix="|", intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.command()
async def hello(ctx):
    await ctx.send("Hola krnal")

client.run(f'{DISCORD_BOT_SECRET}', log_handler=log_handler, log_level=logging.DEBUG)

@client.command(aliases=['importchar', 'charimport', 'ic'])
async def importcharacter(ctx):
    pass
