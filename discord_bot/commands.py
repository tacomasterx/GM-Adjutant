from pathbuilder import *
from display import *

import discord
from discord.ext import commands
import os
import logging

intents = discord.Intents.all()
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents.message_content = True

client = commands.Bot(command_prefix="|", intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.command()
async def hello(ctx):
    await ctx.send("Hola krnal")

client.run(f'{os.environ["TDBTOKEN"]}', log_handler=handler, log_level=logging.DEBUG)
