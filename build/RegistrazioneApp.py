from pathlib import Path
import os, platform
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

class RegistrazioneApp:
    def __init__(self, window):
        self.window = window
        self.window.geometry("862x519")
        self.window.configure(bg = "#FAFFFD")
        
        self.canvas = Canvas(
            window,
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
            26.0,
            599.0,
            494.0,
            fill="#56AAFF",
            outline="")

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            430.5,
            96.0,
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
            y=80.0,
            width=233.0,
            height=30.0
        )
        
        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            430.5,
            158.0,
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
            y=142.0,
            width=233.0,
            height=30.0
        )
        
        self.canvas.create_text(
            302.0,
            59.0,
            anchor="nw",
            text="Nome",
            fill="#FFFFFF",
            font=("Inter Bold", 16 * -1)
        )

        self.canvas.create_text(
            302.0,
            122.0,
            anchor="nw",
            text="Cognome",
            fill="#FFFFFF",
            font=("Inter Bold", 16 * -1)
        )


        self.entry_image_3 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            430.5,
            221.0,
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
            y=205.0,
            width=233.0,
            height=30.0
        )
        self.entry_image_4 = PhotoImage(file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            430.5,
            283.0,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#FAFFFD",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_4.place(
            x=314.0,
            y=267.0,
            width=233.0,
            height=30.0
        )
        
        self.canvas.create_text(
            302.0,
            184.0,
            anchor="nw",
            text="Email",
            fill="#FFFFFF",
            font=("Inter Bold", 16 * -1)
        )

        self.canvas.create_text(
            302.0,
            247.0,
            anchor="nw",
            text="Numero di telefono",
            fill="#FFFFFF",
            font=("Inter Bold", 16 * -1)
        )
        
        self.entry_image_5 = PhotoImage(file=self.relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            430.5,
            346.0,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            bd=0,
            bg="#FAFFFD",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_5.place(
            x=314.0,
            y=330.0,
            width=233.0,
            height=30.0
        )
        
        self.entry_image_6 = PhotoImage(file=self.relative_to_assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(
            430.5,
            408.0,
            image=self.entry_image_6
        )
        self.entry_6 = Entry(
            bd=0,
            bg="#FAFFFD",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_6.place(
            x=314.0,
            y=392.0,
            width=233.0,
            height=30.0
        )
        
        self.canvas.create_text(
            302.0,
            309.0,
            anchor="nw",
            text="Username",
            fill="#FFFFFF",
            font=("Inter Bold", 16 * -1)
        )

        self.canvas.create_text(
            302.0,
            372.0,
            anchor="nw",
            text="Password",
            fill="#FFFFFF",
            font=("Inter Bold", 16 * -1)
        )
        
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("bottone registrazione"),
            relief="flat"
        )
        self.button_1.place(
            x=359.0,
            y=443.0,
            width=143.8626708984375,
            height=39.882110595703125
        )
        
        self.window.resizable(False, False)
        
    def relative_to_assets(self, path: str) -> Path:
        return ASSETS_PATH / Path(path)


if __name__ == '__main__':
    abs = os.getcwd()
    if(platform.system() == "Darwin"):
        ASSETS_PATH = abs + "/assets/frame4"
    else:
        ASSETS_PATH = abs + "/build/assets/frame4"
    
    
    root = Tk()
    app = RegistrazioneApp(root)
    root.mainloop()