from discord.ext import commands
from discord.utils import get

from core import checks
from core.models import PermissionLevel

class RoleReset(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def lmao(self, ctx):
        role_names = ('Abyss Herrscher')
        roles = tuple(get(ctx.guild.roles, name=name) for name in role_names)
        for member in ctx.guild.members:
            try:
                await member.remove_roles(*roles)
            except:
                print(f'Couldn\'t remove roles from {member}')
        await ctx.send('deadded')

    @commands.command()
    async def test(self, ctx):
        await ctx.send('woah it works')

def setup(bot):
    bot.add_cog(RoleReset(bot))