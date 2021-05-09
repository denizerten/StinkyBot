import discord
import asyncio
import os
from runKey import runKey
bot = discord.Client()

@bot.event
async def on_message(message):
    if message.content == 'stinky':
        await message.channel.send("Hello, you can see what I am capable of by typing 'stinky i need help'.")

    if message.content == 'stinky i need help':
        await message.channel.send("""```All commands begin with 'stinky'\n\nTo get a full list of what I can do type 'stinky i really need help'\n\nExamples:\nstinky what are you doing\nstinky how are you```
        """)

    if message.content == 'stinky i really need help':
        await message.channel.send("```All Commands:\n\nstinky what are you doing\nstinky how are you```")



    if message.content == 'stinky what are you doing':
        await message.channel.send("I am talking to a dumbass")

    if message.content == 'stinky how are you':
        await message.channel.send("I am still breathing")





bot.run(runKey)

# https://discord.com/oauth2/authorize?client_id=838547876270702633&scope=bot&permissions=68608
