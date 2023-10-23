"""
Authors: BW, EL, CC, JP

Purpose: Main entry point of application.
"""

import customtkinter as tk

# Create a window
window = tk.CTk()
window.geometry("1280x720")

# Set the window title
window.title("Stock++")

# Create a frame to hold the label and buttons
label_frame = tk.CTkFrame(window)
label_frame.pack(side="top", fill="x")

# Create a label widget
custom_font = ("Lato", 24)
label = tk.CTkLabel(label_frame, text="Stock List", font=custom_font)
label.pack(side="left", padx=10, pady=10)

# Create a frame to hold the buttons
button_frame = tk.CTkFrame(label_frame)
button_frame.pack(side="left")


# Update Market Capitalization Button Text
# CURRENT BUG: Text will not reset when alternating buttons since the []_text variable is saved
def change_text_mcap():
    global mcap_text
    if mcap_text == "Market Capitalization":
        mcap_text = "Market Capitalization ↑"
    elif mcap_text == "Market Capitalization ↑":
        mcap_text = "Market Capitalization ↓"
    elif mcap_text == "Market Capitalization ↓":
        mcap_text = "Market Capitalization"
    market_cap_button.configure(text=mcap_text)
    pe_ratio_button.configure(text="Price to Earnings")


# Market Capitalization Button
mcap_text = "Market Capitalization"
market_cap_button = tk.CTkButton(button_frame, text=mcap_text, command=change_text_mcap)
market_cap_button.pack(side="left", padx=10, pady=10)


# Update Price to Earnings Button Text
def change_text_pe():
    global pe_text
    if pe_text == "Price to Earnings":
        pe_text = "Price to Earnings ↑"
    elif pe_text == "Price to Earnings ↑":
        pe_text = "Price to Earnings ↓"
    elif pe_text == "Price to Earnings ↓":
        pe_text = "Price to Earnings"
    pe_ratio_button.configure(text=pe_text)
    market_cap_button.configure(text="Market Capitalization")


# Price to Earnings
pe_text = "Price to Earnings"
pe_ratio_button = tk.CTkButton(button_frame, text=pe_text, command=change_text_pe)
pe_ratio_button.pack(side="left", padx=10, pady=10)

# Refresh Button
refresh_button = tk.CTkButton(button_frame, text="Refresh")
refresh_button.pack(side="right", padx=10, pady=10)

# Create a frame for the stocks
main_frame = tk.CTkFrame(window)
main_frame.pack(side="top", fill="both", expand=True, padx=20, pady=20)

# Calculate the height for the stock frame
stock_frame_height = window.winfo_height() - label_frame.winfo_reqheight() - 40  # Subtract label frame height and add some padding
stock_frame_width = window.winfo_width() - 40  # Add some padding

# Create a frame for the stocks and set its dimensions
stock_frame = tk.CTkFrame(main_frame)
stock_frame.pack(pady=20, fill="both", expand=True)
stock_frame.configure(height=stock_frame_height, width=stock_frame_width)

# Start the GUI event loop
window.mainloop()
