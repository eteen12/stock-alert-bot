import yfinance as yf
import json

with open('config.json') as f:
    stocks = json.load(f)
    tickers = stocks['tickers']


def get_stock_info(tickers):
    info_list = []
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        info = stock.info
        ticker = info.get("symbol",ticker)
        name = info.get("longName", "N/A")
        price = info.get("regularMarketPrice", "N/A")
        percent_change = info.get("regularMarketChangePercent", None)
        info_list.append({
            "ticker":ticker,
            "name": name,
            "price": price,
            "percent change": percent_change,
        })
    return info_list


def format_stock_info():
    stocks = get_stock_info(tickers)
    lines = [f"{'Ticker':<8} | {'Price':>10} | {'Change %':>9}"]

    for stock in stocks:
        ticker = stock['ticker'].replace('.', '-')
        price = stock['price'] if isinstance(stock['price'], (int, float)) else 0
        percent_change = stock['percent change'] if isinstance(stock['percent change'], (int, float)) else 0
        line = f"{ticker:<8} | ${price:>9.2f} | {percent_change:>7.2f} %"
        lines.append(line)

    return "\n".join(lines)

print(format_stock_info())