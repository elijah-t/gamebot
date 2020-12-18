import json
import discord
from discord.ext import commands

with open('config.json') as f:
    config = json.load(f)

client = commands.Bot(command_prefix=config['prefix'])

client.load_extension("cogs.TicTacCog")

#on_ready()
#Prints a message when the bot is ready to use.
@client.event
async def on_ready():
    print('{0.user} is online.'.format(client))

#ping(ctx)
#Sends the ping between the bot and the server.
@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

#who(ctx)
#Sends an embed about the game bot itself, and the creator.
@client.command()
async def who(ctx):
    embed=discord.Embed(title="Game Bot", url="https://github.com/elijah-t/gamebot", description="A discord bot that plays simple games.", color=0x736dd0)
    embed.set_thumbnail(url="https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/120/twitter/259/video-game_1f3ae.png")
    embed.add_field(name="Written in:", value="Python", inline=True)
    embed.add_field(name="Code by:", value="Elijah Tungul", inline=True)
    embed.set_footer(text="If you found this, you're cool :)")
    await ctx.send(embed=embed)

client.run(config['token'])