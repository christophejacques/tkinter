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
window.title("Tkinter Canvas")
window.geometry("400x300")

def bind_function(param):
    dprint(param)
    if param.keycode == 27:
        window.quit()
window.bind("<KeyPress>", bind_function)

# Canvas
canvas = tk.Canvas(master=window, bg="lightblue")
canvas.pack(pady=10)

canvas.create_rectangle((80, 10, 300, 80), 
    fill="green", 
    width=4,
    outline="red",
    dash=(5, 1, 2))

canvas.create_line((10, 10, 50, 200), 
    width=2,
    fill="red")

canvas.create_oval(200, 200, 100, 100)
canvas.create_arc((200, 200, 100, 100), 
    start=45, 
    extent=180,
    fill="white",
    outline="red",
    width=2,
    style=tk.PIESLICE)

canvas.create_text((10, 250), 
    anchor="w",
    text="Une ligne de mon texte\nUne deuxieme ligne de texte")

clique_souris = tk.BooleanVar()
# mouse_value = ttk.Entry(master=window, 
#     textvariable=clique_souris,
#     width=50)
# mouse_value.pack(pady=10)

canvas.create_window((330, 250), 
    window=ttk.Button(window, text="Valider"))

def click_event(event):
    if event.num == 1:
        clique_souris.set(True)
        dprint("mouseButton down", event)

def release_event(event):
    if event.num == 1:
        clique_souris.set(False)
        dprint("mouseButton up")

window.bind("<Button>", click_event)
window.bind("<ButtonRelease>", release_event)

def print_pixel(event):
    if not clique_souris.get():
        return
    size: int = 2
    canvas.create_oval(
        (event.x-size, event.y-size, event.x+size, event.y+size),
        fill="black")

window.bind("<Motion>", print_pixel)

# Run
window.mainloop()
