from tkinter import *
import webbrowser

def openlink(url):
    webbrowser.open(url)

root = Tk()
root.title("Learn Stocks")
root.geometry("800x600")

# Canvas
canvas = Canvas(root)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Frame inside the Canvas
f1 = Frame(canvas, relief=SUNKEN)

# Scrollbar
v_scroll = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
v_scroll.pack(side=RIGHT, fill=Y)
canvas.configure(yscrollcommand=v_scroll.set)

# Add links to the frame
links = [
    {"url": "https://www.youtube.com/watch?v=RieqxXMds64&list=PLF--UWHQ0vo50RDyN3WYkIb1l92pG4BWS&index=1", "text": "Stock Market Basics"},
    {"url": "https://www.youtube.com/watch?v=K5k4kF_2j0M&list=PLF--UWHQ0vo50RDyN3WYkIb1l92pG4BWS&index=2", "text": "PB Ratio and Enterprise value"},
    {"url": "https://www.youtube.com/watch?v=OaHFyZtN0iM&list=PLF--UWHQ0vo50RDyN3WYkIb1l92pG4BWS&index=3", "text": "Dividend and Promoter Holding"},
    {"url": "https://www.youtube.com/watch?v=KR_U_X039_k&list=PLF--UWHQ0vo50RDyN3WYkIb1l92pG4BWS&index=4", "text": "Return of Equity"},
    {"url": "https://www.youtube.com/watch?v=924-bji0I6Y&list=PLF--UWHQ0vo50RDyN3WYkIb1l92pG4BWS&index=5", "text": "Basics of Fundamental Analysis"},
    {"url": "https://www.youtube.com/watch?v=_lQsquuVKqM&list=PLF--UWHQ0vo50RDyN3WYkIb1l92pG4BWS&index=6", "text": "Identify Bad Stocks"},
    {"url": "https://www.youtube.com/watch?v=I13xlJnrC38&list=PLF--UWHQ0vo50RDyN3WYkIb1l92pG4BWS&index=7", "text": "Analyze Banking Stocks"},
    {"url": "https://www.youtube.com/watch?v=KcAakKmTknM&list=PLF--UWHQ0vo50RDyN3WYkIb1l92pG4BWS&index=8", "text": "Read Annual Report"},
    {"url": "https://www.youtube.com/watch?v=Hcnf-IBcvRw&list=PLF--UWHQ0vo50RDyN3WYkIb1l92pG4BWS&index=9", "text": "Value Banking Stocks"},
    # Add more links here if needed
]

for i, link_data in enumerate(links):
    bullet = Label(f1, text=".", background="black", padx=18, pady=18, borderwidth=3, relief="ridge")
    bullet.grid(row=i, column=0)
    linkbutton = Button(f1, text=link_data["text"], command=lambda u=link_data["url"]: openlink(u), padx=10, pady=18, background="white", width=50, font=("Trebuchet MS", 14, "bold"))
    linkbutton.grid(row=i, column=1, padx=10, pady=10)

# Add the frame to the canvas
canvas.create_window((0, 0), window=f1, anchor='nw')

# Function to update canvas scroll region
def update_scroll_region(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

# Update scroll region when resizing
canvas.bind("<Configure>", update_scroll_region)

root.mainloop()
