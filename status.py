import time
import discord
import random

import formatter
import price

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # lists servers bot is in
    print(client.guilds)
    token = 'imp'
    type = ''
    while True:
        try:
            output = price.get_imp_price(token, type)
            output = formatter.format_status(output)
            await client.change_presence(activity=discord.Game(name=output))
            print(f"<Status Updated>")
        except:
            print(f"<Status Update Failed")
        time.sleep(random.randint(300, 400))


client.run('')
