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
window.title("Toggling widget")
window.geometry("600x400+1000+50")


def bind_function(param):
    if param.keycode == 27:
        window.destroy()
        window.quit()


window.bind("<KeyPress>", bind_function)

# Toggling widget
label1 = ttk.Label(master=window, text="Label 1", background="red")
label2 = ttk.Label(master=window, text="Label 2", background="blue", foreground="yellow")
label3 = ttk.Label(master=window, text="Label 3", background="green")

labels: dict = {}
labels["label1"] = True


def toggle_button(btn_label: str):
    def action(*args, **kwargs):
        if labels[btn_label]:
            label1.place_forget()
        else:
            label1.place(x=50, y=100, width=200, height=150)
            label1.tkraise()

        labels[btn_label] = not labels[btn_label]
    return action


def action2():
    label2.tkraise(aboveThis=label1)


def action3():
    label3.tkraise(aboveThis=label2)


def toggle_grid():
    if labels["label1"]:
        label1.grid_forget()
    else:
        label1.grid(column=0, row=0)

    labels["label1"] = not labels["label1"]


if False:
    # Place
    bouton1 = ttk.Button(master=window, text="raise Label1", command=toggle_button("label1"))
    bouton2 = ttk.Button(master=window, text="raise Label2", command=action2)
    bouton3 = ttk.Button(master=window, text="raise Label3", command=action3)

    label1.place(x=50, y=100, width=200, height=150)
    label2.place(x=150, y=60, width=140, height=100)
    label3.place(x=200, y=100, width=140, height=100)

    bouton1.place(rely=1, relx=0.6, anchor="se")
    bouton2.place(rely=1, relx=0.8, anchor="se")
    bouton3.place(rely=1, relx=1, anchor="se")

if False:
    # Grid
    window.columnconfigure((0, 1), weight=1, uniform="a")
    window.rowconfigure(0)
    bouton1 = ttk.Button(
        master=window, 
        text="raise Label1",
        width=40,
        command=toggle_grid)
    
    label1.grid(column=0, row=0)
    bouton1.grid(column=1, row=0)


def toggle_pack():
    if labels["label1"]:
        label1.pack_forget()
    else:
        # label1.pack(expand=True, fill="both", before=bouton1)  # Ou v
        label1.pack(expand=True, fill="both")

    labels["label1"] = not labels["label1"]


if True:
    # Pack
    frame = ttk.Frame(master=window)
    label1 = ttk.Label(master=frame, text="Label 1", background="red")
    bouton1 = ttk.Button(
        master=window, 
        text="toggle Label1",
        width=40,
        command=toggle_pack)
    frame.pack(side="top", expand=True, fill="both")
    label1.pack(expand=True, fill="both")
    bouton1.pack(side="top")


# Run
window.mainloop()
