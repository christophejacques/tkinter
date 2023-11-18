import tkinter as tk
from tkinter import ttk, scrolledtext
from random import choice
from time import sleep


def dprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)


def button_function(valeur):
    def fonction():
        dprint(valeur.get())
    return fonction


# window 
window = tk.Tk()
window.title("Progressbar & Sliders")
# window.geometry("400x300")


def bind_function(param):
    if param.keycode == 27:
        window.quit()


window.bind("<KeyPress>", bind_function)


# Slider (Scale)
scale = tk.Scale(
    master=window,
    from_=0,
    to=200,
    length=300,
    orient="horizontal",
    command=lambda value: dprint("move scale:", value))
scale.pack()


# Progressbar
pb = ttk.Progressbar(
    master=window,
    length=298)
pb.pack(pady=10)


def update_bar():
    valeur: int = pb["value"]
    if valeur < 100:
        pb.configure(value=1+valeur)
        pb.after(100, update_bar)
    else:
        window.quit()


# pb.after(100, update_bar)
pb.start()
pb.after(5000, pb.stop)

# ScrollText
st = scrolledtext.ScrolledText(
    master=window,
    height=6)
st.pack()

# Run
window.mainloop()
