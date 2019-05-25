import os
import discord
from discord.utils import get

TOKEN=os.environ['TOKEN']
TARGET_ID=os.environ['TARGET_ID']
TARGET_ROLE=os.environ['TARGET_ROLE']
EMOTE=os.environ['EMOTE']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as', self.user)

    async def on_message(self, message):
        emote = get(message.guild.emojis, name=EMOTE)

        if message.author == self.user:
            return

        if message.author.id == int(TARGET_ID):
            await message.add_reaction(emote)

        if TARGET_ROLE.lower() in [i.name.lower() for i in message.author.roles]:
            await message.add_reaction(emote)

client = MyClient()
client.run(TOKEN)

