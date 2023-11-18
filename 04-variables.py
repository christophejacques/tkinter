import tkinter as tk
# import ttkbootstrap as ttk
from tkinter import ttk


def dprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)


def button_function():
    window.quit()

def valider_bouton():
    label2["text"] = entree.get()


# window = tk.Tk()
window = tk.Tk()
window.title("Tkinter variables")
# window.geometry("400x300")

# ttk.Entry
chaine = tk.StringVar(value="debut")

# ttk.Label
zone1 = tk.Frame(master=window)
zone1.pack(anchor="w", side="top")

label1 = tk.Label(master=zone1, textvariable=chaine)
label1.pack()

label2 = tk.Label(master=zone1, textvariable=chaine)
label2.pack()


entree = ttk.Entry(master=window, textvariable=chaine )
entree.pack(pady=20)


# Run
window.mainloop()
