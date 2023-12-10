from os import path
from tkinter import font, ttk
from random import choice


def fprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)


maClasse = __import__("20-classes") 
app = maClasse.App(__file__.split(path.sep)[-1], (400, 300))
App = maClasse.App

style = ttk.Style()
fprint(style.theme_names())
style.theme_use("clam")

style.configure("new.TButton", background="lightgreen", foreground="black", font=("Arial", 20))
style.map("new.TButton", 
    foreground=[("pressed", "red"), ("disabled", "gray"), ("active", "red")],
    background=[("pressed", "yellow"), ("disabled", "lightgray"), ("active", "lightgreen")])


def Window1():
    app.maxsize(600, 400)
    with app.add_frame("pack", expand=True, fill="both") as f1:
        f1.add_widget("label", 
            text="Mon premier label",
            font=(choice(font.families()), 24),
            background="orange",
            foreground="brown",
            anchor="c").pack(expand=True, fill="both")
        with f1.add_frame("pack", expand=True) as sf1:

            sf1.add_widget("button", 
                text=" Open Window ",
                style="new.TButton").pack(side="left")

            sf1.add_widget("button", 
                text="Disable",
                state="disabled",
                style="new.TButton").pack(side="left")


Window1()
app.run()
