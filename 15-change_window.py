import tkinter as tk
from tkinter import ttk


def dprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)

def button_function(valeur):
    def fonction():
        dprint(valeur.get())
    return fonction

# window 
window = tk.Tk()
window.title("Changing Window")
# window.geometry("600x400")

def bind_function(param):
    if param.keycode == 27:
        window.quit()
window.bind("<KeyPress>", bind_function)

mwidth = window.winfo_screenwidth()//2
mheight = window.winfo_screenheight()//2
wwidth = 1440
wheight = 800
mwwidth = wwidth//2
mwheight = wheight//2


# Changing Window
# window.geometry("600x400+1115+20")
window.geometry(f"{wwidth}x{wheight}+{mwidth-mwwidth}+{mheight-mwheight}")
window.iconbitmap("python.ico")

# window sizes
# window.minsize(500, 350)
# window.maxsize(800, 600)
window.resizable(True, True)

# screen attributes
# print(window.winfo_screenwidth())
# print(window.winfo_screenheight())

# window attributes
# print(window.winfo_width())
# print(window.winfo_height())

# window.attributes("-alpha", 0.5)
# window.attributes("-topmost", True)

# window.attributes("-disable", True)
# window.attributes("-fullscreen", True)

# title bar
# window.title("Hello")
# window.overrideredirect(True)
# grip = ttk.Sizegrip(master=window)
# grip.place(relx=1, rely=1, anchor="se")

# Run
window.mainloop()

