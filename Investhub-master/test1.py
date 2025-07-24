from tkinter import *
import yfinance as yf

def fetch_data():
    symbol = entry_symbol.get()
    df = fetch_stock_data(symbol)
    if df is not None:  # Check if data is fetched successfully
        show_earnings_calendar()  # Call show_earnings_calendar if data is fetched

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


def show_earnings_calendar():
    symbol = entry_symbol.get()
    earnings_data = fetch_earnings_calendar(symbol)
    if earnings_data:
        display_earnings_calendar(earnings_data)

def fetch_earnings_calendar(symbol):
    try:
        stock = yf.Ticker(symbol)
        earnings_df = stock.calendar
        return earnings_df
    except Exception as e:
        print(f"Error fetching earnings calendar: {e}")
        return None

def display_earnings_calendar(earnings_data):
    earnings_window = Toplevel(root)
    earnings_window.title("Earnings Calendar")
    earnings_window.geometry("400x200")

    earnings_date = earnings_data['Earnings Date'][0]
    text_widget = Text(earnings_window, wrap="word", font=("Helvetica", 12))
    text_widget.pack(expand=YES, fill=BOTH)
    text_widget.insert(INSERT, f"Earnings Date: {earnings_date}")

root = Tk()
root.title("Analyze Stock")
root.geometry("800x600")

label_symbol = Label(root, text="Enter Stock Symbol:")
entry_symbol = Entry(root)
button_fetch_data = Button(root, text="Fetch Data", command=fetch_data)

label_symbol.pack(pady=10)
entry_symbol.pack(pady=10)
button_fetch_data.pack(pady=10)

root.mainloop()
