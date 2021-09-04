import time
from asyncio.tasks import sleep
import discord
from discord.ext import commands

secret = open("secret").read()

print("mimiyuuuH2O")
bot = commands.Bot(command_prefix="~")


def play_source(vc, duration):
    if duration is not None:
        time.sleep(int(duration))
    else:
        time.sleep(1500)

    while True:
        vc.play(discord.FFmpegPCMAudio('drink.mp3'), after=lambda e: play_source(vc, duration))
            
    
@bot.command()
async def join(ctx, duration=None):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        vc = await channel.connect()
        play_source(vc, duration)


@bot.command()
async def leave(ctx):
    print("mimiyuuuH2O Leaves")
    await ctx.voice_client.disconnect()

bot.run(secret)
