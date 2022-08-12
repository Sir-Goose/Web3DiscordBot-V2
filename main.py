import discord
import pandas as pd

import formatter
import price

client = discord.Client()

cg_tokens_dict = pd.read_csv('cgtokens.csv', header=None, index_col=0, squeeze=True).to_dict()
print("csv loaded")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # lists servers bot is in
    print(client.guilds)


@client.event
async def on_message(message):
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
    elif output != True:
        print(f"<{output}>")
        await message.channel.send(output, reference=message)
    elif output:
        emoji = '\N{THUMBS UP SIGN}'
        await message.add_reaction(emoji)
        print(f"<{emoji}>")
        return


def control_flow(user_message_list):
    user_message_prefix = user_message_list[0].lower()
    token = user_message_list[1].lower()
    try:
        date = user_message_list[2]
    except:
        pass

    if user_message_prefix == '$p':

        if token == 'imp':
            type = 'imp_price'
            output = price.get_imp_price(token, type)
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
        type = 'imp_price'
        output = price.get_imp_price(token, type)
        output = formatter.format_imp(output)
        return output


def convert_tokens(user_message_list, cg_tokens_dict):
    quantity_one = user_message_list[1]
    token_one = user_message_list[2]
    token_two = user_message_list[3]

    type = 'current'
    token_one_price = price.get_cg_price(token_one, type, cg_tokens_dict)
    token_one_price = token_one_price[0].replace(',', '')

    token_two_price = price.get_cg_price(token_two, type, cg_tokens_dict)
    token_two_price = token_two_price[0].replace(',', '')

    output = (float(token_one_price) * float(quantity_one)) / float(token_two_price)
    return output


def record_request(user_message_list):
    message_text = ' '.join(user_message_list)

    with open('requests.txt', 'a') as external_file:
        print(message_text, file=external_file)
        external_file.close()
        return True


def meta_joke(message):
    message = message.split()
    for i in range(len(message)):
        if message[i].lower() == 'meta':
            return True
        else:
            return False


# This has to be at the bottom of the file. No idea why but it doesn't work otherwise.
client.run('MTAwNzAyOTUwMjgyNTczMDE3OQ.GdchPi.8KVQ2sUCOLaW_C4W_s0JhUlLtRwjNrjzFUSDVQ')
