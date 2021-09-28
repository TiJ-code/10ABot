import asyncio
import discord
from datetime import datetime


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.status_task = self.loop.create_task(self.statusTask())

    async def on_ready(self):
        print(f'Logging as {self.user}')

    async def statusTask(self):
        await self.wait_until_ready()
        while not self.is_closed():
            await self.change_presence(
                activity=discord.Activity(name=str(self.updateCountdown()), type=5),
                status=discord.Status.do_not_disturb
            )
            await asyncio.sleep(10)

    def updateCountdown(self):
        file = open("exams.txt", "r")
        Lines = file.readlines()

        title = ""

        for line in Lines:
            if line.startswith('#'):
                title = line.split(' ')[1]
            else:
                delta = line.split('\n')
                delta = delta[0].split('/')

                td = int(delta[0])
                tm = int(delta[1])
                ty = int(delta[2])

                nowdate = datetime.today().strftime('%d/%m/%y/%H/%M/%S').split('/')

                nd = int(nowdate[0])
                nm = int(nowdate[1])
                ny = int(nowdate[2])
                nH = int(nowdate[3])
                nM = int(nowdate[4])
                nS = int(nowdate[5])

                now = datetime(day=nd, month=nm, year=ny, hour=nH, minute=nM, second=nS)
                target = datetime(day=td, month=tm, year=ty)

                over = target - now

                if int(str(over).split(' ')[0]) > 10:
                    rest = "".join(str(over).split(' ')[0] + " Tagen, " + str(over).split(' ')[2]) + " zu " + title
                else:
                    rest = "".join(str(over).split(' ')[0] + " Tage, " + str(over).split(' ')[2]) + " zu " + title

                return rest


client = MyClient()
client.run("ODkxMDUwMjE5MDE2NDQ1OTUy.YU4tLw.TF3OsuSfA9QBWS0-0WxP6iUb1Ec")
