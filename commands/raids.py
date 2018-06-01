import discord
from misc.sheets import Sheet
from discord.ext import commands

class Raids():
    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True, aliases=['raid'])
    async def raids(self, ctx):
        """Commands for raid information"""
        if ctx.invoked_subcommand is None:
            sheet = Sheet()
            raid_data = sheet.get_raid_schedule()
            if raid_data == None:
                await self.bot.say("Raid data not found")

            else:
                em = discord.Embed(title="Rule of Two Raid Schedule")
                description = ""
                for row in raid_data[1:]:
                   description += "**{}:** {}\n".format(row[0], row[1])
                em.description = description
                await self.bot.send_message(ctx.message.channel, embed=em) 
    
    @raids.command(pass_context=True)
    async def schedule(self, ctx):
        """View the current raid schedule"""
        sheet = Sheet()
        raid_data = sheet.get_raid_schedule()
        if raid_data == None:
            await self.bot.say("Raid data not found")

        else:
            em = discord.Embed(title="Rule of Two Raid Schedule")
            description = ""
            for row in raid_data[1:]:
                description += "**{}:** {}\n".format(row[0], row[1])
            em.description = description
            await self.bot.send_message(ctx.message.channel, embed=em)            
            

def setup(bot):
    bot.add_cog(Raids(bot))