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
window.title("Menu")
window.geometry("600x400")

def bind_function(param):
    if param.keycode == 27:
        window.quit()
window.bind("<KeyPress>", bind_function)


# Menu
menu = tk.Menu(master=window)
file_menu1 = tk.Menu(master=menu, tearoff=False)
file_menu1.add_command(label = "Nouveau", command=lambda: print("New"))
file_menu1.add_command(label = "Ouvrir", command=lambda: print("Open"))
file_menu1.add_command(label = "Enregistrer", command=lambda: print("Save"))
file_menu1.add_command(label = "Enregistrer sous", command=lambda: print("Save"))
file_menu1.add_separator()
file_menu1.add_command(label = "Apercu avant impression", command=lambda: print("Save"))
file_menu1.add_command(label = "Imprimer", command=lambda: print("Save"))
file_menu1.add_separator()
file_menu1.add_command(label = "Quitter", command=window.quit)

menu.add_cascade(label = "File", menu=file_menu1)

edit_menu = tk.Menu(master=menu, tearoff=False)
edit_menu.add_command(label = "Annuler", command=lambda: print("Undo"))
edit_menu.add_command(label = "Retablir", command=lambda: print("Redo"))
edit_menu.add_separator()
edit_menu.add_command(label = "Copier", command=lambda: print("Redo"))
edit_menu.add_command(label = "Couper", command=lambda: print("Cut"))
edit_menu.add_command(label = "Coller", command=lambda: print("Paste"))

menu.add_cascade(label = "Edition", menu=edit_menu)

help_menu = tk.Menu(master=menu, tearoff=False)
help_menu.add_command(label = "Bienvenue", command=lambda: print("Aider"))
help_menu.add_command(label = "Vérifier les mises à jour", command=lambda: print("Update"))

toujours_afficher = tk.BooleanVar()
help_menu.add_checkbutton(
    label = "Toujours afficher", 
    onvalue=True, 
    offvalue=False,
    variable=toujours_afficher)
help_menu.add_separator()
help_menu.add_command(label = "A propos de", command=lambda: print("Aider"))

menu.add_cascade(label = "Aide", menu=help_menu)

window.configure(menu=menu)

# bouton Menu
btn_menu = ttk.Menubutton(master=window, text="Bouton Menu")
btn_menu.pack()

btn_sub_menu = tk.Menu(btn_menu, tearoff=False)
btn_sub_menu.add_command(label="sous menu", command=lambda: print("ssmenu"))
btn_sub_menu.add_checkbutton(
    label="Check", 
    onvalue=True,
    offvalue=False)
btn_menu.configure(menu=btn_sub_menu)



# Run
window.mainloop()

