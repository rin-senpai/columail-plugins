from datetime import date

from discord.ext import commands, tasks
from discord.utils import get

from core import checks
from core.models import PermissionLevel

class RoleReset(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.abyss_reset.start()

    def cog_unload(self):
        self.abyss_reset.cancel()

    @tasks.loop(time=24)
    async def abyss_reset(self):
        current_date = date.today().day
        if current_date == 1 or current_date == 16:
            role_names = ('Abyss Herrscher')
            guild = self.bot.get_guild(995084634050265170)
            roles = tuple(get(guild.roles, name=name) for name in role_names)
            for member in guild.members:
                try:
                    await member.remove_roles(*roles)
                except:
                    print(f'Couldn\'t remove roles from {member}')

    @commands.command()
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def notmadeinabyss(self, ctx):
        role_names = ('Abyss Herrscher')
        roles = tuple(get(ctx.guild.roles, name=name) for name in role_names)
        for member in ctx.guild.members:
            try:
                await member.remove_roles(*roles)
            except:
                print(f'Couldn\'t remove roles from {member}')
        await ctx.send('Removed all roles.')

def setup(bot):
    bot.add_cog(RoleReset(bot))