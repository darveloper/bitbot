import discord
import logging
import os
import requests
import json

from discord.ext import commands

'''For Logging'''
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='bit-discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!welcome'):
        member = message.author
        await member.send('Hi')
        await message.channel.send('Welcome to the BiT Community!')
    
    if message.content.startswith('!motivate'):
        channel = client.get_channel(915633826779267073)
        quote = get_quote()
        await message.channel.send(quote)

    # if message.content.startswith('!help'):
    #     me


@client.event
async def on_member_join(member):
        role = discord.utils.get(guild.roles, id='847510190172930108')
        print(role)
        await member.add_roles(member, role)
        await member.send('Welcome to the BiT Discord Community!')

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

client.run('OTE1NjI1NzE1OTY4Mzc2ODMy.YaeU5g.DuiaQe910VztXrYYlqYBi2ohDeQ')

