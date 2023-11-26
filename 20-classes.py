import ctypes
import tkinter as tk
from tkinter import ttk, scrolledtext


def dprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)


# Classes
class cWidget:

    WIDGETS: dict = {
        "label": ttk.Label,
        "libelle": ttk.Label,
        "button": ttk.Button,
        "boutton": ttk.Button,
        "entry": ttk.Entry,
        "text": ttk.Entry,
        "scrolledtext": scrolledtext.ScrolledText,
        "scrollbar": ttk.Scrollbar, 
        "checkbutton": ttk.Checkbutton,
        "radiobutton": ttk.Radiobutton,
        "combobox": ttk.Combobox,
        "spinbox": ttk.Spinbox,
        "progressbar": ttk.Progressbar,
        "scale": ttk.Scale,
        "canvas": tk.Canvas
    }

    def __init__(self, parent, type_widget: str):
        self.parent = parent
        self.type_widget = type_widget

    def parametres(self, **kwargs):
        type_widget = self.type_widget.lower()
        if type_widget not in cWidget.WIDGETS:        
            raise Exception(f"Le type de widget {self.type_widget} n'existe pas. Il faut saisir: Label, Text, ScrolledText, Combobox, etc...")

        return cWidget.WIDGETS[type_widget](master=self.parent, **kwargs)


class cFrame(ttk.Frame):
    def __init__(self, parent, type_layout: str = "pack", **kwargs) -> None:
        super().__init__(master=parent)

        match type_layout.lower():
            case "pack":
                self.pack(**kwargs)
            case "grid":
                self.grid(**kwargs)
            case "place":
                self.place(**kwargs)
            case _:
                raise Exception(f"Le type de placement {type_layout} n'existe pas. Il faut saisir: pack, grid ou place")

    def __enter__(self, *args):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        # print("exit:", exc_type, exc_value)
        pass

    def add_frame(self, type_layout: str = "pack", **kwargs):
        new_frame = cFrame(self, type_layout, **kwargs)
        return new_frame
    
    def add_widget(self, type_widget: str, **kwargs) -> cWidget:
        new_widget = cWidget(self, type_widget)
        return new_widget.parametres(**kwargs)


class App(tk.Tk):
    def __init__(self, title: str, size: tuple):
        # Main setup
        super().__init__()
        self.title(title)
        
        # Centre la fenetre
        screen_size = self.get_screenSize()
        posx = screen_size[0]//2 - size[0]//2
        posy = screen_size[1]//2 - size[1]//2
        
        self.geometry(f"{size[0]}x{size[1]}+{posx}+{posy}")
        self.minsize(*size)

        # configuration de la touche Echappe pour sortir de l'application
        self.bind("<KeyPress>", self.escape_function)

    def get_screenSize(self) -> tuple:
        user32 = ctypes.windll.user32
        return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    
    def escape_function(self, param):
        if param.keycode == 27:
            self.destroy()
            self.quit()

    def add_frame(self, type_layout: str = "pack", **kwargs) -> cFrame:
        new_frame = cFrame(self, type_layout, **kwargs)
        return new_frame
    
    def run(self):
        self.mainloop()


def main():
    app = App("Demo de la classe", (1440, 750))
    with app.add_frame("place", x=0, relwidth=0.3, y=0, relheight=1) as frame_gauche:
        with frame_gauche.add_frame("place", y=0, relwidth=1, height=100) as fg1:
            fg1.add_widget(
                "button", 
                text="Bounton1", 
                ).pack(expand=True, side="left", fill="both", padx=(2, 1), pady=2)
            fg1.add_widget(
                "button", 
                text="Bounton2", 
                ).pack(side="left", expand=True, fill="both", padx=(1, 2), pady=2)

        with frame_gauche.add_frame("place", y=100, relwidth=1, height=100) as fg2:
            fg2.add_widget(
                "button", 
                text="Bounton3", 
                ).pack(expand=True, fill="both", padx=2, pady=2)

        with frame_gauche.add_frame("place", y=200, relwidth=1) as fg3:
            fg3.add_widget(
                "Scale", 
                orient="vertical", length=400
                ).pack(side="left", expand=True, fill="both", pady=20)
            fg3.add_widget(
                "Scale", 
                orient="vertical"
                ).pack(side="left", expand=True, fill="both", pady=20)

        with frame_gauche.add_frame("place", rely=1, relwidth=1, height=60, anchor="sw") as fg4:
            with fg4.add_frame("pack") as fcbtn:
                cvaleur1 = tk.BooleanVar(value=True)
                fcbtn.add_widget(
                    "Checkbutton",
                    text="check 1", variable=cvaleur1, onvalue=True, offvalue=False
                    ).pack(side="left")

                cvaleur2 = tk.BooleanVar(value=True)
                fcbtn.add_widget(
                    "Checkbutton",
                    text="check 2", variable=cvaleur2, onvalue=True, offvalue=False
                    ).pack(side="right")
                fg4.add_widget(
                    "Entry"
                    ).pack(expand=True, fill="both", padx=20, pady=(5, 10))

    with app.add_frame("place", relx=0.3, relwidth=0.7, y=0, relheight=1) as frame_droite:
        with frame_droite.add_frame(expand=True, fill="both") as fd1:
            with fd1.add_frame(expand=True, fill="both") as fdp1:
                fdp1.add_widget(
                    "Label", 
                    text="Label3", background="red"
                    ).pack(side="left", expand=True, fill="both", padx=20, pady=(25, 5))

                fdp1.add_widget(
                    "Label", 
                    text="Label4", background="blue"
                    ).pack(side="left", expand=True, fill="both", padx=20, pady=(25, 5))

        with frame_droite.add_frame(expand=True, fill="both") as fd2:
            fd2.add_widget(
                "button",
                text="bouton1"
                ).pack(side="left", expand=True, fill="both", padx=20, pady=(5, 25))
            fd2.add_widget(
                "button",
                text="bouton2"
                ).pack(side="left", expand=True, fill="both", padx=20, pady=(5, 25))

    app.run()


if __name__ == "__main__":
    main()
