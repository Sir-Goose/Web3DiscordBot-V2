from typing import List, Union

def format_imp(output: float) -> str:
    rounded_output = round(output, 2)
    return f"```IMP ${rounded_output} ```"

def format_imp_status(output: float) -> str:
    rounded_output = round(output, 2)
    return f"IMP ${rounded_output}"

def format_cg(output_list: List[Union[str, float]]) -> str:
    price, change, token_id = output_list
    token_id_str = str(token_id).upper()
    price_str = f"{price:.2f}" if isinstance(price, float) else str(price)
    change_str = f"{change:.2f}" if isinstance(change, float) else str(change)
    return f"```{token_id_str} ${price_str} ({change_str}% 24h)```"

def format_historical_cg(output: float, date: str, token_id: str) -> str:
    rounded_output = round(output, 2)
    formatted_output = '{:,}'.format(rounded_output)
    return f"```{token_id} was ${formatted_output} on {date}```"

def format_conversion(output: float) -> str:
    rounded_output = round(output, 2)
    formatted_output = '{:,}'.format(rounded_output)
    return f"```{formatted_output}```"

def format_status(output: float) -> str:
    rounded_output = round(output, 2)
    return f"IMP {rounded_output} USD"

def format_stock(token: str, output: float) -> str:
    price = round(output, 2)
    token = token.upper()
    return f"```{token} ${price} USD```"
