import discord
from discord.ext import commands
from discord import app_commands

TOKEN = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
CHANNEL_ID = xxxxxxxxxxxxxxxxxx

intents = discord.Intents.default()
intents.reactions = True
intents.messages = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

COMPLETED_EMOJI = "✅"

@client.event
async def on_ready():
    print("on_ready")
    await tree.sync()

@tree.command(name="add", description="課題をスレッドに追加")
async def add_command(interaction: discord.Interaction, title: str, month: int, day: int, weekday: str, content: str):
    embed = discord.Embed(title=title, color=discord.Colour.blue())
    deadline_str = f"{month}月{day}日 ({weekday})"
    embed.add_field(name="期限", value=deadline_str, inline=False)
    embed.add_field(name="内容", value=content, inline=False)

    channel = client.get_channel(CHANNEL_ID)
    message = await channel.send(embed=embed)

    await message.add_reaction(COMPLETED_EMOJI)

    await interaction.response.send_message("added the task!")

client.run(TOKEN)
