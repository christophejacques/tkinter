import tkinter as tk
from tkinter import ttk, scrolledtext
import ctypes


def dprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)


# Classes

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

        # widgets
        self.frames: list = list()

    def get_screenSize(self) -> tuple:
        user32 = ctypes.windll.user32
        return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    
    def escape_function(self, param):
        if param.keycode == 27:
            self.destroy()
            self.quit()

    def add_frame(self, type_layout: str = "pack", **kwargs):
        new_frame = cFrame(self, type_layout, **kwargs)
        self.frames.append(new_frame)
        return new_frame
    
    def run(self):
        self.mainloop()


class cFrame(ttk.Frame):
    def __init__(self, parent, type_layout: str = "pack", **kwargs) -> None:
        super().__init__(master=parent)
        current_widget = None

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
        # print("enter:", args)
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        # print("exit:", exc_type, exc_value)
        pass

    def add_frame(self, type_layout: str = "pack", **kwargs):
        new_frame = cFrame(self, type_layout, **kwargs)
        return new_frame
    
    def add_widget(self, type_widget: str, **kwargs):
        # print("add_widget:", type_widget, kwargs)
        match type_widget.lower():
            case "label":
                return ttk.Label(master=self, **kwargs)
            case "button":
                return ttk.Button(master=self, **kwargs)
            case "entry":
                return ttk.Entry(master=self, **kwargs)
            
            case "text":
                return ttk.Entry(master=self, **kwargs)
            case "scrolledtext":
                return scrolledtext.ScrolledText(master=self, **kwargs)
            case "scrollbar":
                return scrolledtext.Scrollbar(master=self, **kwargs)
            
            case "checkbutton":
                return ttk.Checkbutton(master=self, **kwargs)
            case "radiobutton":
                return ttk.Radiobutton(master=self, **kwargs)
            
            case "combobox":
                return ttk.Combobox(master=self, **kwargs)
            case "spinbox":
                return ttk.Spinbox(master=self, **kwargs)
            
            case "progressbar":
                return ttk.Progressbar(master=self, **kwargs)
            case "scale":
                return ttk.Entry(master=self, **kwargs)
            
            case _:
                raise Exception(f"Le type de widget {type_widget} n'existe pas. Il faut saisir: Label, Text, ScrolledText, Combobox, etc...")
                            

app = App("Demo de la classe", (1440, 750))
with app.add_frame("place", x=0, relwidth=0.3, y=0, relheight=1) as frame_gauche:
    w1 = frame_gauche.add_widget("Label", text="Label1", background="orange")
    w1.pack(expand=True, fill="both")

with app.add_frame("place", relx=0.3, relwidth=0.7, y=0, relheight=1) as frame_droite:
    with frame_droite.add_frame(expand=True, fill="both") as fd1:
        w2 = fd1.add_widget("Label", text="Label2", background="green")
        w2.pack(expand=True, fill="both")

    with frame_droite.add_frame(expand=True, fill="both") as fd2:
        w3 = fd2.add_widget("Label", text="Label3", background="red")
        w3.pack(expand=True, fill="both")


app.run()
