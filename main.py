import discord
from discord.ext import commands
import os

TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def deposit(ctx, amount: int):
    await ctx.send(f"{ctx.author.mention} deposited {amount} coins!")

bot.run(TOKEN)
