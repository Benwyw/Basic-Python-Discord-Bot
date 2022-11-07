import os, discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
guild_ids = [GUILD]

bot = commands.Bot(description='Sample status', guild_subscriptions=True, intents=discord.Intents.all())

@bot.slash_command(guild_ids=guild_ids, name='test')
async def _test(ctx: commands.Context):
    """Test"""
    await ctx.defer()
    await ctx.send_followup("Test!")
    
@bot.slash_command(guild_ids=guild_ids, name='testparam')
async def _testparam(ctx: commands.Context, param):
    """Test with param"""
    await ctx.defer()
    await ctx.send_followup(f"Test! {param}")

@bot.event
async def on_ready():
    print(f'Logged in as:\n{bot.user.name}\n{bot.user.id}')
    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('hello'):
        await message.channel.send('Hello!')

if __name__ == '__main__':
    bot.run(TOKEN)
