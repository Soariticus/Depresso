import random

from bs4 import BeautifulSoup
import requests

import discord

genesis = "3612493"
abberation = "3544133"
extinction = "5329716"
volcano = "4303118"
valguero = "3749804"
url = "https://www.battlemetrics.com/servers/ark/"
output = ""

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user, "|| Depresso is Online ||")
        print("-------------------------")
        await self.change_presence(activity=discord.Game(name='| Allen is an chicken shit'))



    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content.startswith("=td"):
            await message.delete()
            if message.author.id == 638494850861367296:
                text = input("What'd you like to say?")
                await message.channel.send(text)

        if message.content.startswith("=ga"):
            await message.delete()
            role = 684169307248525409
            if message.author.id == 638494850861367296:
                await message.author.add_roles(message.author, role)


client = MyClient()
client.run('NjQ2OTg1ODY1ODA1MTY4NjUw.Xl0fuA.X6wCaJX1PtZ-1NHXTSdCMA7skRY')
