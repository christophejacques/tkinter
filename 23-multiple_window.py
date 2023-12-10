from os import path
from tkinter import messagebox


maClasse = __import__("20-classes") 
app = maClasse.App(__file__.split(path.sep)[-1], (400, 300))
App = maClasse.App

open_apps: list = list()
unique_window: list = list()


def fprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)


def ask_yes_no():
    fprint(messagebox.askquestion("Titre", "Body"))


def is_window_open(win_handle) -> bool:
    try:
        win_handle.winfo_exists()
    except Exception:
        return False
    return True    


def close_window(handle, reponse: str = ""):
    if not is_window_open(handle):
        fprint("Fenetre non ouverte")

    if reponse:
        fprint(reponse)
    handle.destroy()
    handle.quit()


def button1_clicked():
    if len(unique_window):
        unique_window[0].focus_force()

    else:
        new_app = maClasse.App("main Window", (300, 100), (400, 400))
        with new_app.add_frame() as f1:
            f1.add_widget("label", text="Texte dans l'unique Window").pack()

        new_app.focus_force()
        unique_window.append(new_app)
        new_app.run()


def button2_clicked():
    numero: int = len(open_apps)
    posy = 100 + (numero*320 + 80) // 1600 * 120
    posx = (numero*320 + 80) % 1600
    new_app = maClasse.App("main Window", (300, 100), (posx, posy))
    msg: str 
    if numero:
        msg = f"Texte dans la Window n°{numero}"
    else:
        msg = "Texte dans la main Window"

    with new_app.add_frame() as f1:
        f1.add_widget("label", text=msg).pack()

    new_app.focus_force()
    open_apps.append(new_app)
    new_app.run()


def button3_clicked():
    if len(open_apps) == 0:
        return

    new_app = open_apps.pop()
    close_window(new_app)


def action(win_handle, reponse: str = ""):
    close_window(win_handle)

    if reponse.upper() != "OUI":
        return

    if len(unique_window):
        close_window(unique_window.pop())


def button4_clicked():
    if len(unique_window) == 0:
        standalone_app = maClasse.App("Erreur", (300, 100))
        with standalone_app.add_frame(expand=True) as f1:
            f1.add_widget("label", text="La fenêtre unique n'a pas été ouverte.").pack()
            f1.add_widget("label", text="Elle ne peut donc pas être fermée !").pack()

        with standalone_app.add_frame(expand=True, fill="both") as f2:
            f2.add_widget("button", text="Fermer", command=lambda: action(standalone_app)).pack(side="left", expand=True)
        
    else:
        standalone_app = maClasse.App("Question", (300, 100))
        with standalone_app.add_frame(expand=True) as f1:
            f1.add_widget("label", text="Voulez-vous fermer").pack()
            f1.add_widget("label", text="la fenêtre unique ?").pack()
        with standalone_app.add_frame(expand=True, fill="both") as f2:
            f2.add_widget("button", text="Non", command=lambda: action(standalone_app, "Non")).pack(side="left", expand=True)
            f2.add_widget("button", text="Oui", command=lambda: action(standalone_app, "Oui")).pack(side="left", expand=True)

    standalone_app.focus_force()
    standalone_app.run()


def Window1():
    app.maxsize(600, 400)
    with app.add_frame("pack", expand=True, fill="both") as f1:
        t1 = f1.add_widget("button", text="Open Unique Window", command=button1_clicked)
        t1.pack(expand=True)

    with app.add_frame("pack", expand=True, fill="both") as f2:
        with f2.add_frame("pack", side="left", expand=True, fill="both") as sf1:
            t1 = sf1.add_widget("button", text="Open multiple Windows", command=button2_clicked)
            t1.pack(expand=True)

        with f2.add_frame("pack", side="left", expand=True, fill="both") as sf2:
            t2 = sf2.add_widget("button", text="Destroy multiple Window", command=button3_clicked)
            t2.pack(expand=True)

    with app.add_frame("pack", expand=True, fill="both") as f4:
        t3 = f4.add_widget("button", text="Create Yes/No Window", command=button4_clicked)
        t3.pack(expand=True)

    with app.add_frame("pack", expand=True, fill="both") as f5:
        t4 = f5.add_widget("button", text="MessageBox Yes/No", command=ask_yes_no)
        t4.pack(expand=True)


Window1()
app.run()
