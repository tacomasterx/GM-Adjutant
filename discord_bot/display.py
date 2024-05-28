import discord

def embed_character_sheet(character:dict, ctx, origin):
    embed = discord.Embed(title=origin, description=f"Fancy display for {ctx.message.author.name}'s character {character['name']}.", color=discord.Color.green(), timestamp=ctx.message.created_at)
    embed.add_field(name="Class and Level", value=f"{character['class']} {character['level']}")
    embed.add_field(name="Identity", value=f"{character['ancestry']}, {character['heritage']}\nbackground: {character['background']}\nalignment: {character['alignment']}\ngender: {character['gender']}")
    embed.add_field(name="Abilities", value=f"str: {character['abilities']['str']}\ndex: {character['abilities']['dex']}\ncon: {character['abilities']['con']}\nint: {character['abilities']['int']}\nwis: {character['abilities']['wis']}\ncha: {character['abilities']['cha']}\n")
    embed.add_field(name="Max HP", value=f"{character['attributes']['ancestryhp'] + character['attributes']['classhp'] + character['attributes']['bonushp'] + character['attributes']['bonushpPerLevel']}")
    return(embed)

