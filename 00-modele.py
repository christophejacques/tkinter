from os import path


tkinter_classe = __import__("20-classes")
fprint = tkinter_classe.fprint
app = tkinter_classe.App(__file__.split(path.sep)[-1], (500, 300))


def main():
    app.maxsize(600, 400)
    color: str = "#303436"  # "#3D7476"
    with app.add_frame(frame_params={"bg": color}) as f1:
        message = "Appuyer sur la touche 'Echap' \npour fermer l'application\n"
        f1.add_widget("label", text=message, fg="white", bg=color, font=20).pack(expand=True)

    app.run()


if __name__ == "__main__":
    main()
