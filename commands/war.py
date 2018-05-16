import discord
from discord.ext import commands

class WarCommands():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def defenses(self, ctx, *, user_name):
        """Returns the assigned defenses for the specified user"""
        em = discord.Embed(colour=discord.Colour.blue())
        em.title = "Hello {}. Here are your assigned teams".format(user_name)
        em.description = "1. CLS\n2. JTR\n3. Phoenix\n4. Nightsisters"
        await self.bot.send_message(ctx.message.channel, embed=em)

    @commands.command(pass_context=True)
    async def map(self, ctx):
        """Sends the image of the TW map"""
        em = discord.Embed()
        em.set_image(url='https://cdn.discordapp.com/attachments/405606408344829952/405606490322370560/26106.jpeg')
        await self.bot.send_message(ctx.message.channel, embed=em)

def setup(bot):
    bot.add_cog(WarCommands(bot))