import discord
from discord.ext import commands

HELP_COMMAND = "\"|help\""

async def missing_required_arguments(ctx: commands.Context):
    embed = discord.Embed(
            title="Argument error:",
            description=f"Missing the required arguments, use the {HELP_COMMAND} command for mor information.",
            color=discord.Color.red(),
            timestamp=ctx.message.created_at
            )
    await ctx.send(embed=embed)


async def user_not_found(ctx: commands.Context):
    embed = discord.Embed(
            title="User error:",
            description=f"User not found, use the {HELP_COMMAND} command for mor information.",
            color=discord.Color.red(),
            timestamp=ctx.message.created_at
            )
    await ctx.send(embed=embed)

async def argument_parsing_error(ctx: commands.Context):
    embed = discord.Embed(
            title="Argument error:",
            description=f"Error parsing arguments, please share this error message with an administrator.",
            color=discord.Color.red(),
            timestamp=ctx.message.created_at
            )
    await ctx.send(embed=embed)

async def bad_argument(ctx: commands.Context):
    embed = discord.Embed(
            title="Argument error:",
            description=f"Invalid arguments, use the {HELP_COMMAND} command for mor information.",
            color=discord.Color.red(),
            timestamp=ctx.message.created_at
            )
    await ctx.send(embed=embed)
