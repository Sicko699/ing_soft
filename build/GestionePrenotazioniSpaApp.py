from pathlib import Path
import os, platform
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

class GestionePrenotazioniSpa:
    def __init__(self,window):
        self.window = window
        self.window.geometry("862x519")
        self.window.configure(bg = "#FAFFFD")

        self.canvas = Canvas(
            self.window,
            bg = "#FAFFFD",
            height = 519,
            width = 862,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            210.0,
            519.0,
            fill="#3E97F1",
            outline=""
        )

        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(
            x=46.0,
            y=452.0,
            width=47.0,
            height=45.0
        )

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=116.0,
            y=452.0,
            width=47.0,
            height=45.0
        )

        self.button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_3.place(
            x=24.0,
            y=75.0,
            width=162.0,
            height=45.0
        )

        self.button_image_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.button_4.place(
            x=24.0,
            y=135.0,
            width=162.0,
            height=45.0
        )

        self.button_image_5 = PhotoImage(file=self.relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        self.button_5.place(
            x=24.0,
            y=195.0,
            width=162.0,
            height=45.0
        )

        self.button_image_6 = PhotoImage(file=self.relative_to_assets("button_6.png"))
        self.button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        self.button_6.place(
            x=24.0,
            y=255.0,
            width=162.0,
            height=45.0
        )

        self.button_image_7 = PhotoImage(file=self.relative_to_assets("button_7.png"))
        self.button_7 = Button(
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_7 clicked"),
            relief="flat"
        )
        self.button_7.place(
            x=24.0,
            y=315.0,
            width=162.0,
            height=45.0
        )

        self.button_image_8 = PhotoImage(file=self.relative_to_assets("button_8.png"))
        self.button_8 = Button(
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_8 clicked"),
            relief="flat"
        )
        self.button_8.place(
            x=24.0,
            y=375.0,
            width=162.0,
            height=45.0
        )

        self.canvas.create_rectangle(
            315.0,
            25.0,
            752.0,
            494.0,
            fill="#FAFFFD",
            outline=""
        )

        self.button_image_10 = PhotoImage(file=self.relative_to_assets("button_10.png"))
        self.button_10 = Button(
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_10 clicked"),
            relief="flat"
        )
        self.button_10.place(
            x=410.0,
            y=416.0,
            width=247.0,
            height=49.0
        )

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            533.5,
            72.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=352.0,
            y=53.0,
            width=363.0,
            height=36.0
        )

        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            533.5,
            122.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=352.0,
            y=103.0,
            width=363.0,
            height=36.0
        )

        self.button_image_11 = PhotoImage(file=self.relative_to_assets("button_11.png"))
        self.button_11 = Button(
            image=self.button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_11 clicked"),
            relief="flat"
        )
        self.button_11.place(
            x=649.0,
            y=108.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_12 = PhotoImage(file=self.relative_to_assets("button_12.png"))
        self.button_12 = Button(
            image=self.button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_12 clicked"),
            relief="flat"
        )
        self.button_12.place(
            x=649.0,
            y=58.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.entry_image_3 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            533.5,
            172.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_3.place(
            x=352.0,
            y=153.0,
            width=363.0,
            height=36.0
        )

        self.button_image_13 = PhotoImage(file=self.relative_to_assets("button_13.png"))
        self.button_13 = Button(
            image=self.button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_13 clicked"),
            relief="flat"
        )
        self.button_13.place(
            x=649.0,
            y=158.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.entry_image_4 = PhotoImage(file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            533.5,
            222.0,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_4.place(
            x=352.0,
            y=203.0,
            width=363.0,
            height=36.0
        )

        self.entry_image_5 = PhotoImage(file=self.relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            533.5,
            272.0,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_5.place(
            x=352.0,
            y=253.0,
            width=363.0,
            height=36.0
        )

        self.entry_image_6 = PhotoImage(file=self.relative_to_assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(
            533.5,
            322.0,
            image=self.entry_image_6
        )
        self.entry_6 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_6.place(
            x=352.0,
            y=303.0,
            width=363.0,
            height=36.0
        )

        self.button_image_14 = PhotoImage(file=self.relative_to_assets("button_14.png"))
        self.button_14 = Button(
            image=self.button_image_14,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_14 clicked"),
            relief="flat"
        )
        self.button_14.place(
            x=649.0,
            y=308.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.entry_image_7 = PhotoImage(file=self.relative_to_assets("entry_7.png"))
        self.entry_bg_7 = self.canvas.create_image(
            533.5,
            372.0,
            image=self.entry_image_7
        )
        self.entry_7 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_7.place(
            x=352.0,
            y=353.0,
            width=363.0,
            height=36.0
        )

        self.button_image_15 = PhotoImage(file=self.relative_to_assets("button_15.png"))
        self.button_15 = Button(
            image=self.button_image_15,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_15 clicked"),
            relief="flat"
        )
        self.button_15.place(
            x=684.0,
            y=58.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_16 = PhotoImage(file=self.relative_to_assets("button_16.png"))
        self.button_16 = Button(
            image=self.button_image_16,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_16 clicked"),
            relief="flat"
        )
        self.button_16.place(
            x=684.0,
            y=208.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_17 = PhotoImage(file=self.relative_to_assets("button_17.png"))
        self.button_17 = Button(
            image=self.button_image_17,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_17 clicked"),
            relief="flat"
        )
        self.button_17.place(
            x=684.0,
            y=158.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_18 = PhotoImage(file=self.relative_to_assets("button_18.png"))
        self.button_18 = Button(
            image=self.button_image_18,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_18 clicked"),
            relief="flat"
        )
        self.button_18.place(
            x=684.0,
            y=108.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_19 = PhotoImage(file=self.relative_to_assets("button_19.png"))
        self.button_19 = Button(
            image=self.button_image_19,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_19 clicked"),
            relief="flat"
        )
        self.button_19.place(
            x=684.0,
            y=258.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_20 = PhotoImage(file=self.relative_to_assets("button_20.png"))
        self.button_20 = Button(
            image=self.button_image_20,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_20 clicked"),
            relief="flat"
        )
        self.button_20.place(
            x=684.0,
            y=308.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_21 = PhotoImage(file=self.relative_to_assets("button_21.png"))
        self.button_21 = Button(
            image=self.button_image_21,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_21 clicked"),
            relief="flat"
        )
        self.button_21.place(
            x=684.0,
            y=358.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_22 = PhotoImage(file=self.relative_to_assets("button_22.png"))
        self.button_22 = Button(
            image=self.button_image_22,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_22 clicked"),
            relief="flat"
        )
        self.button_22.place(
            x=649.0,
            y=358.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_23 = PhotoImage(file=self.relative_to_assets("button_23.png"))
        self.button_23 = Button(
            image=self.button_image_23,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_23 clicked"),
            relief="flat"
        )
        self.button_23.place(
            x=649.0,
            y=208.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_24 = PhotoImage(file=self.relative_to_assets("button_24.png"))
        self.button_24 = Button(
            image=self.button_image_24,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_24 clicked"),
            relief="flat"
        )
        self.button_24.place(
            x=649.0,
            y=258.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

    def relative_to_assets(self,path: str) -> Path:
        return ASSETS_PATH / Path(path)

if __name__ == "__main__":
    abs = os.getcwd()
    if(platform.system() == "Darwin"):
        ASSETS_PATH = abs + "/assets/frame11"
    else:
        ASSETS_PATH = abs + "/build/assets/frame11"
    root = Tk()
    app = GestionePrenotazioniSpa(root)
    root.mainloop()