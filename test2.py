from os import path
from random import randint


tkinter_classe = __import__("20-classes")
fprint = tkinter_classe.fprint
App: type = tkinter_classe.App
app = App(__file__.split(path.sep)[-1], (500, 200))


def notif(*args):
    message: str = "{align=left}Premiere ligne de texte\n{fg=green}Suite"
    for ligne in range(randint(1, 4)):
        message += f"\nligne numero {ligne}"

    tkinter_classe.Notification("{align=center}{fg=white}Titre de la notif", 
        message,
        bg="#101010", fg="#A0A0A0",
        show=True)


frame = app.add_frame()
frame.add_widget("label", 
    text="Ouvrir un notification", 
    activeforeground="blue",
    font=("", 24),
    command=notif).pack(pady=20)
frame.add_widget("button", text="deplacement", command=notif).pack(expand=True)

app.run()
fprint("Fin")
