import tkinter as tk
from tkinter import messagebox

def submit():
    name = entry_name.get()
    email = entry_email.get()
    gender = var_gender.get()
    phone = entry_phone.get()
    language = var_language.get()

    if not name or not email or not gender or not phone or not language:
        messagebox.showerror("Error", "Please fill in all details correctly.")
    else:
        messagebox.showinfo("Success", "Thank you for registering!")

root = tk.Tk()
root.title("STUDENT REGISTRATION FORM")

label_name = tk.Label(root, text="NAME:")
label_name.grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

label_email = tk.Label(root, text="EMAIL:")
label_email.grid(row=1, column=0, sticky="w")
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1)

label_gender = tk.Label(root, text="GENDER:")
label_gender.grid(row=2, column=0, sticky="w")
var_gender = tk.StringVar(root)
var_gender.set("FEMALE")
gender_options = ["MALE", "FEMALE", "OTHER"]
gender_menu = tk.OptionMenu(root, var_gender, *gender_options)
gender_menu.grid(row=2, column=1)

label_phone = tk.Label(root, text="PHONE:")
label_phone.grid(row=3, column=0, sticky="w")
entry_phone = tk.Entry(root)
entry_phone.grid(row=3, column=1)

label_language = tk.Label(root, text="LANGUAGE:")
label_language.grid(row=4, column=0, sticky="w")
var_language = tk.StringVar(root)
var_language.set("PYTHON")
language_options = ["PYTHON", "C++"]
language_menu = tk.OptionMenu(root, var_language, *language_options)
language_menu.grid(row=4, column=1)

submit_button = tk.Button(root, text="SUBMIT", command=submit, bg="green")
submit_button.grid(row=5, columnspan=2, pady=10)

root.mainloop()
