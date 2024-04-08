from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import os, platform
from main import exit_button, go_front_office_button, go_back_office_button, go_tariffe_dinamiche_button, go_gestione_magazzino

class MainApp:
    def __init__(self, window):
        self.window = window
        self.window.geometry("862x519")
        self.window.configure(bg="#FAFFFD")

        self.canvas = Canvas(
            self.window,
            bg="#FAFFFD",
            height=519,
            width=862,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        
        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            210.0,
            519.0,
            fill="#3E97F1",
            outline=""
        )

        # Load button images and store them as attributes
        self.button_images = {
            f"button_{i}": self.load_button_image(f"button_{i}.png") for i in range(1, 13)
        }

        self.create_buttons()

        self.window.resizable(False, False)

    def create_buttons(self):
        button_1 = Button(
            self.window,
            image=self.button_images["button_1"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.place(x=289.0, y=75.0, width=221.0, height=166.0)

        button_2 = Button(
            self.window,
            image=self.button_images["button_2"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        button_2.place(x=562.0, y=75.0, width=221.0, height=166.0)

        button_3 = Button(
            self.window,
            image=self.button_images["button_3"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        button_3.place(x=289.0, y=277.0, width=221.0, height=166.0)

        button_4 = Button(
            self.window,
            image=self.button_images["button_4"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        button_4.place(x=562.0, y=277.0, width=221.0, height=166.0)

        button_5 = Button(
            self.window,
            image=self.button_images["button_5"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: exit_button(self.window),
            relief="flat"
        )
        button_5.place(x=46.0, y=452.0, width=47.0, height=45.0)

        button_6 = Button(
            self.window,
            image=self.button_images["button_6"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        button_6.place(x=116.0, y=452.0, width=47.0, height=45.0)

        button_7 = Button(
            self.window,
            image=self.button_images["button_7"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: go_front_office_button(self.window),
            relief="flat"
        )
        button_7.place(x=24.0, y=75.0, width=162.0, height=45.0)

        button_8 = Button(
            self.window,
            image=self.button_images["button_8"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: go_back_office_button(self.window),
            relief="flat"
        )
        button_8.place(x=24.0, y=135.0, width=162.0, height=45.0)

        button_9 = Button(
            self.window,
            image=self.button_images["button_9"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: go_tariffe_dinamiche_button(self.window),
            relief="flat"
        )
        button_9.place(x=24.0, y=195.0, width=162.0, height=45.0)

        button_10 = Button(
            self.window,
            image=self.button_images["button_10"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: go_gestione_magazzino(self.window),
            relief="flat"
        )
        button_10.place(x=24.0, y=255.0, width=162.0, height=45.0)

        button_11 = Button(
            self.window,
            image=self.button_images["button_11"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_11 clicked"),
            relief="flat"
        )
        button_11.place(x=24.0, y=315.0, width=162.0, height=45.0)

        button_12 = Button(
            self.window,
            image=self.button_images["button_12"],
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_12 clicked"),
            relief="flat"
        )
        button_12.place(x=24.0, y=375.0, width=162.0, height=45.0)

    def load_button_image(self, image_path):
        abs = os.getcwd()
        if(platform.system() == "Darwin"):
            ASSETS_PATH = abs + "/assets/frame2"
        else:
            ASSETS_PATH = abs + "/build/assets/frame2"

        return PhotoImage(file=ASSETS_PATH / Path(image_path))
    
if __name__ == "__main__":
    root = Tk()
    app = MainApp(root)
    root.mainloop()
