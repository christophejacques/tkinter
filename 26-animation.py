from os import path


tkinter_classe = __import__("20-classes")
fprint = tkinter_classe.fprint
app = tkinter_classe.App(__file__.split(path.sep)[-1], (500, 300))


def slide_frame(frame, btn, posx, deltax):

    def exec(*args):
        lpanel: bool = "left" in btn.cget("text").lower()
        dirx = deltax.get()
        i = posx.get()
        if any([not lpanel and ((i > 0.70 and dirx < 0) or (i < 1+dirx and dirx > 0)),
                lpanel and ((i > -0.3+dirx and dirx < 0) or (i < dirx and dirx > 0))]):
            posx.set(round(i + dirx, 2))
            frame.place(relx=i, anchor="nw")
            frame.after(4, exec)
        else:
            deltax.set(-dirx)
            frame.bind("<Leave>", slide_frame(frame, btn, posx, deltax))

    def checking(*args):
        frame.unbind("<Leave>")
        exec(*args)

    return checking


def main():
    app.maxsize(600, 400)

    with app.add_frame("place", relwidth=1, relheight=1) as f1:
        btnl = f1.add_widget("label", text="Left Params", width=18, bg="white")
        btnl.place(anchor="nw")
        
        btnr = f1.add_widget("label", text=" Outline ", width=18, bg="white")
        btnr.place(relx=1, anchor="ne")
        
        lposx = app.types.DoubleVar(value=-0.3)
        deltalx = app.types.DoubleVar(value=0.01)
        with f1.add_frame("place", relx=lposx.get(), y=0, relheight=1, relwidth=0.3, anchor="ne") as sf1:
            sf1.add_widget("label", text="Left panel 1", background="red").pack(expand=True, fill="both")
            sf1.add_widget("label", text="Left panel 2", background="yellow").pack(expand=True, fill="both")

        rposx = app.types.DoubleVar(value=1)
        deltarx = app.types.DoubleVar(value=-0.01)
        with f1.add_frame("place", relx=rposx.get(), y=0, relheight=1, relwidth=0.3, anchor="nw") as sf2:
            sf2.add_widget("label", text="right panel 1", background="pink").pack(expand=True, fill="both")
            sf2.add_widget("label", text="right panel 2", background="orange").pack(expand=True, fill="both")

        btnl.bind("<Enter>", slide_frame(sf1, btnl, lposx, deltalx))
        btnr.bind("<Enter>", slide_frame(sf2, btnr, rposx, deltarx))

        sf1.bind("<Leave>", slide_frame(sf1, btnl, lposx, deltalx))
        sf2.bind("<Leave>", slide_frame(sf2, btnr, rposx, deltarx))

    app.run()


if __name__ == "__main__":
    main()
