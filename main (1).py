"""
Authors: BW, EL, CC, JP
GUI: CC

Purpose: Main entry point of application.
"""

import customtkinter as tk
from datetime import datetime, timedelta
import pandas as pd
import api
from api import get_stock_data, top_tickers
from filters import *


# Create a window
window = tk.CTk()
window.geometry("1280x720")
window.title("Stock++")

# Create a frame to hold the label and buttons
label_frame = tk.CTkFrame(window)
label_frame.pack(side="top", fill="x")

# Create a label widget
custom_font = ("Lato", 24)
label = tk.CTkLabel(label_frame, text="Stock List 📈", font=custom_font)
label.pack(side="left", padx=10, pady=10)

# Create a frame to hold the buttons
button_frame = tk.CTkFrame(label_frame)
button_frame.pack(side="left")


# Update Market Capitalization Button Text
def change_text_mcap():
    global mcap_text, pe_text, dc_text
    if mcap_text == "Market Capitalization":
        mcap_text = "Market Capitalization ↑"   
    elif mcap_text == "Market Capitalization ↑":
        mcap_text = "Market Capitalization ↓"
    elif mcap_text == "Market Capitalization ↓":
        mcap_text = "Market Capitalization"
    pe_text = "Moving Average"
    dc_text = "Daily % Change"
    pe_ratio_button.configure(text="Moving Average")
    dc_button.configure(text="Daily % Change")
    market_cap_button.configure(text=mcap_text)


# Update Moving Average Button Text
def change_text_pe():
    global pe_text, mcap_text, dc_text
    if pe_text == "Moving Average":
        pe_text = "Moving Average ↑"
    elif pe_text == "Moving Average ↑":
        pe_text = "Moving Average ↓"
    elif pe_text == "Moving Average ↓":
        pe_text = "Moving Average"
    mcap_text = "Market Capitalization"
    dc_text = "Daily % Change"
    market_cap_button.configure(text="Market Capitalization")
    dc_button.configure(text="Daily % Change")
    pe_ratio_button.configure(text=pe_text)


# Update Daily Percentage Change Button
def change_text_dc():
    global pe_text, mcap_text, dc_text
    if dc_text == "Daily % Change":
        dc_text = "Daily % Change ↑"
    elif dc_text == "Daily % Change ↑":
        dc_text = "Daily % Change ↓"
    elif dc_text == "Daily % Change ↓":
        dc_text = "Daily % Change"
    mcap_text = "Market Capitalization"
    pe_text = "Moving Average"
    market_cap_button.configure(text="Market Capitalization")
    pe_ratio_button.configure(text="Moving Average")
    dc_button.configure(text=dc_text)


# Market Capitalization Button
mcap_text = "Market Capitalization"
market_cap_button = tk.CTkButton(button_frame, text=mcap_text, command=change_text_mcap)
market_cap_button.pack(side="left", padx=10, pady=10)


#  Moving Average Button
pe_text = "Moving Average"
pe_ratio_button = tk.CTkButton(button_frame, text=pe_text, command=change_text_pe)
pe_ratio_button.pack(side="left", padx=10, pady=10)


# Daily Percentage Change Button
dc_text = "Daily % Change"
dc_button = tk.CTkButton(button_frame, text=dc_text, command=change_text_dc)
dc_button.pack(side="left", padx=10, pady=10)


# Create a frame for the stocks
main_frame = tk.CTkFrame(window)
main_frame.pack(side="top", fill="both", expand=True, padx=20, pady=20)

# Calculate the height for the stock frame
stock_frame_height = window.winfo_height() - label_frame.winfo_reqheight() - 40  # Subtract label frame height
stock_frame_width = window.winfo_width() - 40  # Add some padding

# Create a frame for the stocks and set its dimensions
stock_frame_height = window.winfo_height() - label_frame.winfo_reqheight() - 40  # Subtract label frame height
stock_frame_width = window.winfo_width() - 40  # Add some padding

# Create a frame for the stocks and set its dimensions
stock_frame = tk.CTkScrollableFrame(main_frame)
stock_frame.pack(pady=20, fill="both", expand=True)
stock_frame.configure(height=stock_frame_height, width=stock_frame_width)

def update_stock_frame():
    # Fetch stock data using the current start_date without explicitly defining top_tickers
    stock_data = get_stock_data(top_tickers)

    # Fetch Market Capitalization and Moving Average data
    market_caps = [market_capitalization(symbol) for symbol in top_tickers]
    moving_avgs = [moving_average(symbol) for symbol in top_tickers]

    # Clear the existing content of the scrollable frame
    for widget in stock_frame.winfo_children():
        widget.destroy()

    # Print the stock data in a similar format as api.py
    formatted_data = stock_data.stack(level=0).reset_index()

    # Create labels for column titles
    title_text = "Ticker Symbol  |       Close    |        Volume  |  Market Cap  |  Moving Avg   " 
    title_label = tk.CTkLabel(stock_frame, text=title_text, font=("Lato", 14, "bold"))
    title_label.pack()

    # Create labels for each row in the stock data and pack them into the scrollable frame
    for i, (_, row) in enumerate(formatted_data.iterrows()):
        # Add Market Cap , Moving Avg values and Dividend yields 
        market_cap = market_caps[i] if i < len(market_caps) else ""
        moving_avg = moving_avgs[i] if i < len(moving_avgs) else ""


        row_text = f"{row['Ticker Symbol']} |  {row['Close']} |   {row['Volume']} |  {market_cap} |  {moving_avg} "
        label = tk.CTkLabel(stock_frame, text=row_text)
        label.pack()

update_stock_frame()

# Refresh Button
refresh_button = tk.CTkButton(button_frame, text="Refresh", command=update_stock_frame)
refresh_button.pack(side="right", padx=10, pady=10)

# Start the GUI event loop
window.mainloop()
