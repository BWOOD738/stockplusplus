import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import os

end_date = datetime(2023, 10, 12, 22, 0, 0)
print(end_date)
start_date = start_date = datetime(2023, 10, 5, 9, 0, 0)
print(start_date)

## To set the display options to show all rows and columns uncomment
#pd.set_option("display.max_rows", None)  # Display all rows
#pd.set_option("display.max_columns", None)  # Display all columns

def get_stock_data(top_tickers):
    data_frames = []

    for symbol in top_tickers:
        stocks = yf.download(symbol,start = start_date, end = end_date)
        data_frames.append(stocks[["Close", "Volume"]])

    stock_data = pd.concat(data_frames, axis=1)
    stock_data.columns = pd.MultiIndex.from_product([top_tickers, ["Close", "Volume"]],names=["Ticker Symbol", "Attributes"])

    return stock_data


top_tickers = ["AAPL", "MSFT", "AMZN", "NVDA", "META", "TSLA", "GOOGL", "GOOG", "AVGO", "COST", "ADBE", "PEP", "CSCO", "CMCSA", "AMD", "TMUS", "NFLX", "INTC", "AMGN", "INTU", 
"TXN", "HON", "QCOM", "AMAT", "BKNG", "SBUX", "ADP", "ISRG", "GILD", "VRTX", "REGN", "ADI", "MDLZ", "LRCX", "PANW", "MU", "SNPS", "PDD", "CDNS", "CHTR", "KLAC", "PYPL", "CSX", 
"MELI", "MAR", "ABNB", "ORLY", "ASML", "NXPI", "CTAS", "MNST", "MRVL", "ODFL", "FTNT", "WDAY", "ADSK", "LULU", "PCAR", "MCHP", "CPRT", "PAYX", "CRWD", "ON", "KDP", "SGEN", "EXC", 
"KHC", "AZN", "MRNA", "AEP", "ROST", "BIIB", "TTD", "IDXX", "CEG", "VRSK", "BKR", "EA", "CTSH", "CSGP", "XEL", "FAST", "GFS", "GEHC", "DXCM", "TEAM", "FANG", "DDOG", "WBD",
"ANSS", "ZS", "DLTR", "EBAY", "ILMN", "ALGN", "WBA", "SIRI", "ENPH", "ZM", "JD", "LCID"]


def stock_to_excel():
    output_folder = r"Your File path here"
    ##Exports the DataFrame to Excel
    output_file = os.path.join(output_folder, 'stock_info.xlsx')
    stock_data.to_excel(output_file)
    stock_data = get_stock_data(top_tickers)
    
"""if __name__ == "__main__":


    #stock_to_excel()

    #print(stock_data)"""