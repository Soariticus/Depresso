import os
import random
import requests
import json
import discord
import discord.ext.commands
import asyncio
import time
import datetime
from discord.utils import get

from discord.ext import commands
from discord.ext.commands import Bot as client

@client.event
async def on_ready(self):
    print('Logged on as', self.user, "|| Depresso is Online ||")
    print("-------------------------")
    await self.change_presence(activity=discord.Game(name='| Reworking Depresso'))


owner = 638494850861367296
bot = commands.Bot(command_prefix='=')


@bot.command(aliases=["howgay"])
async def _howgay(ctx):
    print("howgay called")
    num = random.randint(0, 100)
    try:
        user = ctx.mention[0]
    except:
        user = ctx.author
    if user.id == owner:
        num = 0
    await ctx.send(f"{user} is {num}% gay.")

    #@client.command(aliases=['test'])
    #async def _test(self):
    #    print('work')


async def on_message(self, message):
        # don't respond to ourselves
    if message.author == self.user:
        return

























































































bot.run('NjQ2OTg1ODY1ODA1MTY4NjUw.XqNPWg.xOYmDJO_STtSrZRQ6IeDwX4UG50')