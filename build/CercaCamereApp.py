from pathlib import Path
import os, platform
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

abs_path = os.getcwd()
if platform.system() == "Darwin":
    ASSETS_PATH = abs_path + "/assets/frame5"
else:
    ASSETS_PATH = abs_path + "/build/assets/frame5"

class CercaCamereApp:
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
            262.0,
            106.0,
            599.0,
            414.0,
            fill="#56AAFF",
            outline=""
        )

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            430.5,
            176.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FAFFFD",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=314.0,
            y=160.0,
            width=233.0,
            height=30.0
        )

        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            430.5,
            238.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#FAFFFD",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=314.0,
            y=222.0,
            width=233.0,
            height=30.0
        )

        self.canvas.create_text(
            302.0,
            139.0,
            anchor="nw",
            text="Data di arrivo",
            fill="#FFFFFF",
            font=("Inter Bold", 16 * -1)
        )

        self.entry_image_3 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            430.5,
            301.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#FAFFFD",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_3.place(
            x=314.0,
            y=285.0,
            width=233.0,
            height=30.0
        )

        self.canvas.create_text(
            302.0,
            264.0,
            anchor="nw",
            text="Tipologia camera",
            fill="#FFFFFF",
            font=("Inter Bold", 16 * -1)
        )

        self.canvas.create_text(
            302.0,
            202.0,
            anchor="nw",
            text="Data di partenza",
            fill="#FFFFFF",
            font=("Inter Bold", 16 * -1)
        )

        self.button_images = {
            f"button_{i}": self.load_button_image(f"button_{i}.png") for i in range(1, 1)
        }

        self.create_buttons()

        self.window.resizable(False, False)
        
    def create_buttons(self):
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )

        self.button_1.place(
            x=359.0,
            y=354.0,
            width=143.8626708984375,
            height=39.882110595703125
        )

    def relative_to_assets(self,path: str) -> Path:
        return Path(ASSETS_PATH) / Path(path)

    def load_button_image(self, image_path):
        abs_path = os.getcwd()
        if platform.system() == "Darwin":
            assets_path = abs_path + "/assets/frame5"
        else:
            assets_path = abs_path + "/build/assets/frame5"

        return PhotoImage(file=Path(assets_path) / Path(image_path))
    
if __name__ == "__main__":
    root = Tk()
    app = CercaCamereApp(root)
    root.mainloop()