from customtkinter import *
from PIL import Image
import mysql.connector
from conn import db, cursor

root = CTk()
root.geometry("1550x1000")
root.title("Register Page")
root.minsize(200,100)
root.resizable(0,0)
root.configure(background="#001F3F")

# Variables
email_var = StringVar()
con_var = StringVar()
name_var = StringVar()
pass_var = StringVar()
age_var = IntVar()

# Form Submit function
def submit():
    email = email_var.get()
    contact = con_var.get()
    name = name_var.get()
    password = pass_var.get()
    age = age_var.get()

    # Verify email
    if not email.endswith("@gmail.com"):
        # Error Frame
        f2 = CTkFrame(root, width=200, height=100, fg_color="#001F3F")
        f2.place(anchor=CENTER, relx=0.5, rely=0.5)
        error_label = CTkLabel(f2, text="Please enter valid Email ID", padx="20", pady="20", fg_color="#ffffff",
                            font=("Helvetica", 12, "bold"))
        error_label.pack()
        b1 = CTkButton(f2, text="Close", command=lambda: f2.destroy(), fg_color="red")
        b1.pack(padx="20", pady="20")
        print("Invalid Email")
        return

    # Verify contact
    if not contact.isdigit() or len(contact) != 10:
        # Error Frame
        f2 = CTkFrame(root, width=200, height=100, fg_color="#001F3F")
        f2.place(anchor=CENTER, relx=0.5, rely=0.5)
        error_label = CTkLabel(f2, text="Please enter valid contact", padx="20", pady="20", fg_color="#ffffff",
                            font=("Helvetica", 12, "bold"))
        error_label.pack()
        b1 = CTkButton(f2, text="Close", command=lambda: f2.destroy(), fg_color="red")
        b1.pack(padx="20", pady="20")
        print("Invalid contact")
        return

    if not name or not password or not age:
        # Error Frame
        f2 = CTkFrame(root, width=200, height=100, fg_color="#001F3F")
        f2.place(anchor=CENTER, relx=0.5, rely=0.5)
        error_label = CTkLabel(f2, text="All fields are required", padx="20", pady="20", fg_color="#ffffff",
                            font=("Helvetica", 12, "bold"))
        error_label.pack()
        b1 = CTkButton(f2, text="Close", command=lambda: f2.destroy(), fg_color="red")
        b1.pack(padx="20", pady="20")
        print("Incomplete details")
        return

    # Insert data into database
    query = "Insert into userinfo (useremail, usercontact, userage, username, userpassword) values(%s, %s, %s, %s, %s);"
    values = (email, contact, age, name, password)
    try:
        cursor.execute(query, values)
        db.commit()
        print("Registration successful")

        email_var.set("")
        con_var.set("")
        name_var.set("")
        pass_var.set("")
        age_var.set("")
        #  Show login page function
        root.destroy()
        import LoginPage

    except mysql.connector.Error as err:
        print(f"Error {err}")
        db.rollback()

        # Error Frame
        f2 = CTkFrame(root, width=200, height=100, fg_color="#001F3F")
        f2.place(anchor=CENTER, relx=0.5, rely=0.5)
        error_label = CTkLabel(f2, text="Registration unsuccessful", padx="20", pady="20", fg_color="#ffffff", font=("Helvetica", 12, "bold"))
        error_label.pack()
        b1 = CTkButton(f2, text="Close", command=lambda: f2.destroy(), fg_color="red")
        b1.pack(padx="20", pady="20")

# Login Photo
side_img_data = Image.open("modlog.png")
side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(775, 1000))
CTkLabel(master=root, text="", image=side_img).pack(expand=True, side="left")

# Frame
f1 = CTkFrame(master=root, width=775, height=1000, fg_color="#ffffff")
f1.pack_propagate(0)
f1.pack(expand=True, side="right")

# Welcome Label
CTkLabel(master=f1, text="Welcome to InvestHub", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))

# Email
CTkLabel(master=f1, text="Email:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14)).pack(anchor="w", pady=(38, 0), padx=(25, 0))
CTkEntry(master=f1, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", textvariable=email_var).pack(anchor="w", padx=(25, 0))

# Contact
CTkLabel(master=f1, text="Contact:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14)).pack(anchor="w", pady=(21, 0), padx=(25, 0))
CTkEntry(master=f1, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", textvariable=con_var).pack(anchor="w", padx=(25, 0))

# Age
CTkLabel(master=f1, text="Age:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14)).pack(anchor="w", pady=(21, 0), padx=(25, 0))
CTkEntry(master=f1, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", textvariable=age_var).pack(anchor="w", padx=(25, 0))

# Username
CTkLabel(master=f1, text="Username:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14)).pack(anchor="w", pady=(21, 0), padx=(25, 0))
CTkEntry(master=f1, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", textvariable=name_var).pack(anchor="w", padx=(25, 0))

# Password
CTkLabel(master=f1, text="Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14)).pack(anchor="w", pady=(21, 0), padx=(25, 0))
CTkEntry(master=f1, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*", textvariable=pass_var).pack(anchor="w", padx=(25, 0))

# Register button
CTkButton(master=f1, text="Register", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225, command=submit).pack(anchor="w", pady=(40, 0), padx=(25, 0))

root.mainloop()

