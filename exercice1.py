import tkinter as tk
import ttkbootstrap as ttk


def dprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)


def convert():
    res = 1.61 * entreeEntier.get()
    output_string.set(f"{res:.2f}")


# window = tk.Tk()
window = ttk.Window(themename="darkly")
window.title("Convertir")
window.geometry("350x130")

# Titre
title_label = ttk.Label(master=window, text="Transformer Miles en Km", font="Arial 20 bold")
title_label.pack(pady=1)

# Saisie
input_frame = ttk.Frame(master=window)
entreeEntier = tk.IntVar()
entree = ttk.Entry(master=input_frame, textvariable=entreeEntier)
entree.focus()
bouton = ttk.Button(master=input_frame, text="Valider", command=convert)

entree.pack(side="left", padx=10)
bouton.pack(side="left")
input_frame.pack(pady=10)

# Resultat
output_string = tk.StringVar()
output_label = ttk.Label(master=window, text="zz", font="Arial 20", textvariable=output_string)
output_label.pack()


# Run
window.mainloop()
