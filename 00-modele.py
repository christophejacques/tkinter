from os import path


def fprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)


maClasse = __import__("20-classes") 
app = maClasse.App(__file__.split(path.sep)[-1], (400, 300))


def Window1():
    app.maxsize(600, 400)
    with app.add_frame("pack", expand=True, fill="both") as f1:
        f1.add_widget("label", text="Appuyer sur la touche 'Echap' pour quitter l'application").pack(expand=True, pady=(0,30))


Window1()
app.run()
