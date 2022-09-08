import discord
from discord.ext import commands
#MTAxNzM1MTQyNzU4MjA3NDkzMQ.GQVoQF.Js6DsOEzbLZeVpda5he-ahqEU53pZKvV3dOUU4





intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$',intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


bot.run('MTAxNzM1MTQyNzU4MjA3NDkzMQ.GQVoQF.Js6DsOEzbLZeVpda5he-ahqEU53pZKvV3dOUU4')

