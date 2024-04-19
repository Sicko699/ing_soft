
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/francescomattone/Desktop/coding/ing_soft2/build/assets/frame20")


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
    262.0,
    91.0,
    599.0,
    399.0,
    fill="#56AAFF",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    430.5,
    161.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FAFFFD",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=314.0,
    y=145.0,
    width=233.0,
    height=30.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    430.5,
    223.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FAFFFD",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=314.0,
    y=207.0,
    width=233.0,
    height=30.0
)

canvas.create_text(
    302.0,
    124.0,
    anchor="nw",
    text="Data di arrivo",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    430.5,
    286.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FAFFFD",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=314.0,
    y=270.0,
    width=233.0,
    height=30.0
)

canvas.create_text(
    302.0,
    249.0,
    anchor="nw",
    text="Tipologia camera",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    302.0,
    187.0,
    anchor="nw",
    text="Data di partenza",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

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
    x=359.0,
    y=333.0,
    width=143.8626708984375,
    height=39.882110595703125
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
    x=27.0,
    y=21.0,
    width=47.0,
    height=45.0
)
window.resizable(False, False)
window.mainloop()
