import discord

token = input()
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if 'dorchadas' in message.content.lower():
            await message.channel.send(file=discord.File('./dorchadas.jpg'))
    
client.run(token)
