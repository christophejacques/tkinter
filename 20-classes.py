import re
import ctypes
import tkinter as tk
from tkinter import ttk, scrolledtext


def fprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)


class cTKType:

    def __init__(self):
        if len(list(filter(lambda x: not x.startswith("_"), dir(cTKType)))) > 0:
            return

        for attrib in [nom for nom in dir(tk) if nom.endswith("Var")]:
            setattr(cTKType, attrib, getattr(tk, attrib))


class cTKConstante:
    CURSORS: list[str] = [
        "arrow", "ibeam", "crosshair", "hand1", "hand2", "fleur", "man", "pencil", "pirate", 
        "plus", "sb_h_double_arrow", "sb_v_double_arrow", "watch"]

    def __init__(self):        
        if len(list(filter(lambda x: not x.startswith("_"), dir(cTKConstante)))) > 0:
            return
            
        for attrib in dir(tk):
            if attrib == attrib.upper():
                setattr(cTKConstante, attrib, getattr(tk, attrib))


def check_kwargs(kwargs):
    message: str = ""
    for key in kwargs:
        value = kwargs[key]
        match key:
            case "cursor": 
                if value not in cTKConstante.CURSORS:
                    message = f"'{value}' n'est pas un type de curseur valide"
                    message += "\nLes valeurs valides sont: ("
                    message += ", ".join(cTKConstante.CURSORS) + ")"
                    raise Exception(message)


# Classes
class cWidget:

    WIDGETS: dict = {
        "menu": tk.Menu,
        "label": tk.Label,
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
        "canvas": tk.Canvas,
        "treeview": ttk.Treeview, 
        "listbox": tk.Listbox,
        "notebook": ttk.Notebook,
        "tabs": ttk.Notebook
    }

    def __init__(self, parent, type_widget: str):
        self.parent = parent
        self.type_widget = type_widget
        self.saved: dict = {}

    def filtrage_kwargs(self, type_widget, kwargs):
        kwargs_filtres: dict = {}
        if type_widget != "label":
            return kwargs_filtres

        if "command" in kwargs:
            kwargs_filtres["command"] = kwargs.pop("command")

        return kwargs_filtres

    def check_params(self, widget, **params):
        kwargs_on: dict = {}
        kwargs_off: dict = {}
        type_widget = self.type_widget.lower()

        for key in params:
            match key:
                case "command":
                    if type_widget == "label":
                        widget.bind("<Button-1>", params.get(key))
                        
                case "activeforeground" | "activebackground":
                    new_key: str = "fg" if key == "activeforeground" else "bg"
                    activebgcolor = widget.cget(new_key)
                    newbgcolor = params.get(key)
                    kwargs_on.update({new_key: newbgcolor})
                    kwargs_off.update({new_key: activebgcolor})

        if kwargs_on:
            widget.bind("<Enter>", lambda _: widget.config(**kwargs_on))
            widget.bind("<Leave>", lambda _: widget.config(**kwargs_off))
    
    def parametres(self, **kwargs):
        type_widget = self.type_widget.lower()
        if type_widget not in cWidget.WIDGETS:        
            raise Exception(f"Le type de widget {self.type_widget} n'existe pas. Il faut saisir: Label, Text, ScrolledText, Combobox, etc...")
        extension_kwargs = self.filtrage_kwargs(type_widget, kwargs)
        widget = cWidget.WIDGETS[type_widget](master=self.parent, **kwargs)
        kwargs.update(extension_kwargs)
        self.check_params(widget, **kwargs)
        return widget


class Animation:
    PARAMETRES: tuple = ("start_x", "end_x", "start_y", "end_y")

    def __init__(self, parent, speed: float = 0.05, **params):
        msg: str = ""
        vitesse: float = speed
        for param in params:
            if param not in Animation.PARAMETRES:
                msg += f"{param}, "
        if msg:
            msg = f"Parametre(s) {msg[:-2]} inconnu(s)."

        if msg or len(params) != 2:
            msg += "Il faut preciser 2 parametres parmis:"
            msg += "\n- start_x et end_x"
            msg += "\n- start_y et end_y"
            raise Exception(msg)
            
        self.parent = parent
        self.at_start: bool = True
        self.start: float = params["start_y"] if params.get("start_x") is None else params["start_x"]
        self.end: float = params["end_y"] if params.get("end_x") is None else params["end_x"]
        self.position: float = self.start
        self.delta: float = -vitesse if self.start > self.end else vitesse
        self.horizontal: bool = params.get("start_y") is None

    def place(self, position):
        if self.horizontal:
            self.parent.place(relx=position)
        else:
            self.parent.place(rely=position)

    def reached_position(self, pos_to_reach):
        if self.delta > 0:
            return self.position + self.delta > pos_to_reach
        else:
            return self.position + self.delta < pos_to_reach

    def run(self, *args):
        dest = self.end if self.at_start else self.start
        if self.reached_position(dest):
            self.place(self.end if self.at_start else self.start)
            self.delta = -self.delta
            self.at_start = not self.at_start
        else:
            self.position += self.delta
            self.place(self.position)
            self.parent.after(5, self.run)


