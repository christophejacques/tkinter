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
window.title("Stacking order")
window.geometry("400x400+1000+50")


def bind_function(param):
    if param.keycode == 27:
        window.destroy()
        window.quit()


window.bind("<KeyPress>", bind_function)

# Stacking order
label1 = ttk.Label(master=window, text="Label 1", background="red")
label2 = ttk.Label(master=window, text="Label 2", background="blue", foreground="yellow")
label3 = ttk.Label(master=window, text="Label 3", background="green")

def action1():
    label1.lift()
    label2.lower()

def action2():
    label2.tkraise(aboveThis=label1)

def action3():
    label3.tkraise(aboveThis=label2)

bouton1 = ttk.Button(master=window, text="raise Label1", command=action1)
bouton2 = ttk.Button(master=window, text="raise Label2", command=action2)
bouton3 = ttk.Button(master=window, text="raise Label3", command=action3)

label1.place(x=50, y=100, width=200, height=150)
label2.place(x=150, y=60, width=140, height=100)
label3.place(x=200, y=100, width=140, height=100)

bouton1.place(rely=1, relx=0.6, anchor="se")
bouton2.place(rely=1, relx=0.8, anchor="se")
bouton3.place(rely=1, relx=1, anchor="se")


# Run
window.mainloop()
