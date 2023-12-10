from os import path


saved_width: int = 0
maClasse = __import__("20-classes") 

app = maClasse.App(__file__.split(path.sep)[-1], (1000, 400))


def myCanvas():
    f1 = app.add_frame("pack", expand=True, fill="both")
    sf1 = f1.add_frame("pack", expand=True, fill="both")
    canvas = sf1.add_widget(
        "canvas", 
        background="gray", scrollregion=(0, 0, 1920, 1080))

    for x in range(1, 11):
        canvas.create_line(0, 0, x * 192, 1080)
        canvas.create_line(0, 1080, x * 192, 0)

    canvas.pack(side="left", expand=True, fill="both")

    sbx = f1.add_widget("scrollbar", orient="horizontal", command=canvas.xview)
    sby = sf1.add_widget("scrollbar", orient="vertical", command=canvas.yview)
    canvas.configure(xscrollcommand=sbx.set, yscrollcommand=sby.set)

    sbx.pack(side="bottom", fill="x", padx=(0, 17))
    sby.pack(side="right", fill="y")

    canvas.bind("<MouseWheel>", lambda event: canvas.yview_scroll(what="units", number=-event.delta//60))
    canvas.bind("<Control-MouseWheel>", lambda event: canvas.xview_scroll(what="units", number=-event.delta//60))


def myTreeView():
    with app.add_frame("pack", expand=True, fill="both") as f1:
        tv = f1.add_widget("treeview", show="headings", columns=(1,))
        tv.pack(side="left", expand=True, fill="both")
        sby = f1.add_widget("scrollbar", orient="vertical", command=tv.yview)
        f1.pack()
        
        tv.heading(0, text="Adresse EMail")
        sby.pack(side="left", fill="y")

        tv.configure(yscrollcommand=sby.set)

        for idx in range(100):
            tv.insert(
                parent="",
                # index=idx,  # tk.END,  # idx
                index=app.constantes.END,  
                values=(f"adresse{idx}@gmail.com"))


# myCanvas()
myTreeView()
app.run()
