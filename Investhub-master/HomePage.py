from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Stock Market Analysis")
root.geometry("1550x1000")
root.minsize(200, 100)
root.configure(background="#001F3F")


#  Show login page function
def show_login_page():
    root.destroy()
    import LoginPage


#  Show register page function
def show_register_page():
    root.destroy()
    import RegisterPage

# Load and resize image
image = Image.open("homep2.png")
image = image.resize((1550, 800))
photo = ImageTk.PhotoImage(image)

# Create label to display image
image_label = Label(root, image=photo, background="#141A2A")
image_label.image = photo  # Keep reference to prevent image from being garbage collected
image_label.place(x=00, y=00)  # Adjust coordinates as needed

# Frame
f1 = Frame(root, background="#4A4CBC", relief=SUNKEN)
f1.place(anchor=CENTER, relx=0.5, rely=0.5)



# Login Photo
photo = PhotoImage(file="pfp.png")
resize_login_photo = photo.subsample(10,10)
login_photo = Label(f1, image=resize_login_photo, background="#4A4CBC")
login_photo.pack()

# Login label
login_label = Label(f1, text="Welcome! Please Login or Register", background="#4A4CBC", foreground="white", font=("Helvetica", 10, "italic"))
login_label.pack()

# Button Frame
button_frame = Frame(f1, background="#003872")
button_frame.pack()

# login button
button1 = Button(button_frame, width=14, command=show_login_page, text="Login", background="#141A2A", foreground="white", pady=10, font=("Helvetica", 12, "bold"))
button1.pack(side=LEFT)
# register button
button1 = Button(button_frame, width=15, command=show_register_page, text="Register", background="#141A2A", foreground="white", pady=10, font=("Helvetica", 12, "bold"))
button1.pack(side=LEFT)
# close button
button = Button(f1, width=30, text="Exit", command=root.destroy, background="black", foreground="white", pady=10, font=("Helvetica", 12, "bold"))
button.pack()
root.mainloop()