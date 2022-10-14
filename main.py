import os, discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(description='Sample status', guild_subscriptions=True, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Logged in as:\n{bot.user.name}\n{bot.user.id}')
    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('hello'):
        await message.channel.send('Hello!')
    
bot.run(TOKEN)