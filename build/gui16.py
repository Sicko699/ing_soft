
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import os, platform

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


abs = os.getcwd()
if(platform.system() == "Darwin"):
    ASSETS_PATH = abs + "/assets/frame4"
else:
    ASSETS_PATH = abs + "/build/assets/frame4"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("862x519")
window.configure(bg = "#FAFFFD")


canvas = Canvas(
    window,
    bg = "#FAFFFD",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    210.0,
    519.0,
    fill="#3E97F1",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=46.0,
    y=452.0,
    width=47.0,
    height=45.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=116.0,
    y=452.0,
    width=47.0,
    height=45.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=24.0,
    y=75.0,
    width=162.0,
    height=45.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=24.0,
    y=135.0,
    width=162.0,
    height=45.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=24.0,
    y=195.0,
    width=162.0,
    height=45.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=24.0,
    y=255.0,
    width=162.0,
    height=45.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=24.0,
    y=315.0,
    width=162.0,
    height=45.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=24.0,
    y=375.0,
    width=162.0,
    height=45.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=295.0,
    y=78.0,
    width=212.0,
    height=20.0
)

canvas.create_rectangle(
    344.0,
    110.0,
    734.0,
    410.0,
    fill="#FAFFFD",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    539.0,
    185.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#EAEEEC",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=401.0,
    y=166.0,
    width=276.0,
    height=37.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    539.0,
    260.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#EAEEEC",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=401.0,
    y=241.0,
    width=276.0,
    height=36.0
)

canvas.create_text(
    389.0,
    146.0,
    anchor="nw",
    text="Nome servio",
    fill="#000000",
    font=("Quicksand Medium", 16 * -1)
)

canvas.create_text(
    389.0,
    221.0,
    anchor="nw",
    text="Camera",
    fill="#000000",
    font=("Quicksand Medium", 16 * -1)
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=445.0,
    y=315.0,
    width=187.0,
    height=49.0
)
window.resizable(False, False)
window.mainloop()
