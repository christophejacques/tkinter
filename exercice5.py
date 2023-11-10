import tkinter as tk
# import ttkbootstrap as ttk
from tkinter import ttk


def dprint(*args, **kwargs):
    print(*args, **kwargs, flush=True)


def button_function():
    window.quit()


# window = tk.Tk()
window = tk.Tk()
window.title("Tkinter Buttons")
window.geometry("400x300")


# ttk Buttons
button1 = ttk.Button(master=window, text="Button 1")
button1.pack(pady=10)

zone1 = tk.Frame(master=window)
zone1.pack(pady=10)

check_var1 = tk.StringVar()
check_var2 = tk.StringVar()

cbutton1 = ttk.Checkbutton(
    master=zone1, 
    text="check 1", 
    variable=check_var1,
    command = lambda: print(check_var1.get()))
cbutton1.pack()
cbutton2 = ttk.Checkbutton(
    master=zone1, 
    text="check 2", 
    variable=check_var2,
    command = lambda: print(check_var2.get()))
    
cbutton2.pack()

rbutton1 = ttk.Radiobutton(master=window, text="radio 1", value=1)
rbutton2 = ttk.Radiobutton(master=window, text="radio 2", value=2)
rbutton1.pack()
rbutton2.pack()


# Run
window.mainloop()
