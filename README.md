# Crypto Discord Bot

A Discord bot that provides real-time cryptocurrency prices, charts, and conversions.

## Features

* Get current prices of various cryptocurrencies
* View historical prices of cryptocurrencies
* Convert between different cryptocurrencies
* Get charts of cryptocurrency prices
* Get stock prices

## Requirements

* Python 3.x
* discord.py
* pandas
* PyCoinGecko
* web3
* yfinance
* mplfinance

## Installation

1. Clone this repository or download the code.
2. Install the required dependencies:
   ```
   pip install discord.py pandas pycoingecko web3 yfinance mplfinance
   ```
3. Create a `key.txt` file with your Discord bot token.
4. Create a `cgtokens.csv` file with the CoinGecko token IDs.

## Usage

* `$p <token>`: Get the current price of a cryptocurrency.
* `$h <token> <date>`: Get the historical price of a cryptocurrency.
* `$convert <quantity> <token1> <token2>`: Convert between two cryptocurrencies.
* `$chart <token> <period> <interval>`: Get a chart of a cryptocurrency's price.
* `$stock <token>`: Get the current price of a stock.

## How It Works

The bot uses the CoinGecko API to fetch cryptocurrency prices and the yfinance library to fetch stock prices. The bot also uses the mplfinance library to generate charts. 
For FTM it the price is calculated using onchain data.


## Contributing

Feel free to fork this project and submit pull requests with improvements or bug fixes.
