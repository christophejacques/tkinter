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
window.title("Frames & Parenting")
window.geometry("600x400")

def bind_function(param):
    if param.keycode == 27:
        window.quit()
window.bind("<KeyPress>", bind_function)


# Frame
frame = ttk.Frame(
    master=window,
    borderwidth=10,
    relief=tk.GROOVE,
    width=200,
    height=200)
frame.pack_propagate(False)
frame.pack(side="top")

# Parenting
label = ttk.Label(master=frame, text="Label dans le frame")
label.pack()

bouton = ttk.Button(master=frame, text="Valider")
bouton.pack()

# example
label2 = ttk.Label(master=window, text="Label en dehors du frame")
label2.pack()


# Run
window.mainloop()

