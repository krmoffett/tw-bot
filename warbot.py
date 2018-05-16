#!/usr/bin/env python3
import discord
import asyncio
import configparser
from discord.ext import commands

#client = discord.Client()
config = configparser.ConfigParser()
config.read('config.ini')
defaultConfig = config['DEFAULT']
token = defaultConfig['token']
prefix = defaultConfig['prefix']
bot = commands.Bot(command_prefix=prefix)
startup_extensions = ['commands.test_commands', 'commands.war']

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def load(extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))

@bot.command()
async def unload(extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))

@bot.command()
async def hello():
    """Responds as Ewan would."""
    await bot.say("Hello there")

#@bot.command(pass_context=True)
#async def defenses(ctx, *, user_name):
#    """Sends response as Embed object"""
#    em = discord.Embed(colour=discord.Colour.blue())
#    em.title = "Hello {}. Here are your assigned teams".format(user_name)
#    em.description = "1. CLS\n2. JTR\n3. Phoenix\n4. Nightsisters"
##    await bot.say(em.title + "\n" + em.description)
#    await bot.send_message(ctx.message.channel, embed=em)

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.run(token)
