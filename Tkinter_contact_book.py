import tkinter as tk
from tkinter import messagebox

def get_con():
    select_name = e_name.get()
    select_num = e_num.get()
    select_addr = e_addr.get()
    messagebox.showinfo("Selected contact details", f"Name: {select_name}\nNumber: {select_num}\nAddress: {select_addr}")

def add_con():
    name = e_name.get()
    num =  e_num.get()
    addr = e_addr.get()
    messagebox.showinfo("Added contact", f"Name: {name}\nNumber: {num}\nAddress: {addr}")

def edit_con():
    messagebox.showinfo("Edit contact", "Click here to edit")

def view_con():
    messagebox.showinfo("View contacts", "Displaying contacts")

def reset():
    e_name.delete(0, tk.END)
    e_num.delete(0, tk.END)
    e_addr.delete(0, tk.END)

root = tk.Tk()
root.title("MAGGIE'S CONTACT BOOK!")

# Set the window size to be square
window_size = 350
root.geometry(f"{window_size}x{window_size}")

n_label = tk.Label(root, text="NAME:")
n_label.grid(row=0, column=0, sticky='w')
e_name = tk.Entry(root)
e_name.grid(row=0, column=1)

nu_label = tk.Label(root, text="NUMBER:")
nu_label.grid(row=1, column=0, sticky='w')
e_num = tk.Entry(root)
e_num.grid(row=1, column=1)

addr_label = tk.Label(root, text="ADDRESS:")
addr_label.grid(row=2, column=0, sticky='w')
e_addr = tk.Entry(root)
e_addr.grid(row=2, column=1)

get_button = tk.Button(root, text="Show selected contact", command=get_con, bg="Green")
get_button.grid(row=3, column=0, columnspan=2, pady=5)

add_button = tk.Button(root, text="Add contact", command=add_con, bg="Green")
add_button.grid(row=4, column=0, columnspan=2, pady=5)

edit_button = tk.Button(root, text="Edit contact", command=edit_con, bg="Green")
edit_button.grid(row=5, column=0, columnspan=2, pady=5)

view_button = tk.Button(root, text="View contacts", command=view_con, bg="Green")
view_button.grid(row=6, column=0, columnspan=2, pady=5)

reset_button = tk.Button(root, text="Reset button", command=reset, bg="Red")
reset_button.grid(row=7, column=0, columnspan=2, pady=5)

root.mainloop()
