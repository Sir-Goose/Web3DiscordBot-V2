import discord
import pandas as pd
from discord.ext import commands, tasks
import charting
import formatter
import price
import sys
from typing import List, Dict, Union, Optional, cast

intents = discord.Intents.default()
intents.presences = True
intents.message_content = True

client = discord.Client(intents=intents)

cg_tokens_dict: Dict[str, str] = pd.read_csv('cgtokens.csv', header=None, index_col=0).squeeze(axis='columns').to_dict()
print("csv loaded")

@client.event
async def on_ready() -> None:
    print('We have logged in as {0.user}'.format(client))
    print(client.guilds)
    set_status.start()

def get_status() -> str:
    status = price.get_imp_price("imp")
    status = formatter.format_imp_status(status)
    return status

@tasks.loop(minutes=30)
async def set_status() -> None:
    print("Attempting to set status")
    status = get_status()
    await client.change_presence(activity=discord.Game(name=status))
    print(f'Status updated to: {status}')

@client.event
async def on_message(message: discord.Message) -> None:
    if message.author == client.user:
        return
    print(f"{message.author}: {message.content}")
    is_meta = meta_joke(message.content)
    if is_meta:
        reply = "Did you mean Facebook?"
        await message.channel.send(reply, reference=message)
        print(f"<{reply}>")
        return

    user_message_list = message.content.split()
    print(user_message_list)
    output = control_flow(user_message_list)
    if output is None:
        return
    elif output == 'chart.png':
        print("sending chart")
        with open('chart.png', 'rb') as chart:
            picture = discord.File(chart)
            await message.channel.send(file=picture, reference=message)
    elif output!= True:
        print(f"<{output}>")
        await message.channel.send(str(output), reference=message)
    elif output:
        emoji = '\N{THUMBS UP SIGN}'
        await message.add_reaction(emoji)
        print(f"<{emoji}>")
        return

def control_flow(user_message_list: List[str]) -> Optional[Union[str, bool]]:
    user_message_prefix = user_message_list[0].lower()

    if len(user_message_list) < 2:
        raise ValueError("Token not provided in the message")

    token = user_message_list[1].lower()

    try:
        period = user_message_list[2].lower()
        interval = user_message_list[3].lower()
        date = user_message_list[2]
    except IndexError:
        period = interval = date = None

    if user_message_prefix == '$p':
        if token == 'imp':
            output = price.get_imp_price(token)
            output = formatter.format_imp(output)
            return output
        else:
            type = 'current'
            output_list = price.get_cg_price(token, type, cg_tokens_dict)
            output = formatter.format_cg(output_list)
            return output

    if user_message_prefix == '$h':
        if token == 'imp':
           ...
        else:
            if date is None:
                raise ValueError("Date not provided for historical price")
            output, token_id = price.get_historical_price_cg(token, date, cg_tokens_dict)
            output = formatter.format_historical_cg(output, date, token_id)
            return output

    if user_message_prefix == '$request':
        bool = record_request(user_message_list)
        if bool:
            return True

    if user_message_prefix == '$convert':
        output = convert_tokens(user_message_list, cg_tokens_dict)
        output = formatter.format_conversion(output)
        return output

    if user_message_prefix == '$imp':
        token = 'imp'
        output = price.get_imp_price(token)
        output = formatter.format_imp(output)
        return output

    if user_message_prefix == '$s' or user_message_prefix == '$stock':
        output = price.get_stock_price(token)
        output = formatter.format_stock(token, output)
        return output

    if user_message_prefix == '$c' or user_message_prefix == '$chart':
        output = charting.get_chart(token, period, interval)
        return output

def convert_tokens(user_message_list: List[str], cg_tokens_dict: Dict[str, str]) -> float:
    if len(user_message_list) < 4:
        raise ValueError("Not enough arguments. Usage: $convert <quantity> <token1> <token2>")

    quantity_one = user_message_list[1]
    token_one = user_message_list[2]
    token_two = user_message_list[3]

    type = 'current'

    token_one_price = price.get_cg_price(token_one, type, cg_tokens_dict)
    if token_one_price is None or not token_one_price:
        raise ValueError(f"Unable to get price for {token_one}")
    token_one_price = cast(str, token_one_price[0]).replace(',', '')

    token_two_price = price.get_cg_price(token_two, type, cg_tokens_dict)
    if token_two_price is None or not token_two_price:
        raise ValueError(f"Unable to get price for {token_two}")
    token_two_price = cast(str, token_two_price[0]).replace(',', '')

    try:
        output = (float(token_one_price) * float(quantity_one)) / float(token_two_price)
        return output
    except ValueError:
        raise ValueError("Invalid numeric values for prices or quantity")

def record_request(user_message_list: List[str]) -> bool:
    message_text = '.join(user_message_list)

    with open('requests.txt', 'a') as external_file:
        print(message_text, file=external_file)
        external_file.close()
        return True

def meta_joke(message: List[str]) -> bool:
    for word in message:
        if word.lower() == 'eta':
            return True
    return False

def get_key() -> str:
    try:
        with open('key.txt', 'r') as file:
            key = file.read().strip()
            return str(key)
    except FileNotFoundError:
        print("Error: The file 'key.txt' was not found.")
        sys.exit(1)
    except IOError:
        print("Error: There was an issue reading the file.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

client.run(get_key())
