import tkinter as tk
import math
from tkinter import ttk

def cal():
    p = pr.get()
    t = ti.get() / 100
    r = ra.get()

    if interest.get() == "SI":
        si.set(p * t * r)
        ci.set(0)
    else:
        ci.set(p * (math.pow((1 + r), t) - 1))
        si.set(0)
    
root = tk.Tk()
root.title("Calculator")
pr =ttk.Scale(root,from_=1000,to=50000,length=200,orient="horizontal")
pr.grid(row=0,column=0,padx=10,pady=5)
pr_label = ttk.Label(root, text="PRINCIPAL:")
pr_label.grid(row=0, column=1, padx=10, pady=5)

ti =ttk.Scale(root,from_=1,to=15,length=200,orient="horizontal")
ti.grid(row=1,column=0,padx=10,pady=5)
ti_label = ttk.Label(root, text="TIME (years):")
ti_label.grid(row=1, column=1, padx=10, pady=5)

ra =ttk.Scale(root,from_=1,to=50,length=200,orient="horizontal")
ra.grid(row=2,column=0,padx=10,pady=5)
ra_label = ttk.Label(root, text="RATE (%):")
ra_label.grid(row=2, column=1, padx=10, pady=5)

interest = tk.StringVar()
interest.set("SI")

si_radio = ttk.Radiobutton(root,text="SIMPLE INTEREST",variable=interest,value="SI")
si_radio.grid(row=3,column=0,padx=10,pady=5)

ci_radio = ttk.Radiobutton(root,text="COMPOUND INTEREST",variable=interest,value="CI")
ci_radio.grid(row=4,column=0,padx=10,pady=5)

calculate_button = ttk.Button(root, text="CALCULATE", command=cal)
calculate_button.grid(row=5, column=0, padx=10, pady=10)

si = tk.DoubleVar()
si_label = ttk.Label(root, text="SI-SIMPLE INTEREST:")
si_label.grid(row=6, column=0, padx=10, pady=5)
si_entry = ttk.Entry(root, textvariable=si, state="readonly")
si_entry.grid(row=6, column=1, padx=10, pady=5)

ci = tk.DoubleVar()
ci_label = ttk.Label(root, text="CI-COMPOUND INTEREST:")
ci_label.grid(row=7, column=0, padx=10, pady=5)
ci_entry = ttk.Entry(root, textvariable=ci, state="readonly")
ci_entry.grid(row=7, column=1, padx=10, pady=5)

root.mainloop()
