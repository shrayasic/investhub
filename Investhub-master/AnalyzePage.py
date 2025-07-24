from tkinter import *
import yfinance as yf

def fetch_data():
    symbol = selected_symbol.get()
    stock_info = fetch_stock_info(symbol)
    if stock_info is not None:
        display_stock_info(stock_info)

def fetch_stock_info(symbol):
    try:
        stock = yf.Ticker(symbol)
        info = {
            "Name": stock.info.get('longName', 'N/A'),
            "Type": stock.info.get('quoteType', 'N/A'),
            "Current Price": stock.info.get('currentPrice', 'N/A'),
            "Industry": stock.info.get('industry', 'N/A'),
            "Market Cap": stock.info.get('marketCap', 'N/A'),
            "PE Ratio": stock.info.get('trailingPE', 'N/A'),
            "PB Ratio": stock.info.get('priceToBook', 'N/A'),
            "EBITDA": stock.info.get('ebitda', 'N/A'),
            "Total Debt": stock.info.get('totalDebt', 'N/A'),
            "Total Revenue": stock.info.get('totalRevenue', 'N/A'),
        }
        return info
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def display_stock_info(info):
    info_text.delete(1.0, END)
    for key, value in info.items():
        info_text.insert(END, f"{key}: {value}\n")

root = Tk()
root.title("Analyze Page")
root.geometry("900x700")

# List of available stocks
available_stocks = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "ICICIBANK.NS", "INFY.NS", "LICI.NS", "SBIN.NS",
                    "BHARTIARTL.NS", "HINDUNILVR.NS", "ITC.NS", "LT.NS", "HCLTECH.NS", "KOTAKBANK.NS", "MARUTI.NS",
                    "AXISBANK.NS", "TATAMOTORS.NS", "ASIANPAINT.NS", "WIPRO.NS", "BAJFINANCE.NS", "DMART.NS",
                    "NESTLEIND.NS", "IRCTC.NS", "FINEORG.NS", "LTIM.NS"]

# Create a StringVar to hold the selected symbol
selected_symbol = StringVar(root)
selected_symbol.set(available_stocks[0]) # Set default value

label_symbol = Label(root, text="Select Stock Symbol:", font=("Trebuchet MS", 12, "bold"))
label_symbol.pack(pady=10)

# Create OptionMenu with dropdown
dropdown = OptionMenu(root, selected_symbol, *available_stocks)
dropdown.config(font=("Trebuchet MS", 10, "bold"), width=15, pady=4, background="#003872", foreground="white")
dropdown.pack(pady=10)

b = Button(root, text="Fetch Data", command=fetch_data, font=("Trebuchet MS", 10, "bold"), width=15, pady=4, background="black", foreground="white")
b.pack(pady=10)

info_text = Text(root, font=("Trebuchet MS", 12))
info_text.pack(pady=30)

root.mainloop()