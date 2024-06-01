from random import choice
from discord.ext import commands

class Slapper(commands.Converter):
    name_mode: str

    def __init__(self, *, name_mode='nicknames') -> None:
        super().__init__()
        self.name_mode = name_mode
            

    async def convert(self, ctx: commands.Context, argument):
        random_person = choice(ctx.guild.members)
        author = ctx.author.nick
        someone = random_person.nick
        if author == None:
            author = ctx.author
        if someone == None:
            someone = random_person
        if self.name_mode == 'names':
            author = ctx.author
            someone = random_person
        elif self.name_mode == 'id':
            author = ctx.author.id
            someone = random_person.id

        return f"{author} slaps {someone} with {argument}!"

