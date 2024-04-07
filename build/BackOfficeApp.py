from pathlib import Path
import os, platform
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

class BackOfficeApp:
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
            0.0,
            0.0,
            210.0,
            519.0,
            fill="#3E97F1",
            outline="")

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
            236.0,
            45.0,
            522.0,
            475.0,
            fill="#FAFFFD",
            outline="")

        self.canvas.create_rectangle(
            547.0,
            45.0,
            833.0,
            475.0,
            fill="#FAFFFD",
            outline="")

        self.canvas.create_rectangle(
            236.0,
            45.0,
            522.0,
            81.0,
            fill="#56AAFF",
            outline="")

        self.canvas.create_text(
            245.0,
            53.0,
            anchor="nw",
            text="Camere occupate per periodo",
            fill="#FFFFFF",
            font=("Quicksand Medium", 18 * -1)
        )

        self.canvas.create_rectangle(
            547.0,
            45.0,
            833.0,
            81.0,
            fill="#56AAFF",
            outline="")

        self.canvas.create_text(
            581.0,
            53.0,
            anchor="nw",
            text="Resoconto incassi annuali",
            fill="#FFFFFF",
            font=("Quicksand Medium", 18 * -1)
        )

        self.canvas.create_rectangle(
            249.0,
            116.0,
            508.0,
            176.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            249.0,
            211.0,
            508.0,
            271.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            249.0,
            306.0,
            508.0,
            366.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            249.0,
            401.0,
            508.0,
            461.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_text(
            335.0,
            90.0,
            anchor="nw",
            text="1° Trimestre",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.canvas.create_text(
            659.0,
            90.0,
            anchor="nw",
            text="Camere",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.canvas.create_text(
            651.0,
            167.0,
            anchor="nw",
            text="Ristorante",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.canvas.create_text(
            665.0,
            242.0,
            anchor="nw",
            text="Servizi",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.canvas.create_text(
            675.0,
            317.0,
            anchor="nw",
            text="Spa",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.canvas.create_text(
            676.0,
            392.0,
            anchor="nw",
            text="Bar",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.canvas.create_text(
            333.0,
            185.0,
            anchor="nw",
            text="2° Trimestre",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.canvas.create_text(
            333.0,
            280.0,
            anchor="nw",
            text="3° Trimestre",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.canvas.create_text(
            333.0,
            375.0,
            anchor="nw",
            text="4° Trimestre",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.canvas.create_rectangle(
            560.0,
            116.0,
            819.0,
            161.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            560.0,
            191.0,
            819.0,
            236.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            560.0,
            266.0,
            819.0,
            311.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            560.0,
            341.0,
            819.0,
            386.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            560.0,
            416.0,
            819.0,
            461.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            448.0,
            121.0,
            498.0,
            171.0,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_rectangle(
            448.0,
            216.0,
            498.0,
            266.0,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_rectangle(
            448.0,
            311.0,
            498.0,
            361.0,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_rectangle(
            448.0,
            406.0,
            498.0,
            456.0,
            fill="#FFFFFF",
            outline="")

        self.canvas.create_text(
            261.0,
            126.0,
            anchor="nw",
            text="Percentuale occupazione camere",
            fill="#000000",
            font=("Quicksand Medium", 15 * -1)
        )

        self.canvas.create_text(
            262.0,
            221.0,
            anchor="nw",
            text="Percentuale occupazione camere",
            fill="#000000",
            font=("Quicksand Medium", 15 * -1)
        )

        self.canvas.create_text(
            263.0,
            316.0,
            anchor="nw",
            text="Percentuale occupazione camere",
            fill="#000000",
            font=("Quicksand Medium", 15 * -1)
        )

        self.canvas.create_text(
            263.0,
            416.0,
            anchor="nw",
            text="Percentuale occupazione camere",
            fill="#000000",
            font=("Quicksand Medium", 15 * -1)
        )

        self.canvas.create_text(
            451.0,
            136.0,
            anchor="nw",
            text="60%",
            fill="#000000",
            font=("Quicksand Medium", 18 * -1)
        )

        self.canvas.create_text(
            451.0,
            326.0,
            anchor="nw",
            text="80%",
            fill="#000000",
            font=("Quicksand Medium", 18 * -1)
        )

        self.canvas.create_text(
            451.0,
            421.0,
            anchor="nw",
            text="53%",
            fill="#000000",
            font=("Quicksand Medium", 18 * -1)
        )

        self.canvas.create_text(
            451.0,
            231.0,
            anchor="nw",
            text="37%",
            fill="#000000",
            font=("Quicksand Medium", 18 * -1)
        )

        self.canvas.create_text(
            567.0,
            129.0,
            anchor="nw",
            text="Suca suca suca suca",
            fill="#000000",
            font=("Quicksand Medium", 18 * -1)
        )

        self.canvas.create_text(
            567.0,
            204.0,
            anchor="nw",
            text="Suca suca suca suca",
            fill="#000000",
            font=("Quicksand Medium", 18 * -1)
        )

        self.canvas.create_text(
            567.0,
            279.0,
            anchor="nw",
            text="Suca suca suca suca",
            fill="#000000",
            font=("Quicksand Medium", 18 * -1)
        )

        self.canvas.create_text(
            567.0,
            354.0,
            anchor="nw",
            text="Suca suca suca suca",
            fill="#000000",
            font=("Quicksand Medium", 18 * -1)
        )

        self.canvas.create_text(
            567.0,
            429.0,
            anchor="nw",
            text="Suca suca suca suca",
            fill="#000000",
            font=("Quicksand Medium", 18 * -1)
        )
    def relative_to_assets(self, path: str) -> Path:
        return ASSETS_PATH / Path(path)

    
if __name__ == "__main__":
    abs = os.getcwd()
    if(platform.system() == "Darwin"):
        ASSETS_PATH = abs + "/assets/frame8"
    else:
        ASSETS_PATH = abs + "/build/assets/frame8"

    root = Tk()
    app = BackOfficeApp(root)
    root.mainloop()