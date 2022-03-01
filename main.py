from discord.ext import commands
from discord.ext.commands import Context

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    await client.process_commands(message)


@client.command(name='ping', help='pong')
async def test(ctx: Context):
    await ctx.reply('pong')


