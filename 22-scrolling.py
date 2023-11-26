from os import path


saved_width: int = 0
maClasse = __import__("20-classes") 
App = getattr(maClasse, "App")

app = maClasse.App(__file__.split(path.sep)[-1], (1000, 400))

f1 = app.add_frame("pack", expand=True, fill="both")
sf1 = f1.add_frame("pack", expand=True, fill="both")
canvas = sf1.add_widget(
    "canvas", 
    background="yellow", scrollregion=(0, 0, 1920, 1080))

for x in range(1, 11):
    canvas.create_line(0, 0, x * 192, 1080)
    canvas.create_line(0, 1080, x * 192, 0)

canvas.pack(side="left", expand=True, fill="both")

sbx = f1.add_widget("scrollbar", orient="horizontal", command=canvas.xview)
sby = sf1.add_widget("scrollbar", orient="vertical", command=canvas.yview)
canvas.configure(xscrollcommand=sbx.set, yscrollcommand=sby.set)
# sbx.place(relx=0, rely=1, relwidth=1, anchor="sw")
# sby.place(relx=1, rely=0, relheight=1, anchor="ne")
sbx.pack(side="bottom", fill="x", padx=(0, 17))
sby.pack(side="right", fill="y")

canvas.bind("<MouseWheel>", lambda event: canvas.yview_scroll(what="units", number=-event.delta//60))

app.run()
