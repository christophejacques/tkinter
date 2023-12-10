import tkinter as tk

# Créer la fenêtre
window = tk.Tk()
window.title("Ma fenêtre")


def fprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)


# Définir un gestionnaire d'événement pour l'événement `WM_DELETE_WINDOW`
def on_window_close():
    fprint("Demande de fermeture de la fenetre ... ", end="")
    window.destroy()
    window.quit()
    fprint("done")


def on_enter_window(event):
    fprint(event)


def on_leave_window(event):
    fprint(event)


# Démarrer les gestionnaires d'événements
window.protocol("WM_DELETE_WINDOW", on_window_close)
window.bind("<Enter>", on_enter_window)
window.bind("<Leave>", on_leave_window)

# Démarrer la boucle principale
window.mainloop()
