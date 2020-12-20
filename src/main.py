import os
import discord
import paramiko
import time

TOKEN = os.getenv('DISCORD_TOKEN')
slashem_user = os.getenv('USER')
slashem_pass = os.getenv('PASS')
discord_client = discord.Client()
ssh_client = paramiko.SSHClient()


@discord_client.event
async def on_ready() -> None:
    print(f'{discord_client.user} is connected.\n')


@discord_client.event
async def on_message(message: str) -> None:
    # ignore messages from ego
    if message.author == discord_client.user:
        return

    # todo, parse message content and run discord cmd on ssh
    if message.content == 'slashem!':
        slashem_screen = call_ssh(message.content)
        output = slashem_screen.encode('utf8').decode('latin-1')
        await message.channel.send(output)


def call_ssh(slashem_command: str) -> str:
    screen = "Something went wrong"
    try:
        print('connecting to ssh')
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname='alt.org', username='nethack', password='')
        stdin, stdout, stderr = ssh_client.exec_command('')

        print('logging into slashem account')
        stdin.write(f'l{slashem_user}\n{slashem_pass}\npp')
        stdin.flush()

        print('closing stdin and reading stdout')
        stdin.channel.shutdown_write()
        screen = 'NetHack' + stdout.read().decode().split('NetHack')[-1]
        print(f'slashem screen: {screen}')

    finally:
        print('ending ssh session')
        ssh_client.close()

    return screen


if __name__ == "__main__":
    # start the client
    discord_client.run(TOKEN)
    # call_ssh('')
