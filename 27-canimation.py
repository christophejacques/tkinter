from os import path


tkinter_classe = __import__("20-classes")
fprint = tkinter_classe.fprint
app = tkinter_classe.App(__file__.split(path.sep)[-1], (500, 300))


def quit(*args):
    app.destroy()
    app.quit()


app.title("Test")
app.geometry("500x300")
app.maxsize(600, 400)

with app.add_frame() as frame:
    with frame.add_frame("place", relx=0, relwidth=0.35, rely=-1, relheight=0.96) as sfl:
        sfl.set_animation(start_y=-1, end_y=0.03, speed=0.04)

        sfl.add_widget("label", text="Label 1", bg="orange").pack(expand=True, fill="both")
        sfl.add_widget("label", text="Label 2", bg="yellow").pack(expand=True, fill="both")

        boutons = sfl.add_frame(expand=False, frame_params={"bg": "#6DA2A7"})
        boutons.add_widget("button", 
            text="Annuler",
            command=sfl.run_animation).pack(side="left", expand=True, padx=2, pady=5)
        boutons.add_widget("button", 
            text="Valider", 
            command=sfl.run_animation).pack(side="right", expand=True, padx=2, pady=5)

    with frame.add_frame("place", relx=1, relwidth=0.35, rely=0.02, relheight=0.96) as sfr:
        sfr.set_animation(start_x=1, end_x=0.65, speed=0.02)

        sfr.add_widget("label", text="Label 1", bg="orange").pack(expand=True, fill="both")
        sfr.add_widget("label", text="Label 2", bg="yellow").pack(expand=True, fill="both")

        boutons = sfr.add_frame(expand=False, frame_params={"bg": "#6DA2A7"})
        boutons.add_widget("button", 
            text="Annuler",
            command=sfr.run_animation).pack(side="left", expand=True, padx=2, pady=5)
        boutons.add_widget("button", 
            text="Valider", 
            command=sfr.run_animation).pack(side="right", expand=True, padx=2, pady=5)

    btnl = frame.add_widget("Button", text=" Parametres ", command=sfl.run_animation)
    btnl.place(relx=0.5, rely=0.4, anchor="center")
    btnr = frame.add_widget("Button", text=" OutLine ", command=sfr.run_animation)
    btnr.place(relx=0.5, rely=0.6, anchor="center")


app.run()
