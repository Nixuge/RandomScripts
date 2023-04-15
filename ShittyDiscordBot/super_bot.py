import discord
from discord.ext import commands
import time

DISCORD_TOKEN = "OTc4MDc0MDA3OTE4MjIzMzcy.G_zaEj.vNO7nb32YmKwO_ZqQ3xXXS-uYg3ZYje_feERSc"
VOCAL_ID = 978076101865799694

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!',intents=intents)


def get_channel(ctx):
    for channel in ctx.guild.channels:
        if channel.id == VOCAL_ID:
           return channel

async def join(ctx):
    await get_channel(ctx).connect()

async def play(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client
    filename = "cta3.mp3"
    while True:
        try :
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=filename))
            time.sleep(2)
        except Exception as e:
            pass
            # await ctx.send(str(e))


@bot.command(name='play')
async def play_command(ctx):
    await join(ctx)
    await play(ctx)



if __name__ == "__main__" :
    bot.run(DISCORD_TOKEN)
    