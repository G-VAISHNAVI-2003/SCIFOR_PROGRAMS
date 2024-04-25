import tkinter as tk
from tkinter import messagebox

def form():
    name = e_name.get()
    age = e_age.get()
    gender = var_gender.get()
    address = e_address.get()
    email = e_email.get()
    contact = e_contact.get()
    country = e_country.get()
    state = e_state.get()

    # Use a dictionary to store diseases
    diseases = {
        "Cold": cold.get(),
        "Cough": cough.get(),
        "Fever": fever.get(),
        "Headache": headache.get()
    }
    
    if not name or not age or not gender or not address or not email or not contact or not country or not state:
        messagebox.showerror("Error", "Fill all details")
    else:
        messagebox.showinfo("Success", "Thanks for filling")

root = tk.Tk()
root.title("COVID VACCINE REGISTRATION FORM")

# Name
l_name = tk.Label(root, text="Name:")
l_name.grid(row=0, column=0, sticky="w")
e_name = tk.Entry(root)
e_name.grid(row=0, column=1)

# Age
l_age = tk.Label(root, text="Age:")
l_age.grid(row=1, column=0, sticky="w")
e_age = tk.Entry(root)
e_age.grid(row=1, column=1)

# Gender
l_gender = tk.Label(root, text="Gender:")
l_gender.grid(row=2, column=0, sticky="w")
var_gender = tk.StringVar(root)
options = ["Male", "Female", "Others"]

# Create radio buttons for each option using i and j
for i in range(len(options)):
    j = options[i]
    tk.Radiobutton(root, text=j, variable=var_gender, value=j).grid(row=2, column=i+1, sticky="w")

# Email
l_email = tk.Label(root, text="Email:")
l_email.grid(row=3, column=0, sticky="w")
e_email = tk.Entry(root)
e_email.grid(row=3, column=1)

# Address
l_address = tk.Label(root, text="Address:")
l_address.grid(row=4, column=0, sticky="w")
e_address = tk.Entry(root)
e_address.grid(row=4, column=1)

# Contact Number
l_contact = tk.Label(root, text="Contact Number:")
l_contact.grid(row=5, column=0, sticky="w")
e_contact = tk.Entry(root)
e_contact.grid(row=5, column=1)

# Country
l_country = tk.Label(root, text="Country:")
l_country.grid(row=6, column=0, sticky="w")
e_country = tk.Entry(root)
e_country.grid(row=6, column=1)

# State
l_state = tk.Label(root, text="State:")
l_state.grid(row=7, column=0, sticky="w")
e_state = tk.Entry(root)
e_state.grid(row=7, column=1)

# Disease Selection
l_disease = tk.Label(root, text="Select If you are having any of the following diseases:")
l_disease.grid(row=8, column=0, sticky="w")
cold = tk.BooleanVar()
cough = tk.BooleanVar()
fever = tk.BooleanVar()
headache = tk.BooleanVar()
tk.Checkbutton(root, text="Cold", variable=cold).grid(row=9, column=0, sticky="w")
tk.Checkbutton(root, text="Cough", variable=cough).grid(row=9, column=1, sticky="w")
tk.Checkbutton(root, text="Fever", variable=fever).grid(row=9, column=2, sticky="w")
tk.Checkbutton(root, text="Headache", variable=headache).grid(row=9, column=3, sticky="w")

# Submit Button
submit_button = tk.Button(root, text="Submit", command=form, bg="green")
submit_button.grid(row=10, columnspan=2, pady=10)

root.mainloop()
