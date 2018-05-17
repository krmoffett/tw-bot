import discord
from misc.sheets import Sheet
from discord.ext import commands
from misc.base import Player

class WarCommands():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def defenses(self, ctx, *, user_name):
        """Returns the assigned defenses for the specified user"""
#        em = discord.Embed(colour=discord.Colour.blue())
#        em.title = "Hello {}. Here are your assigned teams".format(user_name)
#        em.description = "1. CLS\n2. JTR\n3. Phoenix\n4. Nightsisters"
#        await self.bot.send_message(ctx.message.channel, embed=em)
        sheet = Sheet()
        sheet_data = sheet.get_data()
        if sheet_data != None:
            for row in sheet_data:
                if user_name.lower() in row[0].lower():
                    player = Player(row[0], row[1], row[2])        
                    await self.bot.say("{}\t{}\t{}".format(row[0],row[1],row[2]))
        else:
            await self.bot.say("No data found for {}".format(user_name))

    @commands.command(pass_context=True)
    async def map(self, ctx):
        """Sends the image of the TW map"""
        em = discord.Embed()
        em.set_image(url='https://cdn.discordapp.com/attachments/405606408344829952/405606490322370560/26106.jpeg')
        await self.bot.send_message(ctx.message.channel, embed=em)

def setup(bot):
    bot.add_cog(WarCommands(bot))