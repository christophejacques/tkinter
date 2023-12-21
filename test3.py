from os import path
from random import randint


tkinter_classe = __import__("20-classes")
fprint = tkinter_classe.fprint
App: type = tkinter_classe.App

def click(*args):
    print(root.geometry(), flush=True)
    root.destroy()
    root.quit()


root = App("root", size=(300, 100))
with root.add_frame() as frame:
    label = frame.add_widget("label", 
        text="Ceci est un texte très long qui contient des liens hypertextes. Vous pouvez cliquer sur les liens pour accéder à d'autres pages web.", 
        wraplength=300, 
        bg="orange",
        justify='right')
    # label.anchor = 'w'
    label.pack()

    # Créer un lien hypertexte
    hyperlink = frame.add_widget("label", 
        text="[Lien vers Google]", 
        fg="green",   #000099
        cursor="hand2", 
        activeforeground="#0000FF",
        pady=10,
        command=click)
    hyperlink.pack()

# Afficher la fenêtre
root.mainloop()

exit()
