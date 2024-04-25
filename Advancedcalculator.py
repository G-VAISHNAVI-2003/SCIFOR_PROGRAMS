import tkinter as tk

def clk(char):
    curr = disp.get()
    disp.delete(0, tk.END)
    disp.insert(tk.END, curr + char)

def clr():
    disp.delete(0, tk.END)

def calc():
    expression = disp.get()
    if expression:
        result = eval(expression)
        disp.delete(0, tk.END)
        disp.insert(tk.END, str(result))
    else:
        disp.delete(0, tk.END)
        disp.insert(tk.END, "Error: Empty Expression")

root = tk.Tk()
root.title("Calculator")

disp = tk.Entry(root, width=35, borderwidth=5)
disp.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2),
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3),
    ('/', 4, 3), ('C', 5, 0), ('AC', 5, 1)
]

for (txt, r, c) in buttons:
    if txt == '=':
        btn = tk.Button(root, text=txt, padx=40, pady=20, bg='lightblue', fg='black', command=calc)
    elif txt == 'C':
        btn = tk.Button(root, text=txt, padx=40, pady=20, bg='orange', fg='black', command=clr)
    elif txt == 'AC':
        btn = tk.Button(root, text=txt, padx=40, pady=20, bg='red', fg='white', command=lambda: disp.delete(0, tk.END))
    else:
        btn = tk.Button(root, text=txt, padx=40, pady=20, bg='lightgrey', fg='black', command=lambda t=txt: clk(t))
    btn.grid(row=r, column=c)

root.mainloop()
