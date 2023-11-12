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
window.title("Tabs")
window.geometry("600x400")

def bind_function(param):
    if param.keycode == 27:
        window.quit()
window.bind("<KeyPress>", bind_function)


# Tabs
tabs = ttk.Notebook(master=window)
tabs.pack()

tab1 = ttk.Frame(master=tabs)
label1 = ttk.Label(master=tab1, text="label dans tab 1")
bouton1 = ttk.Button(master=tab1, text="btn dans tab 1")
label1.pack()
bouton1.pack()

tab2 = ttk.Frame(master=tabs)
label2 = ttk.Label(master=tab2, text="label dans tab 2")
bouton2 = ttk.Button(master=tab2, text="btn dans tab 2")
label2.pack()
bouton2.pack()
entree = ttk.Entry(master=tab2)
entree.pack()

tab3 = ttk.Frame(master=tabs)
bouton31 = ttk.Button(master=tab3, text="btn 1 dans tab 3")
bouton32 = ttk.Button(master=tab3, text="btn 2 dans tab 3")
bouton31.pack()
bouton32.pack()


tabs.add(tab1, text="Tab 1")
tabs.add(tab2, text="Tab 2")
tabs.add(tab3, text="Tab 3")



# Run
window.mainloop()

