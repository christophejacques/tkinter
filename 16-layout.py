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
window.title("Layout")
# window.geometry("600x400")
window.geometry("400x600+100+50")


def bind_function(param):
    if param.keycode == 27:
        window.destroy()
        window.quit()


window.bind("<KeyPress>", bind_function)

# Layout
if False:
    # Pack
    left = tk.Frame(master=window, background="yellow")
    right = tk.Frame(master=window, background="brown")

    labels = []
    labels.append(ttk.Label(master=left, text="Label 1", background="red"))
    labels.append(ttk.Label(master=left, text="Label 2", background="green"))
    labels.append(ttk.Label(master=right, text="Label 3", 
        background="blue", 
        foreground="yellow",))
    [label.pack(fill="both") for label in labels]

    left.pack(side="left", expand=True, fill="both")
    right.pack(side="right", expand=True, fill="both")


def button_command():

    def bind_new_function(param):
        if param.keycode == 27:
            new_window.destroy()
            new_window.quit()

    new_window = tk.Tk()
    new_window.title("New Layout")
    new_window.geometry("400x300+100+150")
    new_window.bind("<KeyPress>", bind_new_function)

    new_label = ttk.Label(master=new_window, text="mon texte", background="orange")
    new_label.place(relx=0.025, y=10, relwidth=0.95, height=100)
    
    new_window.focus_force()
    new_window.mainloop()
    print("Fin")


label1 = ttk.Label(master=window, text="Label 1", background="red")
label2 = ttk.Label(master=window, text="Label 2", background="blue", foreground="yellow")
label3 = ttk.Label(master=window, text="Last of the Labels", background="green")
bouton = ttk.Button(master=window, text="Bouton", command=button_command)

if False:
    # Grid
    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.columnconfigure(2, weight=2)
    window.rowconfigure(0, weight=1)
    window.rowconfigure(1, weight=1)

    label1.grid(row=0, column=1, sticky="nsew")
    label2.grid(row=1, column=1, columnspan=2, sticky="nsew")

if False:
    # Place
    label1.place(x=100, y=280, width=100, height=100)
    label2.place(relx=0.5, rely=0.2, relwidth=1, relheight=0.5, anchor="se")

if False:
    # Exercice
    window.columnconfigure(0, weight=8)
    window.columnconfigure(1, weight=1)
    window.rowconfigure(0, weight=6)

    # window.rowconfigure((1, 2), weight=2)

    window.rowconfigure(1, weight=2)
    window.rowconfigure(2, weight=2)

    label1.grid(row=0, column=0, columnspan=2, sticky="nsew")
    label2.grid(row=1, column=0, rowspan=3, sticky="nsew")
    label3.grid(row=1, column=1, sticky="nsew")
    bouton.grid(row=2, column=1, sticky="nsew")

if False:
    label1.pack(side="top", fill="x")
    label2.pack(side="top", expand=True)
    label3.pack(side="top", fill="both", expand=True)
    bouton.pack(side="bottom", fill="x")

if False:
    label1.pack(side="top", fill="both", expand=True, padx=10, pady=10)
    label2.pack(side="left", fill="both", expand=True)
    label3.pack(side="top", fill="both", expand=True)
    bouton.pack(side="bottom", fill="both", expand=True)

if True:
    label1.place(x = 10, y = 10, width = 380, height = 150)
    # label1.place(relx = 0.5, rely = 0.5, relwidth = 0.5, height = 200, anchor="center")
    label2.place(relx=0, rely=0.3, relwidth=0.8, relheight=0.7, anchor="nw")
    label3.place(relx=0.8, rely=0.3, relwidth=0.2, relheight=0.35)
    bouton.place(relx=0.8, rely=0.65, relwidth=0.2, relheight=0.35)

# Run
window.mainloop()
