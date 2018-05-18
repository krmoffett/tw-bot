import discord
from misc.sheets import Sheet
from discord.ext import commands
from misc.base import Player

class TerritoryWar():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, aliases=['defences'])
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

    @commands.command(pass_context=True, aliases=['alldefences'])
    @commands.has_any_role('officers', 'botadmins')
    async def alldefenses(self, ctx):
        """Lists the defensive teams for all players.
        Usable by officers and botadmins only."""
        sheet = Sheet()
        sheet_data = sheet.get_data()
        description1 = "***Here's everyone's defense assignments for TW:***\n"
        description2 = ""
        if sheet_data != None:
            player_list = []
            for row in sheet_data:
                new_player = Player(row[0], row[1], row[2])
                player_list.append(new_player)
            for player in player_list[0:25]:
                description1 = description1 + "**" + player.name + "**" + "\n\t" + player.assigned_chars + " --- " + player.assigned_ships + "\n"
            for player in player_list[25:]:
                description2 = description2 + "**" + player.name + "**" + "\n\t" + player.assigned_chars + " --- " + player.assigned_ships + "\n"
            await self.bot.send_message(ctx.message.channel, description1)
            await self.bot.send_message(ctx.message.channel, description2)
            return
        else:
            await self.bot.say("No data found")
    
    @alldefenses.error
    async def alldefences_handler(self, error, ctx):
        """Handler for alldefenses command"""
        print ("error:{}".format(error))
        print ("ctx: {}".format(ctx))
        if isinstance(error, discord.ext.commands.errors.CheckFailure):
            print ("check failuer")
            await self.bot.say("You do not have permission to use this command")

    @commands.command(pass_context=True)
    async def map(self, ctx):
        """Sends the image of the TW map"""
        em = discord.Embed()
        em.set_image(url='https://cdn.discordapp.com/attachments/405606408344829952/405606490322370560/26106.jpeg')
        sheet = Sheet()
        sheet_data = sheet.get_squads()
        description = ""
        if sheet_data != None:
            for row in sheet_data:
                description += "**" + row[0] + ":** " + row[1] + "\n"
        em.description = description
        await self.bot.send_message(ctx.message.channel, embed=em)

def setup(bot):
    bot.add_cog(TerritoryWar(bot))