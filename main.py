import discord
from discord.ext import commands
from discord.ext.commands import Context
from podcast import podcast_feed
import io


client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    await client.process_commands(message)


@client.command(name='ping', help='pong')
async def ping(ctx: Context):
    await ctx.reply('pong')


@client.command(name='play', help='播放檔案')
async def play(ctx: Context, url: str=None):
    if not url:
        await ctx.reply('請給我 Google Podcast 網址。')
        return
    if 'podcasts.google.com' not in url:
        await ctx.reply('請給我正確的 Google Podcast 網址。')
        return

    files = podcast_feed(url)
    if not files:
        await ctx.reply('檔案解析失敗。')
        return

    # connect to voice channel
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()

    # try:
    server = ctx.message.guild
    voice_channel = server.voice_client
    async with ctx.typing():

        # with open('xxx.mp3', 'w') as f:
        #     f.write(files)

        # wrapper = open('xxx.mp3', 'rb').read()

        voice_channel.play(discord.FFmpegPCMAudio(source='aaa.mp3'))
    # await ctx.send('**Now playing:** {}'.format(filename))
    # except:
    await ctx.send("The bot is not connected to a voice channel.")
        # raise

@client.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client and voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")



