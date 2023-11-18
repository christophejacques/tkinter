import tkinter as tk
# import ttkbootstrap as ttk
from tkinter import ttk


def dprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)


def button_function():
    window.quit()

def valider_bouton():
    label2["text"] = entree.get()
    entree["state"] = "disabled"
    bouton1["state"] = "disabled"
    for attribut in label2.configure():
        print(label2.configure().get(attribut))

# window = tk.Tk()
window = tk.Tk()
window.title("Window & Widgets")
# window.geometry("400x300")

# ttk.Label
label1 = tk.Label(master=window, text="Une ligne de texte en Label 1")
label1.pack()
label1.config(text="nouveau texte 1")

label2 = tk.Label(master=window, text="Une ligne de texte en Label 2")
label2.pack()
label2["text"] = "nouveau texte 2"

# ttk.Entry
entree = ttk.Entry(master=window)
entree.pack(pady=20)

# Frame
zone_boutons = tk.Frame(master=window)

# ttk.Button
bouton1 = ttk.Button(master=zone_boutons, text="Valider", command=valider_bouton)
bouton1.pack(padx=20, side="left")

bouton2 = ttk.Button(master=zone_boutons, text="Fermer", command=button_function)
bouton2.pack()
zone_boutons.pack(pady=20)

# Run
window.mainloop()
