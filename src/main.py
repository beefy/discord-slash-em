import os
import discord
import paramiko
from ansitoimg.render import ansiToRaster

TOKEN = os.getenv('DISCORD_TOKEN')
SLASHEM_USER = os.getenv('USER')
SLASHEM_PASS = os.getenv('PASS')
DISCORD_CLIENT = discord.Client()
SSH_CLIENT = paramiko.SSHClient()


@DISCORD_CLIENT.event
async def on_ready() -> None:
    print(f'{DISCORD_CLIENT.user} is connected.\n')


@DISCORD_CLIENT.event
async def on_message(message: str) -> None:
    # ignore messages from ego
    if message.author == DISCORD_CLIENT.user:
        return

    # todo, parse message content and run discord cmd on ssh
    if message.content == 'slashem!':
        slashem_screen = call_ssh(message.content)
        await message.channel.send(slashem_screen)


def call_ssh(slashem_command: str) -> str:
    screen = "Something went wrong"
    try:
        print('connecting to ssh')
        SSH_CLIENT.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        SSH_CLIENT.connect(hostname='alt.org', username='nethack', password='')
        stdin, stdout, stderr = SSH_CLIENT.exec_command('')

        print('logging into slashem account')
        stdin.write(f'l{SLASHEM_USER}\n{SLASHEM_PASS}\npp')
        stdin.flush()

        print('closing stdin and reading stdout')
        stdin.channel.shutdown_write()
        screen = 'NetHack' + stdout.read().decode().split('NetHack')[-1]
        print(f'slashem screen: {screen}')

    finally:
        print('ending ssh session')
        SSH_CLIENT.close()

    output = screen.encode('utf8')
    # ValueError: invalid literal for int() with base 10: '3;1H         By Stichting Mathe'
    # ansiToRaster(output, "screen.png")
    return screen


if __name__ == "__main__":
    # start the client
    # DISCORD_CLIENT.run(TOKEN)
    call_ssh('')
