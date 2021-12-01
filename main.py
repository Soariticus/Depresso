from builtins import range

import discord
import random
from bs4 import BeautifulSoup as bs
import requests

owner = 638494850861367296
dyno = 155149108183695360
genesis = "3612493"
abberation = "3544133"
extinction = "5329716"
volcano = "4303118"
valguero = "3749804"
url = "https://www.battlemetrics.com/servers/ark/"
output = ""
staff = [638494850861367296]
suggestionChannel = [684050221709393981, 684146862365868058, 644983893581234188, 701912523309318246]

class battle:
    def getServer(self, choice):
        global output
        go = True
        global url, genesis, abberation, extinction, volcano, valguero
        if choice == "genesis" or choice == "gen":
            self.server = genesis
            output = "Genesis"
        elif choice == "abberation" or choice == "abb":
            output = "Abberation"
            self.server = abberation
        elif choice == "extinction" or choice == "ext":
            output = "Extinction"
            self.server = extinction
        elif choice == "volcano" or choice == "vol":
            output = "Vulcano"
            self.server = volcano
        elif choice == "valguero" or choice == "val":
            output = "Valguero"
            self.server = valguero
        else:
            go = False
            return("Cannot find that server. Try again.")
        if go == True:
            self.url = url + self.server
            users = self.htmlParsing()
            return users

    def htmlParsing(self):
        self.headers = {
            "Authorization": "AUTHKEYHERE" }
        self.request = requests.post(url=self.url, headers=self.headers)
        pageSoup = bs(self.request.text, "html.parser")

        users = pageSoup.findAll("a", {"class": "css-zwebxb"})
        onlineUser = len(users)
        return onlineUser


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user, "|| Depresso is Online ||")
        print("-------------------------")
        await self.change_presence(activity=discord.Game(name='| =help'))

    async def on_message(self, message):
        # don't respond to ourselves
        global gayscale, defs, staff
        if message.author == self.user:
            return

        guildID = message.guild.id

        if guildID == 701608917129494549:  # LoVector
            staff += [480230678152085515]  # Xel
        elif guildID == 478070785345454080:  # Playground
            staff += [425450014366629901, 365016779606458369, 379118368474529792, 167130892450398208]  # Allen, Valka, Pak, Dream

        if message.content.startswith("=howgay"):  # looking for =howgay command
            bot = 1
            args = message.content.split()
            s = args[1]
            if s is "":  # if the user area is empty
                s = str(message.author.id)  # set the name used to the authors
                s = "<@" + s + ">"  # turning the int into a usable string
            if "<@638494850861367296>" not in s and "<@643805478828245018>" not in s:  # owner override
                gayscale = str(random.randint(0, 100))  # getting a random number for % of gay-ness
            elif "<@643805478828245018>" in s:
                await message.channel.send("¯\_(ツ)_/¯")
                bot = 0
            else:
                gayscale = "0"
            if bot is not 0:
                await message.channel.send(s + " is " + gayscale + "% gay.")  # putting the arg and % of gayness in chat

        if message.content.startswith("=info"):
            embed = discord.Embed(title="Info", description="Depresso", color=0xCCCC00)
            embed.add_field(name="Developer", value="Soariticus#0666", inline=False)
            embed.add_field(name="Discord", value="https://discord.gg/3PFzFb7",
                            inline=False)
            embed.add_field(name="Creation Date",
                            value="11/12/2019",
                            inline=False)
            embed.add_field(name="Status", value="Heavy WIP", inline=False)
            await message.channel.send(delete_after=60, embed=embed)

        if message.content.startswith("=help"):
            embed = discord.Embed(title="Prefix: `=`", description="[example] < means **required** | {example} < means "
                                                                      "*optional*", color=0xCCCC00)
            embed.add_field(name="Fun:", value="`howgay [user]` "
                                                   "`=clap [sentence]` `space [sentence]` `8ball {question}`",
                                inline=False)
            embed.add_field(name="Functional:", value="`help` `info` `userinfo [user]` `poll (or poll:)`",
                                inline=False)
            if guildID == 478070785345454080:
                embed.add_field(name="Server Specific (Playground):", value="`uo [server]`", inline=False)
            embed.add_field(name="Owner:", value="`p [amount]` `c [channelID] [text]` `t`", inline=False)
            await message.channel.send(delete_after=60, embed=embed)

        if message.content.startswith("=userinfo"): # shitty way of taking input, I still need to rework depresso
            name = None # Setting the default value so that the 'if' statement will trigger, old code, its kinda meh
            if name is None: # Obvious enough
                try: # It will first TRY this.
                    user = message.mentions[0] # We're assigning the first mention from the message to the var 'user'. If this failed (aka there is no user mentioned in the message) it will error with "IndexError"
                except IndexError:  # We catch the IndexError, and process it.
                    user = message.author  # Setting the 'user' variable
                if user is None:  # This used to work in an earlier version, I don't know if it still does, if the user had left the server it would become 'None', as such this.
                    await message.channel.send('Could not find user.')
                    return

            if isinstance(user, discord.Member):
                role = user.top_role.name
                if role == "@everyone":
                    role = "N/A"
                voice_state = None if not user.voice else user.voice.channel
                em = discord.Embed(timestamp=message.created_at, colour=0xCCCC00)
                em.add_field(name='User ID', value=user.id, inline=True)
                if isinstance(user, discord.Member):
                    em.add_field(name='Nick', value=user.nick, inline=True)
                    em.add_field(name='Status', value=user.status, inline=True)
                    em.add_field(name='In Voice', value=voice_state, inline=True)
                    em.add_field(name='Game', value=user.activity, inline=True)
                    em.add_field(name='Highest Role', value=role, inline=True)
                em.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
                if isinstance(user, discord.Member):
                    em.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
                em.set_author(name=user)
                await message.channel.send(delete_after=120, embed=em)

        if message.content.startswith("=clap"):
            text = message.content.split()
            newtext = " :clap: ".join(text[1:])
            await message.channel.send(newtext)

        if message.content.startswith("=space"):
            text = message.content
            text = text.replace(" ", "")
            text = list(text)
            newtext = " ".join(text[6:])
            await message.channel.send(newtext)

        if message.content.startswith("=8ball"):
            option = random.randint(0, 10)
            if option is 0:
                await message.channel.send("yessir")
            elif option is 1:
                await message.channel.send("nah brother")
            elif option is 2:
                await message.channel.send("maybe")
            elif option is 3:
                await message.channel.send("for sure")
            elif option is 4:
                await message.channel.send("sure as hell")
            elif option is 5:
                await message.channel.send("roll again")
            elif option is 6:
                await message.channel.send("hell to the nah")
            elif option is 7:
                await message.channel.send("no, no, no, no, no")
            elif option is 8:
                await message.channel.send("how am i supposed to know? im just a computer doing RNG leave me alone")
            elif option is 9:
                await message.channel.send("Only monday-wednesday")
            elif option is 10:
                await message.channel.send("Only thursday-sunday")
            else:
                await message.channel.send("definitely")

        if guildID == 478070785345454080:
            if "cunt" in message.content:
                await message.delete()
                await message.channel.send(f"{message.author.mention} you did a bad.", delete_after=5)

        if message.content.lower().startswith("poll:") or message.content.lower().startswith("=poll"):
            reactions = ['✅', '❌', '🤷']
            for emoji in reactions:
                await message.add_reaction(emoji)

        if message.channel.id in suggestionChannel:
            if "suggestion" not in message.content.lower() or "reason" not in message.content.lower():
                if message.author.id not in staff:
                    await message.delete()
                    await message.channel.send(f"{message.author.mention} please use the correct format as seen in the pinned message.", delete_after=10)
            else:
                reactions = ['✅', '❌']
                for emoji in reactions:
                    await message.add_reaction(emoji)

        if message.content.startswith("=uo"):
            global output
            args = message.content.split()
            b = battle()
            users = b.getServer(args[1].lower())
            if users == "Cannot find that server. Try again.":
                await message.channel.send(users)
            else:
                embed = discord.Embed(title="The Playground", description=output, color=0x00ff00)
                embed.add_field(name=f"Users online on {output}:", value=users, inline=False)
                await message.channel.send(embed=embed)

        if message.author.id in staff:
            if message.content.startswith("=p"):
                args = message.content.split()
                amt = int(args[1])
                amt += 1
                if amt > 1000:
                    amt = 1000
                await message.channel.purge(limit=amt)

            if message.content.startswith("=t"):
                await message.delete()
                text = input("What'd you like to say?")
                await message.channel.send(text)

        if message.content.startswith("=p"):
            await message.delete()

        if message.content.startswith("=c"):
            await message.delete()
            if message.author.id == owner:
                args = message.content.split()
                chan = int(args[1])
                mssg = args[2:]
                chan = self.get_channel(chan)
                mssg = " ".join(mssg)
                await chan.send(mssg)
            else:
                pass


client = MyClient()
client.run('YOUR TOKEN HERE')
