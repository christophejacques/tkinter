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
    # dprint(param)
    if param.keycode == 27:
        window.quit()


window.bind("<KeyPress>", bind_function)

# Canvas
canvas = tk.Canvas(master=window, bg="lightblue")
canvas.pack(pady=10)

rectangle_params: list = [(80, 10), (300, 80)]
canvas.create_rectangle(rectangle_params, 
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


def is_in_rectangle(position: list, rectangle: list) -> bool:
    if all([rectangle[0][0] < position[0] < rectangle[1][0],
      rectangle[0][1] < position[1] < rectangle[1][1]]):
        return True
    return False


def is_in_circle(position: list, circle_center_position: list, rayon: float):
    dx = circle_center_position[0] - position[0]
    dy = circle_center_position[1] - position[1]
    distance = dx*dx + dy*dy
    return distance < rayon*rayon


position_souris: list = [-1, -1]
clique_souris = tk.BooleanVar()

bouton_valider = ttk.Button(canvas, text="Quitter")
canvas.create_window((330, 250), 
    window=bouton_valider)


def click_event(event):
    if event.num == 1:
        clique_souris.set(True)
        position_souris[0] = event.x
        position_souris[1] = event.y


def release_event(event):
    if event.num == 1:
        clique_souris.set(False)
        # dprint("mouseButton up")


def print_pixel(event):
    
    if not clique_souris.get():
        return

    if not is_in_circle((event.x, event.y), (150, 150), 50):
        if is_in_rectangle((event.x, event.y), rectangle_params):
            color = "black"
        else:
            color = "red"

        canvas.create_line((*position_souris, event.x, event.y), 
            width=4, fill=color)

    position_souris[0] = event.x
    position_souris[1] = event.y


canvas.bind("<Button>", click_event)

canvas.bind("<ButtonRelease>", release_event)
canvas.bind("<Motion>", print_pixel)


def release_check(event):
    if all([event.num == 1,
      0 <= event.x < bouton_valider.winfo_width(),
      0 <= event.y < bouton_valider.winfo_height()]):
        window.quit()


bouton_valider.bind("<Button-1>", lambda *_: None)
bouton_valider.bind("<ButtonRelease>", release_check)

# Run
window.mainloop()
