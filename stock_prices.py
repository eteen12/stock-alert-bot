import yfinance as yf

tickers = ["UNH","BLK","BX","TSLA","IVV","BAM.TO"]

def get_stock_info(tickers):
    info_list = []
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        info = stock.info
        ticker = info.get("symbol",ticker)
        name = info.get("longName", "N/A")
        price = info.get("regularMarketPrice", "N/A")
        info_list.append({
            "ticker":ticker,
            "name": name,
            "price": price,
        })
    return info_list


def format_stock_info():
    stocks = get_stock_info(tickers)
    lines = [f"{'Ticker':<8} | {'Price':>10}"]

    for stock in stocks:
        ticker = stock['ticker'].replace('.', '-')
        price = stock['price'] if isinstance(stock['price'], (int, float)) else 0
        line = f"{ticker:<8} | ${price:>9.2f}"
        lines.append(line)

    return "\n".join(lines)
