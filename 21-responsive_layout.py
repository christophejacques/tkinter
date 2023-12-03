from os import path


saved_width: int = 0
maClasse = __import__("20-classes") 
App = getattr(maClasse, "App")

app = maClasse.App(__file__.split(path.sep)[-1], (200, 400), (300, 200))
app.maxsize(1000, 400)

f1 = app.add_frame("pack", expand=True, fill="both")
f2 = app.add_frame("pack", expand=True, fill="both")

l1 = f1.add_widget("label", text="Label 1", background="yellow")
l2 = f1.add_widget("label", text="Label 2", background="orange")

l3 = f2.add_widget("label", text="Label 3", background="red")
l4 = f2.add_widget("label", text="Label 4", background="grey")


def forget_app_layout() -> None:
    [frame.pack_forget() for frame in (f1, f2)]
    [label.pack_forget() for label in (l1, l2, l3, l4)]


def frame_200() -> None:
    forget_app_layout()
    l1.pack(side="top", expand=True, fill="both", padx=10, pady=(10, 5))
    l2.pack(side="top", expand=True, fill="both", padx=10, pady=5)
    l3.pack(side="top", expand=True, fill="both", padx=10, pady=5)
    l4.pack(side="top", expand=True, fill="both", padx=10, pady=(5, 10))

    f1.pack(side="top", expand=True, fill="both")
    f2.pack(side="top", expand=True, fill="both")


def frame_400() -> None:
    forget_app_layout()
    l1.pack(side="left", expand=True, fill="both", padx=(10, 5), pady=(10, 5))
    l2.pack(side="left", expand=True, fill="both", padx=(5, 10), pady=(10, 5))
    l3.pack(side="left", expand=True, fill="both", padx=(10, 5), pady=(5, 10))
    l4.pack(side="left", expand=True, fill="both", padx=(5, 10), pady=(5, 10))

    f1.pack(side="top", expand=True, fill="both")
    f2.pack(side="top", expand=True, fill="both")


def frame_600() -> None:
    forget_app_layout()
    l1.pack(side="left", expand=True, fill="both", padx=(10, 5), pady=10)
    l2.pack(side="left", expand=True, fill="both", padx=5, pady=10)
    l3.pack(side="left", expand=True, fill="both", padx=5, pady=10)
    l4.pack(side="left", expand=True, fill="both", padx=(5, 10), pady=10)

    f1.pack(side="left", expand=True, fill="both")
    f2.pack(side="left", expand=True, fill="both")


def app_resize(event) -> None:
    global saved_width

    if event.widget.__class__.__name__ == "App":
        actual_width: int = event.width

        if actual_width < 400:
            actual_width = 200
        elif actual_width < 600:
            actual_width = 400
        else:
            actual_width = 600

        if actual_width != saved_width:
            saved_width = actual_width
            {
                200: frame_200,
                400: frame_400,
                600: frame_600
            }[saved_width]()


app.bind("<Configure>", app_resize)

app.run()
