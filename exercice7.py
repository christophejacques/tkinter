import tkinter as tk
from tkinter import ttk


def dprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)


def button_function(valeur):
    def fonction():
        dprint(valeur.get())
    return fonction


def bind_function(param):
    dprint(param)
    if param.keycode == 27:
        window.quit()

def get_position(pos):
    entree_string.set(pos)


# window 
window = tk.Tk()
window.title("Tkinter Event binding")
window.geometry("400x300")

# tk Text
texte = tk.Text(master=window, height=5, width=40)
texte.pack(pady=10)

# ttk Entry
entree_string = tk.StringVar()
entree = ttk.Entry(master=window, 
    textvariable=entree_string,
    width=50)
entree.pack(pady=10)

# ttk Buttons
button = ttk.Button(master=window, text="Button")
button.pack()

# Events
# window.bind(event (str), function)

# window.bind("<KeyPress>", bind_function)
window.bind("<Motion>", get_position)

entree.bind("<FocusIn>", bind_function)
entree.bind("<FocusOut>", bind_function)


# Run
window.mainloop()
