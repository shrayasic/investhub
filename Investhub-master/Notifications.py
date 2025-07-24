from tkinter import *
import yfinance as yf
from plyer import notification
from PIL import Image, ImageTk
def fetch_data():
    symbol = selected_symbol.get()
    df = fetch_stock_data(symbol)
    if df is not None:
        show_earnings_notification(symbol)

def fetch_stock_data(symbol):
    try:
        start = '2010-01-01'
        end = '2023-12-31'
        df = yf.download(symbol, start=start, end=end)
        df = df.reset_index()
        df = df.drop(['Date', 'Adj Close'], axis=1)
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def show_earnings_notification(symbol):
    earnings_data = fetch_earnings_calendar(symbol)
    if earnings_data:
        earnings_date = earnings_data['Earnings Date'][0]
        notification_message = f"Earnings Date: {earnings_date}"
        notification.notify(
            title=symbol,
            message=notification_message,
            app_name="Analyze Stock"
        )
    else:
        notification.notify(
            title="Error",
            message="Failed to fetch earnings data.",
            app_name="Analyze Stock"
        )

def fetch_earnings_calendar(symbol):
    try:
        stock = yf.Ticker(symbol)
        earnings_df = stock.calendar
        return earnings_df
    except Exception as e:
        print(f"Error fetching earnings calendar: {e}")
        return None


# List of available stocks
available_stocks = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "ICICIBANK.NS", "INFY.NS", "LICI.NS", "SBIN.NS",
                    "BHARTIARTL.NS", "HINDUNILVR.NS", "ITC.NS", "LT.NS", "HCLTECH.NS", "KOTAKBANK.NS", "MARUTI.NS",
                    "AXISBANK.NS", "TATAMOTORS.NS", "ASIANPAINT.NS", "WIPRO.NS", "BAJFINANCE.NS", "DMART.NS",
                    "NESTLEIND.NS", "IRCTC.NS", "FINEORG.NS", "LTIM.NS"]

root = Tk()
root.title("Notifications")
root.geometry("800x600")
root.configure(background="#141A2A")



label_symbol = Label(root, text="Select Stock Symbol:", font=("Trebuchet MS", 12, "bold"))
label_symbol.pack(pady=10)



# Create a StringVar to hold the selected symbol
selected_symbol = StringVar(root)
selected_symbol.set(available_stocks[0])  # Set default value

# Create OptionMenu with dropdown
dropdown = OptionMenu(root, selected_symbol, *available_stocks)
dropdown.config(font=("Trebuchet MS", 10, "bold"), width=20, pady=4, background="#003872", foreground="white")
dropdown.pack(pady=10)

button_fetch_data = Button(root, text="Notify", command=fetch_data, font=("Trebuchet MS", 10, "bold"), width=15, pady=4, background="black", foreground="white")
button_fetch_data.pack(pady=10)

root.mainloop()
