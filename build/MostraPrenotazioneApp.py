from pathlib import Path
import os
import platform
from tkinter import Tk, Canvas, Button, PhotoImage
from datetime import datetime

abs_path = os.getcwd()
if platform.system() == "Darwin":
    ASSETS_PATH = abs_path + "/assets/frame6"
else:
    ASSETS_PATH = abs_path + "/build/assets/frame6"

data = [
    {
        "prezzi": [
            {
                "Camera Singola": "80",
                "Camera Doppia": "120",
                "Camera Tripla": "160",
                "Camera Quadrupla": "200"
            }
        ]
    }
]

class MostraPrenotazioneApp:
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

        # Estraiamo la prenotazione corrente dall'oggetto `current_prenotazione`
        current_prenotazione = {"arrivo": "19-04-2024", "partenza": "25-04-2024", "tipo_camera": "Camera Tripla"}

        # Calcoliamo il prezzo totale
        arrivo = datetime.strptime(current_prenotazione['arrivo'], "%d-%m-%Y")
        partenza = datetime.strptime(current_prenotazione['partenza'], "%d-%m-%Y")
        numero_giorni = (partenza - arrivo).days
        prezzo_camera = int(data[0]['prezzi'][0][current_prenotazione['tipo_camera']])
        prezzo_totale = numero_giorni * prezzo_camera

        # Creiamo gli elementi sulla canvas
        self.canvas.create_rectangle(
            262.0,
            140.0,
            599.0,
            380.0,
            fill="#56AAFF",
            outline="")

        self.canvas.create_text(
            325.0,
            163.0,
            anchor="nw",
            text="Tipologia camera selezionata",
            fill="#FFFFFF",
            font=("Inter Bold", 16 * -1)
        )

        self.canvas.create_text(
            369.0,
            200.0,  # Modifica la coordinata y per spostare il testo verso il basso
            anchor="nw",
            text=current_prenotazione['tipo_camera'],
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.canvas.create_text(
            383.0,
            222.0,
            anchor="nw",
            text="Prezzo totale",
            fill="#FFFFFF",
            font=("Inter Bold", 16 * -1)
        )
        
        self.canvas.create_rectangle(
            302.0,
            184.0,
            559.0,
            216.0,
            fill="#FAFFFD",
            outline=""
        )

        self.canvas.create_rectangle(
            302.0,
            242.0,
            559.0,
            274.0,
            fill="#FAFFFD",
            outline="")
        
        self.canvas.create_text(
            379.0,
            190.0,  # Modifica la coordinata y per spostare il testo verso il basso
            anchor="nw",
            text=current_prenotazione['tipo_camera'],
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.canvas.create_text(
            411.0,
            248.0,
            anchor="nw",
            text=f"{prezzo_totale}€",  # Mostra il prezzo totale calcolato
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.button_images = {
            f"button_{i}": self.load_button_image(f"button_{i}.png") for i in range(1, 2)
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

    def relative_to_assets(self, path: str) -> Path:
        return Path(ASSETS_PATH) / Path(path)

    def load_button_image(self, image_path):
        abs_path = os.getcwd()
        if platform.system() == "Darwin":
            assets_path = abs_path + "/assets/frame6"
        else:
            assets_path = abs_path + "/build/assets/frame6"

        return PhotoImage(file=Path(assets_path) / Path(image_path))


if __name__ == "__main__":
    root = Tk()
    app = MostraPrenotazioneApp(root)
    root.mainloop()
