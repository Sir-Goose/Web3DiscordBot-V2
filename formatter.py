from typing import List, Union

def format_imp(output: float) -> str:
    output = round(output, 2)
    output = f"```IMP ${str(output)} ```"
    return output

def format_imp_status(output: float) -> str:
    output = round(output, 2)
    output = f"IMP ${str(output)}"
    return output

def format_cg(output_list: List[Union[str, float]]) -> str:
    price, change, token_id = output_list
    output = f"```{token_id.upper()} ${str(price)} ({str(change)}% 24h)```"
    return output

def format_historical_cg(output: float, date: str, token_id: str) -> str:
    output = round(output, 2)
    output = '{:,}'.format(output)
    output = f"```{token_id} was ${str(output)} on {date}```"
    return output

def format_conversion(output: float) -> str:
    output = round(output, 2)
    output = '{:,}'.format(output)
    output = f"```{output}```"
    return output

def format_status(output: float) -> str:
    output = round(output, 2)
    output = f"IMP {str(output)} USD"
    return output

def format_stock(token: str, output: float) -> str:
    price = round(output, 2)
    token = token.upper()
    output = f"```{token} ${price} USD```"
    return output
