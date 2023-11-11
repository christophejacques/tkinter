import tkinter as tk
from tkinter import ttk
from random import choice


def dprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)

def button_function(valeur):
    def fonction():
        dprint(valeur.get())
    return fonction



# window 
window = tk.Tk()
window.title("Tkinter Treeview")
# window.geometry("400x300")

def bind_function(param):
    # dprint(param)
    if param.keycode == 27:
        window.quit()
window.bind("<KeyPress>", bind_function)

# Treeview
first_names = ["Bob", "Maria", "Alex", "James", "Susan", "Henry", "Lisa", "Anna", "Lisa"]
last_names = ["Smith", "Brown", "Wilson", "Thomson", "Cook", "Taylor", "Walker", "Clark"]

table = ttk.Treeview(
    master=window,
    columns=("Last", "First", "Email"),
    show="headings")

table.heading("First", text="Prenom")
table.heading("Last", text="Nom")
table.heading("Email", text="Mail")
table.pack(fill="both", expand=True)

# insert valeur dans la table
# for idx, (nom, prenom) in enumerate(zip(first_names, last_names)):
for idx in range(100):
    nom = choice(last_names)
    prenom = choice(first_names)
    table.insert(
        parent="",
        index=tk.END, # idx
        values=(prenom, nom, f"{prenom.lower()}.{nom.lower()}@gmail.com"))

def print_selected(_):
    for ligne in table.selection():
        print(table.item(ligne)["values"])

def delete_selected(_):
    for ligne in table.selection():
        print("delete:", table.item(ligne)["values"])
        table.delete(ligne)
    

table.bind("<<TreeviewSelect>>", print_selected)
table.bind("<Delete>", delete_selected)


# Run
window.mainloop()
