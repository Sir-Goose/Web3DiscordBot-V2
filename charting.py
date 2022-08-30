import yfinance as yf
import mplfinance as mpf


def get_chart(token, period, interval):
    ticker = yf.Ticker(token)
    mc = mpf.make_marketcolors(up='#00bed4', down='#eb4d5c', edge='#131722', inherit=True)
    custom = mpf.make_mpf_style(base_mpf_style='nightclouds', facecolor='#131722', figcolor='#131722', marketcolors=mc)

    mpf.plot(ticker.history(period=period, interval=interval, actions=False), title=token.upper(), type='candle', style=custom,
             savefig=dict(fname='chart', bbox_inches='tight'))
    return 'chart.png'

