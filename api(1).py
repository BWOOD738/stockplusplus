import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import os


top_tickers = ["AAPL", "MSFT", "AMZN", "NVDA", "META", "TSLA", "GOOGL", "GOOG", "AVGO", "COST", "ADBE", "PEP", "CSCO", "CMCSA", "AMD", "TMUS", "NFLX", "INTC", "AMGN", "INTU", 
"TXN", "HON", "QCOM", "AMAT", "BKNG", "SBUX", "ADP", "ISRG", "GILD", "VRTX", "REGN", "ADI", "MDLZ", "LRCX", "PANW", "MU", "SNPS", "PDD", "CDNS", "CHTR", "KLAC", "PYPL", "CSX", 
"MELI", "MAR", "ABNB", "ORLY", "ASML", "NXPI", "CTAS", "MNST", "MRVL", "ODFL", "FTNT", "WDAY", "ADSK", "LULU", "PCAR", "MCHP", "CPRT", "PAYX", "CRWD", "ON", "KDP", "SGEN", "EXC", 
"KHC", "AZN", "MRNA", "AEP", "ROST", "BIIB", "TTD", "IDXX", "CEG", "VRSK", "BKR", "EA", "CTSH", "CSGP", "XEL", "FAST", "GFS", "GEHC", "DXCM", "TEAM", "FANG", "DDOG", "WBD",
"ANSS", "ZS", "DLTR", "EBAY", "ILMN", "ALGN", "WBA", "SIRI", "ENPH", "ZM", "JD", "LCID"]

# Function to get the current date and time adjusted for the stock market opening hours
def get_start_date():
    now = datetime.now()
    
    # Check if the stock market is open (assuming it opens at 9:00 AM)
    if now.hour < 9:
        # If before 9:00 AM, use yesterday's date
        return now - timedelta(days=1)
    else:
        # If after 9:00 AM, use today's date
        return now 


## To set the display options to show all rows and columns uncomment
#pd.set_option("display.max_rows", None)  # Display all rows
#pd.set_option("display.max_columns", None)  # Display all columns
start_date = get_start_date()
end_date = get_start_date()
def get_stock_data(top_tickers,start_date=None, end_date=None):
   
    if end_date is None:
        end_date = get_start_date()
    if start_date is None:
       start_date = get_start_date()

    data_frames = []
    

    for symbol in top_tickers:
        stocks = yf.download(symbol,start = start_date, end=end_date)
        data_frames.append(stocks[["Close", "Volume"]])

    stock_data = pd.concat(data_frames, axis=1)
    stock_data.columns = pd.MultiIndex.from_product([top_tickers, ["Close","Volume"]],names=["Ticker Symbol", "Attributes"])

    return stock_data



def stock_to_excel(stock_data, output_folder):
    output_folder = r"Your File path here"
    ##Exports the DataFrame to Excel
    output_file = os.path.join(output_folder, 'stock_info.xlsx')
    stock_data.to_excel(output_file)

if __name__ == "__main__":
    start_date = get_start_date()

    # Fetch stock data using the current start_date without explicitly defining top_tickers
    stock_data = get_stock_data(start_date)

    #stock_to_excel()
    print(stock_data.stack(level=0).reset_index())
   