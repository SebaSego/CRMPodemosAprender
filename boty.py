import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    #Obtener todos los miembros del servidor
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

    #Obtener los foros por nombre

    forums = '\n - '.join([forum.name for forum in guild.forums])
    print(f'Foros creados por nombre:\n - {forums}')

@client.event
async def on_message(message):
    if message.channel.name == 'foronuevo': # Reemplaza 'nombre_del_canal' con el nombre del canal que deseas monitorear
        print(f'{message.author.name}: {message.content}')

client.run(TOKEN)