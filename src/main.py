import os
import discord
import paramiko

TOKEN = os.getenv('DISCORD_TOKEN')
slashem_user = os.getenv('USER')
slashem_pass = os.getenv('PASS')
discord_client = discord.Client()
ssh_client = paramiko.SSHClient()


@discord_client.event
async def on_ready():
    print(f'{discord_client.user} is connected.\n')


@discord_client.event
async def on_message(message: str) -> None:
    # ignore messages from ego
    if message.author == discord_client.user:
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


def call_ssh(slashem_command: str) -> str:
    try:
        print('connecting to ssh')
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname='alt.org', username='nethack', password='')

        print('logging into slashem account')
        stdin, stdout, stderr = ssh_client.exec_command('')
        stdin.write('l\n')
        stdin.flush()
        # stdin.write(f'{slashem_user}\n')
        # stdin.flush()
        # stdin.write(f'{slashem_pass}\n')
        # stdin.flush()
        stdin.channel.close()
        print(f'Slashem screen: {stdout.readlines()}')

    finally:
        print('ending ssh session')
        ssh_client.close()


if __name__ == "__main__":
    # start the client
    # discord_client.run(TOKEN)
    call_ssh('')
