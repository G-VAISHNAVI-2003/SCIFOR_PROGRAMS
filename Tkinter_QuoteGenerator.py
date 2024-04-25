import tkinter as tk
import requests

window = tk.Tk()
window.title("QUOTE GENERATOR")

label = tk.Label(window,text="",wraplength=500)
label.pack()

def fetch_quote():
    url = "https://api.quotable.io/random"
    res = requests.get(url)
    Json = res.json()
    quote = Json['content']  
    author = Json['author']
    label.config(text=f"{quote} \n\n {author}")


button = tk.Button(window,text="click",bg="green",command=fetch_quote)
nd = fetch_quote()
button.pack()

window.mainloop()