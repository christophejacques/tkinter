from os import path


tkinter_classe = __import__("20-classes")
fprint = tkinter_classe.fprint
app = tkinter_classe.App(__file__.split(path.sep)[-1], (500, 300))


def main():
    app.maxsize(600, 400)
    with app.add_frame() as f1:
        img = app.load_image("DMP.PNG")
        f1.add_widget("label", image=img).pack(pady=10)

    app.run()


if __name__ == "__main__":
    main()