class cFrame(tk.Frame):
    def __init__(self, parent, type_layout: str = "pack", **kwargs) -> None:
        super_params: dict = {}
        key = "frame_params"
        if not kwargs.get(key) is None:
            super_params.update(kwargs.pop(key))
        
        super().__init__(master=parent, **super_params)

        default_kwargs: dict
        match type_layout.lower():
            case "pack":
                default_kwargs = {"expand": True, "fill": "both"}
                default_kwargs.update(kwargs)
                self.pack(**default_kwargs)

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
        check_kwargs(kwargs)
        new_widget = cWidget(self, type_widget)
        return new_widget.parametres(**kwargs)

    def set_animation(self, **params):
        self.animation = Animation(self, **params)

    def run_animation(self, *args):
        self.animation.run()


class App(tk.Tk):
    def __init__(self, title: str, size: tuple, position: tuple = (-1, -1), **options):
        # Main setup
        super().__init__()

        if not options.get("resizable", True):
            self.resizable(False, False)

        if not options.get("border", True):
            # Suppression des bords de fenetre
            self.overrideredirect(True)

        self.style = ttk.Style()
        self.style.theme_use("clam")
        # fprint(self.style.theme_names())

        # Recuperation de toutes les constances de tkinter
        self.constantes = cTKConstante()
        self.types = cTKType()
        self.title(title)
        
        # Centre la fenetre
        screen_size = self.get_screenSize()
        posx = (screen_size[0]//2 - size[0]//2) if position[0] == -1 else position[0]
        posy = screen_size[1]//2 - size[1]//2 if position[1] == -1 else position[1]
        
        # Centre l'affichage de la fenetre
        self.geometry(f"{size[0]}x{size[1]}+{posx}+{posy}")
        self.minsize(*size)

        # configuration de la touche Echappe pour sortir de l'application
        self.bind("<KeyPress>", self.escape_function)

    def get_screenSize(self) -> tuple:
        user32 = ctypes.windll.user32
        return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    
    def escape_function(self, param):
        if param.keycode == 27:
            self.close()

    def add_frame(self, type_layout: str = "pack", **kwargs) -> cFrame:
        new_frame = cFrame(self, type_layout, **kwargs)
        return new_frame
    
    def load_image(self, image_path: str):
        return tk.PhotoImage(file=image_path)

    def run(self):
        self.mainloop()

    def close(self):
        self.destroy()
        self.quit()


class Notification(App):
    OPTIONS: dict = {
        "show": False,
        "fg": "white",
        "bg": "#203040",
        "align": "left"
    }
    BG_COLOR: str = "#203040"
    FG_COLOR: str = "white"
    DELAY: int = 5000  # 5 sec
    SIZE: tuple = (360, 130)
    PADY: int = 10

    NOMBRE: int = 0
    INSTANCES: list = list()

    def __init__(self, titre, texte, **options):
        if self.get_last_instance_pos_y() < (Notification.PADY+Notification.SIZE[1]):
            raise Exception("Nombre trop important de notifications ouvertes")

        self.titre = titre
        self.texte = texte
        self.options = self.OPTIONS.copy()

        for option in options:
            if option.lower() not in self.options:
                msg: str = f"Option: -{option} inconnue\n"
                msg += "Valeurs autorisée: -"
                msg += ", -".join(Notification.OPTIONS)
                raise Exception(msg)

            else:
                self.options[option] = options[option]

        if self.options.get("show"):
            self.show()

    def add_line(self, frame, texte, fontsize):

        options: dict = self.options.copy()
        options["fontsize"] = fontsize

        # Rechercher le texte compris entre {}
        params: list = re.findall(r"\{(.*?)\=(.*?)\}", texte)
        for key, value in params:
            options[key] = value.lower()
            texte = texte.replace(f"{{{key}={value}}}", "")

        if options["align"] == "top":
            options["justify"] = "center"
        else:
            options["justify"] = options["align"]

        if options["align"] == "center":
            options["align"] = "top"

        frame.add_widget("label", 
            fg=options["fg"], 
            bg=options["bg"], 
            text=texte, 
            wraplength=Notification.SIZE[0] - 10,
            justify=options["justify"],
            font=(None, options["fontsize"])).pack(side=options["align"], fill="x")

        # Sauvegarde globale pour les prochaines lignes
        self.options.update(options)

    def get_full_height(self, root_frame):
        hauteur: int = 0
        for itemf in root_frame.children:
            frame = root_frame.children[itemf]
            if frame.widgetName == "frame":
                hauteur += self.get_full_height(frame)
            else:
                hauteur += frame.winfo_reqheight()

        return hauteur

    def get_last_instance_pos_y(self):
        if len(Notification.INSTANCES) > 0:
            return Notification.INSTANCES[-1].winfo_y()
        else:
            user32 = ctypes.windll.user32
            return user32.GetSystemMetrics(1) - 40

    def show(self):
        self.size: tuple = Notification.SIZE[:]
        width, height = self.size

        super().__init__(self.titre, 
            size=self.size, 
            border=False)

        with self.add_frame() as frame:

            frame.add_widget("label", 
                bg=self.options["bg"], 
                text="").place(x=0, y=0, relwidth=1, relheight=1)

            frame_titre = frame.add_frame("place", x=10, y=5, width=width-20, frame_params={"bg": self.options["bg"]})
            self.add_line(frame_titre, self.titre, 14)

            contenu = frame.add_frame("place", x=10, y=30, width=width-20)
            for idx, ligne_texte in enumerate(self.texte.split("\n")):
                if idx > 5:
                    break

                ligne = contenu.add_frame("pack", fill="x", frame_params={"bg": self.options["bg"]})
                self.add_line(ligne, ligne_texte, 10)

        real_height = self.get_full_height(frame)
        if real_height > height:
            height = real_height 
        geometry: str = f"{width}x{height}"
        geometry += f"+{self.winfo_screenwidth() - width - 10}"
        geometry += f"+{self.get_last_instance_pos_y() - height - Notification.PADY}"
        self.geometry(geometry)

        Notification.NOMBRE += 1
        Notification.INSTANCES.append(self)

        self.after(Notification.DELAY, self.fermer)
        self.screen_width = self.winfo_screenwidth()
        self.run()

    def fermer(self):
        taille, x, y = self.geometry().split('+')
        x = int(x) + 10
        if x < self.screen_width:
            self.geometry(f"{taille}+{x}+{y}")
            self.after(5, self.fermer)

        else:
            height = self.winfo_height()
            Notification.INSTANCES.remove(self)
            Notification.NOMBRE -= 1

            # descend les notifications restantes
            for idx, instance in enumerate(Notification.INSTANCES):
                taille, x, y = instance.geometry().split('+')
                instance.geometry(f"{taille}+{x}+{Notification.PADY+height+int(y)}")
            # Ferme la notification
            self.close()


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
                ).pack(side="left", expand=True, fill="y", pady=20)
            fg3.add_widget(
                "Scale", 
                orient="vertical"
                ).pack(side="left", expand=True, fill="y", pady=20)

        with frame_gauche.add_frame("place", rely=1, relwidth=1, height=60, anchor="sw") as fg4:
            with fg4.add_frame("pack") as fcbtn:
                cvaleur1 = tk.BooleanVar(value=True)
                fcbtn.add_widget(
                    "Checkbutton",
                    text="check 1", variable=cvaleur1, onvalue=True, offvalue=False
                    ).pack(side="left", expand=True, anchor="e", padx=20)

                cvaleur2 = tk.BooleanVar(value=True)
                fcbtn.add_widget(
                    "Checkbutton",
                    text="check 2", variable=cvaleur2, onvalue=True, offvalue=False
                    ).pack(side="left", expand=True, anchor="w", padx=20)
                fg4.add_widget(
                    "Entry"
                    ).pack(expand=True, fill="both", padx=20, pady=(5, 10))

    with app.add_frame("place", relx=0.3, relwidth=0.7, y=0, relheight=1) as frame_droite:
        with frame_droite.add_frame(expand=True, fill="both") as fd1:
            with fd1.add_frame(expand=True, fill="both") as fdp1:
                fdp1.add_widget(
                    "Label", 
                    text="Label3", 
                    background="#BB0000", activebackground="red", 
                    fg="white", activeforeground="yellow"
                    ).pack(side="left", expand=True, fill="both", padx=20, pady=(25, 5))

                fdp1.add_widget(
                    "Label", 
                    text="Label4", 
                    background="#0000BB", activebackground="blue", 
                    fg="white", activeforeground="cyan"
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
