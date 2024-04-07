
from pathlib import Path
import os, platform
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

class MostraPrenotazioneApp:
    def __init__(self, window):
        
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
            262.0,
            140.0,
            599.0,
            380.0,
            fill="#56AAFF",
            outline="")

        self.canvas.create_text(
            315.0,
            163.0,
            anchor="nw",
            text="Tipologia camera selezionata",
            fill="#FFFFFF",
            font=("Inter Bold", 16 * -1)
        )
        
        self.canvas.create_text(
            378.0,
            222.0,
            anchor="nw",
            text="Prezzo totale",
            fill="#FFFFFF",
            font=("Inter Bold", 16 * -1)
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
            x=282.0,
            y=310.0,
            width=143.8626708984375,
            height=39.882110595703125
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
            x=435.86279296875,
            y=310.0,
            width=143.8626708984375,
            height=39.882110595703125
        )
        
        self.canvas.create_rectangle(
            302.0,
            184.0,
            559.0,
            216.0,
            fill="#FAFFFD",
            outline="")

        self.canvas.create_rectangle(
            302.0,
            242.0,
            559.0,
            274.0,
            fill="#FAFFFD",
            outline="")

        self.canvas.create_text(
            369.0,
            190.0,
            anchor="nw",
            text="Camera doppia",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.canvas.create_text(
            411.0,
            248.0,
            anchor="nw",
            text="700€",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )
        
    def relative_to_assets(self, path: str) -> Path:
        return ASSETS_PATH / Path(path)


if __name__ == "__main__":
    abs = os.getcwd()
    if(platform.system() == "Darwin"):
        ASSETS_PATH = abs + "/assets/frame6"
    else:
        ASSETS_PATH = abs + "/build/assets/frame6"
        
    root = Tk()
    app = MostraPrenotazioneApp(root)
    root.mainloop()