
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import os
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

class RegisterApp:
    def __init__(self, window):
        self.window = window
        self.window.geometry("862x519")
        self.window.configure(bg = "#FAFFFD")
        
        



abs = os.getcwd()
ASSETS_PATH = abs + "/assets/frame4"


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
    26.0,
    599.0,
    494.0,
    fill="#56AAFF",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    430.5,
    96.0,
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
    y=80.0,
    width=233.0,
    height=30.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    430.5,
    158.0,
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
    y=142.0,
    width=233.0,
    height=30.0
)

canvas.create_text(
    302.0,
    59.0,
    anchor="nw",
    text="Nome",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    302.0,
    122.0,
    anchor="nw",
    text="Cognome",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    430.5,
    221.0,
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
    y=205.0,
    width=233.0,
    height=30.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    430.5,
    283.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FAFFFD",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=314.0,
    y=267.0,
    width=233.0,
    height=30.0
)

canvas.create_text(
    302.0,
    184.0,
    anchor="nw",
    text="Email",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    302.0,
    247.0,
    anchor="nw",
    text="Numero di telefono",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    430.5,
    346.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FAFFFD",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=314.0,
    y=330.0,
    width=233.0,
    height=30.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    430.5,
    408.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FAFFFD",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=314.0,
    y=392.0,
    width=233.0,
    height=30.0
)

canvas.create_text(
    302.0,
    309.0,
    anchor="nw",
    text="Username",
    fill="#FFFFFF",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    302.0,
    372.0,
    anchor="nw",
    text="Password",
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
    y=443.0,
    width=143.8626708984375,
    height=39.882110595703125
)
window.resizable(False, False)
window.mainloop()
