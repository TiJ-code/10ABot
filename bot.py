import discord
import asyncio


default_channel = discord.TextChannel


class Edgar(discord.Client):
    def __init__(self, *args, **kwargs):
        global default_channel
        super().__init__(*args, **kwargs)
        default_channel = self.get_channel(798147945396568098)

    async def on_ready(self):
        print(f'Logging in as {self.user}')

    async def on_message(self, msg):
        if msg.author.id == self.user.id:
            return

        curseWords = ['discode', 'discord.ccom']

        if any(word in msg.content for word in curseWords):
            await msg.delete()


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
