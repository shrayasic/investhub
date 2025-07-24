from customtkinter import *
from tkinter import *
from PIL import Image
import mysql.connector
from conn import db, cursor

root = CTk()
root.geometry("1550x1000")
root.title("Login Page")
root.minsize(200,100)
root.resizable(0,0)

# Variables
name_var = StringVar()
pass_var = StringVar()

side_img_data = Image.open("modlog.png")
email_icon_data = Image.open("usicon.png")
password_icon_data = Image.open("password-icon.png")

side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(775, 1000))
email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20,20))
password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17,17))

CTkLabel(master=root, text="", image=side_img).pack(expand=True, side="left")

frame = CTkFrame(master=root, width=775, height=1000, fg_color="#ffffff")
frame.pack_propagate(0)
frame.pack(expand=True, side="right")

CTkLabel(master=frame, text="Welcome Back!", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 35)).pack(anchor="n", pady=(100, 5), padx=(25, 0))
CTkLabel(master=frame, text="Login to your account", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 17)).pack(anchor="n", padx=(25, 0))

CTkLabel(master=frame, text="  Username:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 20), image=email_icon, compound="left").pack(anchor="n", pady=(38, 0), padx=(25, 0))
CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", textvariable=name_var).pack(anchor="n", padx=(50, 0))

CTkLabel(master=frame, text="  Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 20), image=password_icon, compound="left").pack(anchor="n", pady=(21, 0), padx=(25, 0))
CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*", textvariable=pass_var).pack(anchor="n", padx=(50, 0))

# Form Submit function
def submit():
    name = name_var.get()
    password = pass_var.get()
    if check_cred(name, password):
        print("Login successful")
        name_var.set("")
        pass_var.set("")
        #  Show register page function
        root.destroy()
        import Dashboard
    else:
        print("Invalid credentials")
        # Error Frame
        f2 = CTkFrame(root, width=200, height=100, fg_color="#001F3F")
        f2.place(anchor=CENTER, relx=0.5, rely=0.5)
        error_label = CTkLabel(f2, text="Invalid credentials", padx="20", pady="20", fg_color="#ffffff", font=("Helvetica", 12, "bold"))
        error_label.pack()
        b1 = CTkButton(f2, text="Close", command=lambda: f2.destroy(), fg_color="red")
        b1.pack(padx="20", pady="20")

CTkButton(master=frame, text="Login", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225, command=submit).pack(anchor="n", pady=(40, 0), padx=(50, 0))

def check_cred(username, password):
    try:
        query = "SELECT * FROM userinfo WHERE username = %s AND userpassword = %s"
        values = (username, password)
        cursor.execute(query, values)
        result = cursor.fetchone()
        return result is not None
    except mysql.connector.Error as err:
        print(f"Error {err}")
        return False

root.mainloop()
