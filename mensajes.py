import os
import discord
from dotenv import load_dotenv
from db.connectionDb import altaDatosDiscord


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=discord.Intents.all())
nombrePost=''
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
    

# Obtengo los mensajes escritos en las publicaciones de un foro
@client.event
async def on_message(message):
    print('mensaje de post nueva publi' )
    if message.channel.name == 'nueva publi': # Reemplaza 'nombre_del_canal' con el nombre del canal que deseas monitorear
        print(f'{message.author.name}: {message.content}')



#Obtener titulo y mensaje de nuevo mensaje de post
@client.event
async def on_message(post):
    print('nuevo posteo')
    #print(f'Titulo: {post.channel.name}')# imprime el titulo del posteo
    print(f'Usuario:{post.author.name}\nTitulo: {post.channel.name}\nMensaje: {post.content}') #imprime autor y mensaje del post
    title = post.channel.name
    autor = post.author.name
    data = post.content
    print(f'variable title:{title} - Variable autor: {autor} - Varialbe data: {data}')
    altaDatosDiscord(autor,title, data)




client.run(TOKEN)