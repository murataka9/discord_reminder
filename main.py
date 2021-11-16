import discord
import key

client = discord.Client()

@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)
    

tokens = key.Token()
client.run(tokens)