import os
import re
import discord
import gtts
#import youtube_dl
import ctypes
import ctypes.util
import time
import asyncio
from mutagen.mp3 import MP3

print("ctypes - Find opus:")
a = ctypes.util.find_library('opus')
print(a)
 
print("Discord - Load Opus:")
b = discord.opus.load_opus(a)
print(b)
 
print("Discord - Is loaded:")
c = discord.opus.is_loaded()
print(c,'\n\n')


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
      #still don't know how to directly message people :(
    
    if re.search("\A>play\s",message.content):
      await message.channel.send("lol nice")


    #A pretty cool Text to speech feature
    if re.search("\A>tts\s", message.content):
      if len(message.content) < 1000:
        #await message.channel.send("Extracting message and transforming to file")
        msg = re.sub("\A>tts\s", "", message.content)
        tts = gtts.gTTS(msg)
        tts.save("tts.mp3")
        
        channel = message.author.voice.channel
        if channel != None:
          #await message.channel.send("Joining your channel and playing the file")
          vc = await channel.connect(reconnect=True)

          audioFile = MP3("tts.mp3")
          duration = audioFile.info.length
          player = vc.play(discord.FFmpegOpusAudio("tts.mp3"))
          while duration > 0:
            await asyncio.sleep(1)
            duration-=1

          #await message.channel.send("Cya, hope you liked it!")
          await vc.disconnect()

        else:
          await message.channel.send("Please join a Voice Channel before you use this command")

      else:
        await message.channel.send("Nope, your message is too long.")
  



client = MyClient()
client.run(os.environ['TOKEN'])