import tkinter as tk
from tkinter import ttk


def dprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)


def button_function(valeur):
    def fonction():
        dprint(valeur.get())
    return fonction


# window 
window = tk.Tk()
window.title("Tkinter Combobox and Spinbox")
window.geometry("400x300")

def bind_function(param):
    dprint(param)
    if param.keycode == 27:
        window.quit()
window.bind("<KeyPress>", bind_function)


# tk Combobox
items = ["Glace", "Pizza", "Alpha", "Sac"]

chaine = tk.StringVar(value= items[0])
cb = ttk.Combobox(master=window, 
    textvariable=chaine, 
    values=items)
cb.pack(pady=10)

cb.bind("<<ComboboxSelected>>", lambda e: dprint(chaine.get()))

label = ttk.Label(master=window, textvariable=chaine)
label.pack()

# Spinbox
sb = ttk.Spinbox(
    master=window, 
    from_=1,
    to=10,
    increment=3,
    # values=items
    command=lambda: dprint(sb.get())
    )
sb.pack(pady=10)
sb.bind("<<Increment>>", lambda e: dprint("up"))
sb.bind("<<Decrement>>", lambda e: dprint("down"))

# Run
window.mainloop()
