import tkinter as tk
from tkinter import ttk


def dprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)


# window 
window = tk.Tk()
window.title("Toggling widget")
window.geometry("1440x750+200+50")
window.minsize(800, 400)
window.maxsize(1600, 800)


def bind_function(param):
    if param.keycode == 27:
        window.destroy()
        window.quit()


window.bind("<KeyPress>", bind_function)

# Toggling widget
frame_gauche = ttk.Frame(master=window)
frame_droite = ttk.Frame(master=window)
frame_gauche.place(x=0, relwidth=0.3, y=0, relheight=1)
frame_droite.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)

frame_gp1 = ttk.Frame(master=frame_gauche)
frame_gp2 = ttk.Frame(master=frame_gauche)
frame_gp3 = ttk.Frame(master=frame_gauche)
frame_gp4 = ttk.Frame(master=frame_gauche)

frame_gp1.place(y=0, relwidth=1, height=100)
frame_gp2.place(y=100, relwidth=1, height=100)
frame_gp3.place(y=200, relwidth=1)

frame_gp4.place(rely=1, relwidth=1, height=50, anchor="sw")


btn1 = ttk.Button(master=frame_gp1, text="Bouton1")
btn1.pack(side="left", expand=True, fill="both", padx=(2, 1), pady=2)

btn2 = ttk.Button(master=frame_gp1, text="Bouton2")
btn2.pack(side="right", expand=True, fill="both", padx=(1, 2), pady=2)

btn3 = ttk.Button(master=frame_gp2, text="Bouton3")
btn3.pack(side="top", expand=True, fill="both", padx=2, pady=2)

slider1 = ttk.Scale(master=frame_gp3, orient="vertical", length=400)
slider2 = ttk.Scale(master=frame_gp3, orient="vertical")

slider1.pack(side="left", expand=True, fill="both", pady=20)
slider2.pack(side="right", expand=True, fill="both", pady=20)

frame_cbutton = ttk.Frame(master=frame_gp4)
frame_cbutton.pack()
frame_gtext = ttk.Frame(master=frame_gp4)
frame_gtext.pack(expand=True, fill="both")


cvaleur1 = tk.BooleanVar(value=True)
cbutton1 = ttk.Checkbutton(
    master=frame_cbutton, 
    text="check 1", 
    variable=cvaleur1,
    onvalue=True,
    offvalue=False)
cbutton1.pack(side="left")

cvaleur2 = tk.BooleanVar(value=True)
cbutton2 = ttk.Checkbutton(
    master=frame_cbutton, 
    text="check 2", 
    variable=cvaleur2,
    onvalue=True,
    offvalue=False)
cbutton2.pack(side="right")

label1 = ttk.Label(master=frame_gtext, text="", background="white")
label1.pack(side="bottom", expand=True, fill="both", padx=20, pady=(5, 10))


frame_dp1 = ttk.Frame(master=frame_droite)
frame_dp2 = ttk.Frame(master=frame_droite)
frame_dp1.pack(expand=True, fill="both")
frame_dp2.pack(expand=True, fill="both")

label3 = ttk.Label(master=frame_dp1, text="Label 3", background="red")
label3.pack(side="left", expand=True, fill="both", padx=20, pady=(25, 5))
label4 = ttk.Label(master=frame_dp1, text="Label 4", background="blue")
label4.pack(side="right", expand=True, fill="both", padx=20, pady=(25, 5))


btn4 = ttk.Button(master=frame_dp2, text="bouton1")
btn4.pack(side="left", expand=True, fill="both", padx=20, pady=(5, 25))

btn5 = ttk.Button(master=frame_dp2, text="bouton2")
btn5.pack(side="right", expand=True, fill="both", padx=20, pady=(5, 25))


# # Pack
# frame.pack(side="top", expand=True, fill="both")
# label1.pack(expand=True, fill="both")
# bouton1.pack(side="top")


# Run
window.mainloop()
