import tkinter as tk
# import ttkbootstrap as ttk
from tkinter import ttk


def dprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)


def button_function(valeur):
    def fonction():
        dprint(valeur.get())
    return fonction


# window 
window = tk.Tk()
window.title("Tkinter Buttons, functions and arguments")
window.geometry("400x300")

entree_string = tk.StringVar(value="test")
entree = ttk.Entry(
    master=window,
    textvariable=entree_string)
entree.pack(pady=10)

# ttk Buttons
button1 = ttk.Button(
    master=window, 
    text="Button", 
    command=button_function(entree_string))
button1.pack(pady=10)


# Run
window.mainloop()
