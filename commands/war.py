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
        sheet = Sheet()
        sheet_data = sheet.get_data()
        if sheet_data != None:
            for row in sheet_data:
                if user_name.lower() in row[0].lower():
                    player = Player(row[0], row[1], row[2])        
                    chars = player.get_chars()
                    ships = player.get_ships()
                    em = discord.Embed(title="Hello {}. Here are your assigned teams:".format(player.get_name()))
                    em.add_field(name="Characters", value=chars)
                    em.add_field(name="Ships", value=ships)
                    await self.bot.send_message(ctx.message.channel, embed=em)
                    return
            await self.bot.say("{} not found in list".format(user_name))
        else:
            await self.bot.say("No data found")

    @commands.command(pass_context=True)
    async def alldefenses(self, ctx):
        """Lists the defensive teams for all players"""
        sheet = Sheet()
        sheet_data = sheet.get_data()
        if sheet_data != None:
            player_list = []
            for row in sheet_data:
                new_player = Player(row[0], row[1], row[2])
                player_list.append(new_player)
            em = discord.Embed(title="Here is the list of everyone's teams for this TW:")
            for player in player_list:
                em.add_field(name=player.name, value=(player.assigned_chars + " --- " + player.assigned_ships))
            await self.bot.send_message(ctx.message.channel, embed=em)
            return
        else:
            await self.bot.say("No data found")

    @commands.command(pass_context=True)
    async def map(self, ctx):
        """Sends the image of the TW map"""
        em = discord.Embed()
        em.set_image(url='https://cdn.discordapp.com/attachments/405606408344829952/405606490322370560/26106.jpeg')
        await self.bot.send_message(ctx.message.channel, embed=em)

def setup(bot):
    bot.add_cog(WarCommands(bot))