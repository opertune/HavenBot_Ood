import os
import discord
from discord.ext import commands
import logging
from Commands.Player_not_registered import Player_not_registered
from dotenv import load_dotenv
from keep_alive import keep_alive

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)
@bot.command(name='check')
# Commande restriction by roles
@commands.has_any_role(1084908952963260527, 1084909032160104528) #Roles : GM's - Officiers
async def check(ctx, arg=None):
    command1 = Player_not_registered(bot, ctx, arg)
    await command1.commandCheck()

@check.error
async def check_error(ctx, error):
    if isinstance(error, commands.MissingAnyRole):
        await ctx.message.author.send('You are not allowed to use this command.')

keep_alive()
load_dotenv('.env')
bot.run(os.getenv("TOKEN"), log_handler=handler, log_level=logging.DEBUG)
