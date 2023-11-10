import tkinter as tk
# import ttkbootstrap as ttk
from tkinter import ttk


def dprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)


def button_function():
    window.quit()


# window = tk.Tk()
window = tk.Tk()
window.title("Window & Widgets")
window.geometry("800x300")

# ttk.Label
title_label = tk.Label(master=window, text="Une ligne de texte en Label")
title_label.pack()

# tk.Text
texte = tk.Text(master=window, height=10)
texte.tk_focusFollowsMouse()
texte.pack()

# ttk.Entry
entree = ttk.Entry(master=window, background="lightblue")
entree.pack(pady=10)

# ttk.Button
bouton = ttk.Button(master=window, text="Fermer", command=button_function)
bouton.pack(pady=5)

# Run
window.mainloop()
