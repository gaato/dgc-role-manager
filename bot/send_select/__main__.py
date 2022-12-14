import os
import pathlib

import discord
from dotenv import load_dotenv

from ..views import SelectView1
from .. import config


HERE = pathlib.Path(__file__).parent

load_dotenv()
intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")
    print("------")
    button_channel = client.get_channel(config.select_channel_id)
    view = SelectView1(client)
    await button_channel.send('What language do you speak?\nあなたの話せる言語を選択してください。（複数選択可）', view=view)
    await client.close()


client.run(os.environ.get('DISCORD_TOKEN'))
