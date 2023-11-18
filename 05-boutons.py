import tkinter as tk
# import ttkbootstrap as ttk
from tkinter import ttk


def dprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)


def button_function():
    window.quit()


# window 
window = tk.Tk()
window.title("Tkinter Buttons")
window.geometry("400x300")


# ttk Buttons
button1 = ttk.Button(master=window, text="Button 1")
button1.pack(pady=10)

zone1 = tk.Frame(master=window)
zone1.pack(pady=10)

# CheckButtons
check_var1 = tk.BooleanVar(value=True)
check_var2 = tk.BooleanVar()

cbutton1 = ttk.Checkbutton(
    master=zone1, 
    text="check 1", 
    variable=check_var1,
    onvalue=True,
    offvalue=False,
    command = lambda: print(check_var1.get()))
cbutton1.pack()
cbutton2 = ttk.Checkbutton(
    master=zone1, 
    text="check 2", 
    variable=check_var2,
    command = lambda: print(check_var2.get()))
cbutton2.pack()

# RadioButtons
radio_var = tk.IntVar(value=1)
radio_zone1 = tk.Frame(master=window)
radio_zone1.pack(pady=10)

rbutton1 = ttk.Radiobutton(
    master=radio_zone1, 
    text="radio 1", 
    value=1, 
    variable=radio_var,
    command=lambda: print(radio_var.get()))
rbutton2 = ttk.Radiobutton(master=radio_zone1, text="radio 2", value=2, variable=radio_var,
    command=lambda: print(radio_var.get()))
rbutton3 = ttk.Radiobutton(master=radio_zone1, text="radio 3", value=3, variable=radio_var,
    command=lambda: print(radio_var.get()))
rbutton1.pack(side="left")
rbutton2.pack(side="left")
rbutton3.pack(side="left")

# RadioButtons
radio_var2 = tk.IntVar()
radio_zone2 = tk.Frame(master=window)
radio_zone2.pack()

rbutton4 = ttk.Radiobutton(master=radio_zone2, text="radio 4", value=4, 
    variable=radio_var2, command=lambda: print(radio_var2.get()))
rbutton5 = ttk.Radiobutton(master=radio_zone2, text="radio 5", value=5, 
    variable=radio_var2, command=lambda: print(radio_var2.get()))
rbutton6 = ttk.Radiobutton(master=radio_zone2, text="radio 6", value=6, 
    variable=radio_var2, command=lambda: print(radio_var2.get()))
rbutton4.pack(side="left")
rbutton5.pack(side="left")
rbutton6.pack(side="left")


# Run
window.mainloop()
