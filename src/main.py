import os
import discord
from dotenv import load_dotenv
import subprocess

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} is connected.\n')

@client.event
async def on_message(message):
    # ignore messages from ego
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        # response = random.choice(brooklyn_99_quotes)
        await message.channel.send(brooklyn_99_quotes[2])

    # res = subprocess.Popen("ssh {user}@{host} {cmd}".format(user=user, host=host, cmd=message), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

client.run(TOKEN)
