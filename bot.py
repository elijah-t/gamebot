import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix='$')

client.load_extension("cogs.TicTacCog")

@client.event
async def on_ready():
    print('{0.user} is online.'.format(client))

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

@client.command()
async def who(ctx):
    embedVar = discord.Embed(title="Game Bot", description="A discord bot that plays simple games.", color=0x00ff00)
    embedVar.add_field(name="Code written by:", value="Elijah Tungul", inline=True)
    await ctx.send(embed=embedVar)

client.run("Nzg4OTU0Mjk1NzMwODMxMzgw.X9rA8g.KSj5Ub-8NIP-kfxHZZM5JeMVAwk")