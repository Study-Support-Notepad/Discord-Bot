from discord.ext import commands
import discord

intents = discord.Intents.all()
TOKEN = "no Token"  # Tokenは今後.env, settings.pyで読み込む
prefix = "s"

bot = commands.Bot(command_prefix=prefix, help_command=None, intents=intents)

bot.load_extension("main")

bot.run(TOKEN)
