from tkinter import *
from create_user import *
from run import *

window = Tk()


def scan(username_entry):
    username = username_entry.get()
    swift_lock(username)

def username_search(username_entry):
    username = username_entry.get()
    user_dir(username)
    #new LINE OF CODE
    new_userFolder(username)
    capture(username)


def scan_window():
    new_window = Toplevel(window)
    new_window.minsize(100, 100)
    new_window.config(padx=10, pady=10)
    username_label = Label(new_window, text="Username :", font=("Arial", 8))
    username_label.grid(column=0, row=0)
    username_entry = Entry(new_window, width=28)
    username_entry.focus()
    username_entry.grid(column=1, row=0)
    username = username_entry.get()
    username_entry.delete(0, END)
    enter_button = Button(new_window, text="Enter", font=("Arial", 8), command=lambda: scan(username_entry))
    enter_button.grid(column=3, row=0)


def profile_window():
    new_window = Toplevel(window)
    new_window.minsize(100, 100)
    new_window.config(padx=10, pady=10)
    username_label = Label(new_window, text="Username :", font=("Arial", 8))
    username_label.grid(column=0, row=0)
    username_entry = Entry(new_window, width=28)
    username_entry.focus()
    username_entry.grid(column=1, row=0)
    username = username_entry.get()
    username_entry.delete(0, END)
    enter_button = Button(new_window, text="Enter", font=("Arial", 8), command=lambda: username_search(username_entry))
    enter_button.grid(column=3, row=0)


window.title("Swift Unlock")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="Welcome To Swift Unlock", font=("Arial", 24, "bold"))
my_label.place(relx=0.15, rely=0.1)

#text
here_label= Label(text="Here you can create a new profile or unlock your device!", font=("Arial", 10, "italic"))
here_label.place(relx=0.15, rely=0.25)

# Button
create_profile = Button(text="Create Profile", font=("Arial", 10, "bold"), command=profile_window)
create_profile.place(relx=0.1, rely=0.5)
#
Face_ID = Button(text="Face ID", font=("Arial", 10, "bold"), command=scan_window)
Face_ID.place(relx=0.7, rely=0.5)
#
window.mainloop()
