import os
import discord
import youtube_dl

class MyClient(discord.Client):
  async def on_ready(self):
    print("Logged on as", self.user)

  async def on_message(self, message):
    if message.author == self.user:
      return
      
    if message.content == "ping":
      await message.channel.send("pong")

    if message.content == "I'm lonely":
      await message.channel.send("Then let me slide into your DMs ;)",embed=discord.Embed(title="lol you freaking fool",url="https://www.google.com/"))


client = MyClient()
client.run(os.environ['TOKEN'])