
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import os, platform

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


abs = os.getcwd()
if(platform.system() == "Darwin"):
    ASSETS_PATH = abs + "/assets/frame7"
else:
    ASSETS_PATH = abs + "/build/assets/frame7"



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
    x=326.0,
    y=53.0,
    width=190.0,
    height=67.0
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
    x=556.0,
    y=53.0,
    width=190.0,
    height=67.0
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
    y=135.0,
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
    y=195.0,
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
    y=255.0,
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
    x=24.0,
    y=315.0,
    width=162.0,
    height=45.0
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
    x=24.0,
    y=375.0,
    width=162.0,
    height=45.0
)

canvas.create_rectangle(
    316.0,
    170.0,
    756.0,
    420.0,
    fill="#FAFFFD",
    outline="")

canvas.create_rectangle(
    316.0,
    170.0,
    756.0,
    201.0,
    fill="#56AAFF",
    outline="")

canvas.create_text(
    506.0,
    173.0,
    anchor="nw",
    text="Report",
    fill="#FFFFFF",
    font=("Quicksand Medium", 18 * -1)
)

canvas.create_rectangle(
    356.0,
    227.2998046875,
    516.0,
    297.2998046875,
    fill="#6D6D6D",
    outline="")

canvas.create_rectangle(
    356.0,
    322.2998046875,
    516.0,
    392.2998046875,
    fill="#6D6D6D",
    outline="")

canvas.create_rectangle(
    556.0,
    227.0,
    716.0,
    297.0,
    fill="#6D6D6D",
    outline="")

canvas.create_rectangle(
    556.0,
    322.0,
    716.0,
    392.0,
    fill="#6D6D6D",
    outline="")

canvas.create_text(
    408.0,
    232.29998779296875,
    anchor="nw",
    text="Singole",
    fill="#000000",
    font=("Quicksand Medium", 16 * -1)
)

canvas.create_text(
    595.0,
    327.29998779296875,
    anchor="nw",
    text="Quadruple",
    fill="#000000",
    font=("Quicksand Medium", 16 * -1)
)

canvas.create_text(
    414.0,
    327.29998779296875,
    anchor="nw",
    text="Triple",
    fill="#000000",
    font=("Quicksand Medium", 16 * -1)
)

canvas.create_text(
    608.0,
    232.0,
    anchor="nw",
    text="Doppie",
    fill="#000000",
    font=("Quicksand Medium", 16 * -1)
)

canvas.create_text(
    410.0,
    262.29998779296875,
    anchor="nw",
    text="19 / 20",
    fill="#000000",
    font=("Quicksand Medium", 16 * -1)
)

canvas.create_text(
    412.0,
    357.29998779296875,
    anchor="nw",
    text="9 / 20",
    fill="#000000",
    font=("Quicksand Medium", 16 * -1)
)

canvas.create_text(
    610.0,
    262.0,
    anchor="nw",
    text="14 / 20",
    fill="#000000",
    font=("Quicksand Medium", 16 * -1)
)

canvas.create_text(
    610.0,
    357.29998779296875,
    anchor="nw",
    text="11 / 20",
    fill="#000000",
    font=("Quicksand Medium", 16 * -1)
)
window.resizable(False, False)
window.mainloop()
