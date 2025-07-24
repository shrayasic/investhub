from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Notes")
root.geometry("900x700")

f1 = Frame(root)
f1.pack()

text_scroll = Scrollbar(f1)
text_scroll.pack(side=RIGHT, fill=Y)

my_text = Text(f1, width=100, height=29, font=("Comic Sans MS", 12), selectbackground="light blue", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

text_scroll.config(command=my_text.yview)

my_menu = Menu(root)
root.config(menu=my_menu)

global open_status_name
open_status_name = False
global selected
selected = False
def new_file():
    my_text.delete("1.0", END)
    root.title("New File")
    statusbar.config(text="New File")
    global open_status_name
    open_status_name = False

def open_file():
    my_text.delete("1.0", END)
    text_file = filedialog.askopenfilename(initialdir="C:/gui/", title="Open File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if text_file:
        global open_status_name
        open_status_name = text_file
        name = text_file
        statusbar.config(text=f'{name}')
        name = name.replace("C:/Users/User/Downloads/", "")
        root.title(f'{name}')
        # Open
        text_file = open(text_file, "r")
        stuff = text_file.read()
        my_text.insert(END, stuff)
        text_file.close()

def saveas_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".txt", initialdir="C:/gui/", title="Save File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if text_file:
        global open_status_name
        open_status_name = text_file
        name = text_file
        statusbar.config(text=f'{name}')
        name = name.replace("C:/Users/User/Downloads/", "")
        root.title(f'{name}')
        # save
        text_file = open(text_file, "w")
        text_file.write(my_text.get(1.0, END))
        text_file.close()

def save_file():
    global open_status_name
    if open_status_name:
        text_file = open(open_status_name, "w")
        text_file.write(my_text.get(1.0, END))
        text_file.close()
        statusbar.config(text=f'Saved : {open_status_name}')
    else:
        saveas_file()


# File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=saveas_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)


def cut_text(e):
    global selected
    if e:
        selected = my_text.selection_get()
    else:
        if my_text.selection_get():
            # Select Text
            selected = my_text.selection_get()
            # Cut Text
            my_text.delete("sel.first", "sel.last")
            root.clipboard_clear()
            root.clipboard_append(selected)


def copy_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if my_text.selection_get():
            # Select Text
            selected = my_text.selection_get()
            root.clipboard_clear()
            root.clipboard_append(selected)


def paste_text(e):
    global selected
    if e:
        selected = root.clipboard_get()
    else:
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)

# Edit Menu
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut      ctrl+x", command=lambda : cut_text(False))
edit_menu.add_command(label="Copy   ctrl+c", command=lambda : copy_text(False))
edit_menu.add_command(label="Paste   ctrl+v", command=lambda : paste_text(False))

statusbar = Label(root, text="Ready", anchor=E)
statusbar.pack(fill=X, side=BOTTOM, ipady=5)

# Edit Bindings
root.bind("<Control-Key-x>", cut_text)
root.bind("<Control-Key-c>", copy_text)
root.bind("<Control-Key-v>", paste_text)

root.mainloop()
