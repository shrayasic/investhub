from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk
from Flashcard import FlashcardApp  # Ensure Flashcard.py is in the same directory or adjust the import path accordingly

def create_rounded_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    points = [x1 + radius, y1,
              x1 + radius, y1,
              x2 - radius, y1,
              x2 - radius, y1,
              x2, y1,
              x2, y1 + radius,
              x2, y1 + radius,
              x2, y2 - radius,
              x2, y2 - radius,
              x2, y2,
              x2 - radius, y2,
              x2 - radius, y2,
              x1 + radius, y2,
              x1 + radius, y2,
              x1, y2,
              x1, y2 - radius,
              x1, y2 - radius,
              x1, y1 + radius,
              x1, y1 + radius,
              x1, y1]

    return canvas.create_polygon(points, **kwargs, smooth=True)

def show_analyze():
    import AnalyzePage

def show_chart():
    import ChartPage

def show_compare():
    import ComparePage

def show_learn():
    import LearnPage

def show_news():
    import NewsPage

def show_games():
    # import Flashcard
    game_window = Toplevel(root)
    game_window.geometry("800x600")
    app = FlashcardApp(game_window)  # Pass the new window as the parent to FlashcardApp

def show_notes():
    import Notes

def show_notif():
    import Notifications

root = Tk()
root.geometry("1550x1000")
root.title("Dashboard")
root.configure(background="#141A2A")

# Header
f2 = Frame(root, background="#001F3F", relief=SUNKEN)
f2.grid(row=0, column=0, columnspan=5, sticky="ew")
l1 = Label(f2, text="Dashboard", background="#001F3F", foreground="white", font=("Helvetica", 15, "bold"))
l1.pack(side=LEFT)
icon1 = PhotoImage(file="account1.png")
resize_icon1 = icon1.subsample(10, 10)
l2 = Label(f2, image=resize_icon1, background="#001F3F")
l2.pack(side=RIGHT)

# Load and resize image
image = Image.open("dashb1.png")
image = image.resize((1920, 1000))
photo = ImageTk.PhotoImage(image)

# Create label to display image
image_label = Label(root, image=photo, background="#141A2A")
image_label.image = photo  # Keep reference to prevent image from being garbage collected
image_label.place(x=00, y=50)  # Adjust coordinates as needed

# Canvas
canvas_width = 1000
canvas_height = 500
corner_radius = 60
bg_color = '#05192E'
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg=bg_color, highlightbackground=bg_color, highlightthickness=0)
canvas.place(relx=0.5, rely=0.5, anchor=CENTER)

# Draw rounded rectangle canvas
fill_color = '#4A4CBC'
create_rounded_rectangle(canvas, 0, 0, canvas_width, canvas_height, corner_radius, fill=fill_color, outline='white', width=5)

# Add buttons
button_size = 150
button_spacing = 150
button_positions = [
    (130, 150),
    (130, 350),
    (380, 150),
    (380, 350),
    (630, 150),
    (630, 350),
    (880, 150),
    (880, 350)
]

buttons_info = [
    ("Analyze", show_analyze),
    ("Charts", show_chart),
    ("Compare", show_compare),
    ("Learn", show_learn),
    ("News", show_news),
    ("Games", show_games),
    ("Notes", show_notes),
    ("Notifications", show_notif)
]

for i, (x, y) in enumerate(button_positions):
    button_text, command = buttons_info[i]
    button = Button(root, text=button_text, command=command, background="#141A2A", foreground= "white" , font=("squada one", 15, "bold"))
    canvas.create_window(x, y, window=button, width=button_size, height=button_size)

root.mainloop()
