from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import yfinance as yf

def fetch_data(symbol):
    df = fetch_stock_data(symbol)
    if df is not None:
        plot_stock_data(df, ax, canvas)

def fetch_stock_data(symbol):
    try:
        start = '2010-01-01'
        end = '2023-12-31'
        df = yf.download(symbol, start=start, end=end)
        return df
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

def plot_stock_data(df, ax, canvas):
    ax.clear()
    ax.plot(df['Close'])
    ax.set_title("Stock Price Over Time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Closing Price")
    canvas.draw()

def show_chart(symbol):
    fetch_data(symbol)

root = Tk()
root.title("Stock List")
root.geometry("900x700")

figure = Figure(figsize=(5, 4))
ax = figure.add_subplot(1, 1, 1)
canvas = FigureCanvasTkAgg(figure, master=root)
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

indian_symbols = {
    "RELIANCE.NS": "Reliance Industries Limited",
    "TCS.NS": "Tata Consultancy Services Limited",
    "HDFCBANK.NS": "HDFC Bank Limited",
    "ICICIBANK.NS": "ICICI Bank Limited",
    "INFY.NS": "Infosys Limited",
    "LICI.NS": "Life Insurance Corporation of India",
    "SBIN.NS": "State Bank of India",
    "BHARTIARTL.NS": "Bharti Airtel Limited",
    "HINDUNILVR.NS": "Hindustan Unilever Limited ",
    "ITC.NS": "ITC Limited ",
    "LT.NS": "Larsen & Toubro Limited ",
    "HCLTECH.NS": "HCL Technologies Limited ",
    "KOTAKBANK.NS": "Kotak Mahindra Bank Limited",
    "MARUTI.NS": "Maruti Suzuki India Limited",
    "AXISBANK.NS": "Axis Bank Limited",
    "TATAMOTORS.NS": "Tata Motors Limited",
    "ASIANPAINT.NS": "Asian Paints Limited",
    "WIPRO.NS": "Wipro Limited",
    "BAJFINANCE.NS": "Bajaj Finance Limited",
    "DMART.NS": "Avenue Supermarts Limited",
    "NESTLEIND.NS": "Nestlé India Limited",
    "IRCTC.NS" : "Indian Railway Catering & Tourism Corporation Limited",
    "FINEORG.NS" : "Fine Organic Industries Limited ",
    "LTIM.NS": "LTIMindtree Limited "
}

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(root, yscrollcommand=scrollbar.set, font=("Trebuchet MS", 12))
for symbol, name in indian_symbols.items():
    listbox.insert(END, f"{symbol} - {name}")

listbox.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar.config(command=listbox.yview)

def on_select(evt):
    index = listbox.curselection()[0]
    symbol = list(indian_symbols.keys())[index]
    show_chart(symbol)

listbox.bind('<<ListboxSelect>>', on_select)

root.mainloop()
