def format_imp(output):
    output = round(output, 2)
    # output = "```" + "IMP $" + str(output) + "```"
    output = f"```IMP ${str(output)} ```"
    return output


def format_cg(output_list):
    price = output_list[0]
    change = output_list[1]
    token_id = output_list[2]
    # output = "```" + token_id.upper() + " $" + str(price) + " (" + str(
    # change) + "%" + " 24h" + ")" + "```"
    output = f"```{token_id.upper()} ${str(price)} ({str(change)}% 24h)```"
    return output


def format_historical_cg(output, date, token_id):
    output = round(output, 2)
    output = '{:,}'.format(output)
    # output = "```" + token_id + " $" + str(output) + " at " + date + "```"
    output = f"```{token_id} was ${str(output)} on {date}```"
    return output


def format_conversion(output):
    output = round(output, 2)
    output = '{:,}'.format(output)
    # output = "```" + output + "```"
    output = f"```{output}```"
    return output


def format_status(output):
    output = round(output, 2)
    output = f"IMP {str(output)} USD"
    return output
