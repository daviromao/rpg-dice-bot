import discord
from discord.ext import commands
from random import randint

TOKEN = "YOUR TOKEN"

client = commands.Bot(command_prefix = '*')

@client.event
async def on_ready():
    print("Bot is ready.")

@client.command(pass_context = True)
async def d(ctx, entry):
    username = ctx.message.author.name

    if(entry.isnumeric()):
        entry = int(entry)
        out = randint(1, entry)
        await ctx.send("**{}** rolou o  ***d{}***  e tirou: **{}**".format(username, entry, out))
        
    else:
        await ctx.send("**{}** use um número inteiro positivo! ;P".format(username))

@client.command(pass_context = True)
async def dado(ctx, entry): await d(ctx, entry)


@client.command(pass_context = True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    
    async for message in channel.history(limit=amount+1):
        if message.author == client.user:
            await discord.Message.delete(message)


client.run(TOKEN)
