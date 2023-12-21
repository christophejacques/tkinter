import re
import ctypes
from os import path
from random import randint


tkinter_classe = __import__("20-classes")
fprint = tkinter_classe.fprint
App: type = tkinter_classe.App


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


app = App(__file__.split(path.sep)[-1], (500, 300))


def notif():
    message: str = "{align=left}Premiere ligne de texte\n{fg=green}Suite"
    for ligne in range(randint(1, 4)):
        message += f"\nligne numero {ligne}"

    Notification("{align=center}{fg=white}Titre de la notif", 
        message,
        bg="#101010", fg="#A0A0A0",
        show=True)


frame = app.add_frame()
frame.add_widget("button", text="deplacement", command=notif).pack(expand=True)

app.run()
fprint("Fin")
