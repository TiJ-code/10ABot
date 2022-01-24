import discord
import asyncio


class Edgar(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.default_channel = self.get_channel(798147945396568098)

    async def on_ready(self):
        print(f'Logging in as {self.user}')

    async def on_message(self, msg):
        if msg.author.id == self.user.id:
            return

        curseWords = ['discode', 'discord.ccom']

        if any(word in msg.content for word in curseWords):
            #await msg.delete()
            await self.msg.channel.send(f"LOL! {msg.author.mention} hats erwischt! POGGERS")
            await send_dm(530758332882092032, "Es hat wieder wen erwischt")


async def send_dm(member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(content)


def getRunToken():
    file = open('exams.txt', 'r')
    line = file.readline()
    file.close()
    out = line.replace('!', '')
    out = out.replace(' ', '')
    return out


client = Edgar()
client.run(getRunToken())
