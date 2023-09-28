import discord

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('nasılsın'):
        await message.channel.send("merhaba")
    elif message.content.startswith('görüşürüz'):
        await message.channel.send("görüşürüz dostum")
    else:
        await message.channel.send(message.content)

client.run("MTE1Njk1ODUwMjI5MjU1Mzc0OA.GVOYo0.UUkSf6XrDzgOfCNwFKV2PmMyoY6klteRwkvhGY")
