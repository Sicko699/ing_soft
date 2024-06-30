from pathlib import Path
import os, platform, json
from datetime import datetime
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from main import exit_button, go_home_button, go_back_office_button, go_gestione_magazzino, go_gestione_servizi, go_gestione_spa, centrare_finestra

abs_path = os.getcwd()

ASSETS_PATH = abs_path + "/assets/frame7"

class FrontOfficeApp:
    def __init__(self, window):
        self.window = window
        self.window.geometry("862x519")
        self.window.configure(bg = "#FAFFFD")

        # Inizializzazione delle variabili
        prenotazione_singola = 0
        prenotazione_doppia = 0
        prenotazione_tripla = 0
        prenotazione_quadrupla = 0

        # Lettura del file JSON
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except Exception as e:
            print(f"Errore nella lettura del file JSON: {e}")
            data = []

        # Ottenere la data odierna
        oggi = datetime.now().date()

        # Funzione per convertire stringhe di date in oggetti datetime
        def str_to_date(date_str):
            return datetime.strptime(date_str, "%d-%m-%Y").date()

        # Controllare le prenotazioni
        for camera in data[1].get('camere', []):
            for tipo, prenotazioni_camera in camera.items():
                for numero_camera, prenotazioni in prenotazioni_camera[0].items():
                    for prenotazione in prenotazioni:
                        arrivo = prenotazione.get("arrivo", "")
                        partenza = prenotazione.get("partenza", "")
                        if not arrivo or not partenza:
                            continue
                        try:
                            arrivo_date = str_to_date(arrivo)
                            partenza_date = str_to_date(partenza)
                            if arrivo_date <= oggi <= partenza_date:
                                if tipo == "Camera Singola":
                                    prenotazione_singola += 1
                                elif tipo == "Camera Doppia":
                                    prenotazione_doppia += 1
                                elif tipo == "Camera Tripla":
                                    prenotazione_tripla += 1
                                elif tipo == "Camera Quadrupla":
                                    prenotazione_quadrupla += 1
                        except ValueError as e:
                            print(f"Errore nella conversione della data: {e}")

        # Stampare il risultato
        print(f"Occupazione Camera Singola: {prenotazione_singola}")
        print(f"Occupazione Camera Doppia: {prenotazione_doppia}")
        print(f"Occupazione Camera Tripla: {prenotazione_tripla}")
        print(f"Occupazione Camera Quadrupla: {prenotazione_quadrupla}")

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
        
        self.canvas.create_rectangle(
            316.0,
            170.0,
            756.0,
            420.0,
            fill="#FAFFFD",
            outline="")

        self.canvas.create_rectangle(
            316.0,
            170.0,
            756.0,
            201.0,
            fill="#56AAFF",
            outline="")

        self.canvas.create_text(
            506.0,
            173.0,
            anchor="nw",
            text="Report",
            fill="#FFFFFF",
            font=("Quicksand Medium", 18 * -1)
        )

        self.canvas.create_rectangle(
            356.0,
            227.2998046875,
            516.0,
            297.2998046875,
            fill="#EAEEEC",
            outline="")

        self.canvas.create_rectangle(
            356.0,
            322.2998046875,
            516.0,
            392.2998046875,
            fill="#EAEEEC",
            outline="")

        self.canvas.create_rectangle(
            556.0,
            227.0,
            716.0,
            297.0,
            fill="#EAEEEC",
            outline="")

        self.canvas.create_rectangle(
            556.0,
            322.0,
            716.0,
            392.0,
            fill="#EAEEEC",
            outline="")

        self.canvas.create_text(
            408.0,
            232.29998779296875,
            anchor="nw",
            text="Singole",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.canvas.create_text(
            595.0,
            327.29998779296875,
            anchor="nw",
            text="Quadruple",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.canvas.create_text(
            414.0,
            327.29998779296875,
            anchor="nw",
            text="Triple",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.canvas.create_text(
            608.0,
            232.0,
            anchor="nw",
            text="Doppie",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.canvas.create_text(
            420.0,
            262.29998779296875,
            anchor="nw",
            text=f"{prenotazione_singola} / 6",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.canvas.create_text(
            420.0,
            357.29998779296875,
            anchor="nw",
            text=f"{prenotazione_tripla} / 6",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.canvas.create_text(
            620.0,
            262.0,
            anchor="nw",
            text=f"{prenotazione_doppia} / 6",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.canvas.create_text(
            620.0,
            357.29998779296875,
            anchor="nw",
            text=f"{prenotazione_quadrupla} / 6",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        
        self.button_images = {
            f"button_{i}": self.load_button_image(f"button_{i}.png") for i in range(1, 10)
        }

        self.create_buttons()

        self.window.resizable(False, False)

    def create_buttons(self):
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: exit_button(self.window),
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
            command=lambda: go_home_button(self.window),
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
            y=98.0,
            width=162.0,
            height=45.0
        )
        
        self.button_image_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: go_inserimento_prenotazioni(self.window),
            relief="flat"
        )
        self.button_4.place(
            x=326.0,
            y=53.0,
            width=190.0,
            height=67.0
        )
        self.button_image_5 = PhotoImage(file=self.relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: go_visualizzazione_prenotazioni(self.window),
            relief="flat"
        )
        self.button_5.place(
            x=556.0,
            y=53.0,
            width=190.0,
            height=67.0
        )
        
        self.button_image_6 = PhotoImage(file=self.relative_to_assets("button_6.png"))
        self.button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: go_back_office_button(self.window),
            relief="flat"
        )
        self.button_6.place(
            x=24.0,
            y=158.0,
            width=162.0,
            height=45.0
        )
        self.button_image_8 = PhotoImage(file=self.relative_to_assets("button_8.png"))
        self.button_8 = Button(
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: go_gestione_magazzino(self.window),
            relief="flat"
        )
        self.button_8.place(
            x=24.0,
            y=218.0,
            width=162.0,
            height=45.0
        )
        self.button_image_9 = PhotoImage(file=self.relative_to_assets("button_9.png"))
        self.button_9 = Button(
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: go_gestione_servizi(self.window),
            relief="flat"
        )
        self.button_9.place(
            x=24.0,
            y=278.0,
            width=162.0,
            height=45.0
        )
        self.button_image_10 = PhotoImage(file=self.relative_to_assets("button_10.png"))
        self.button_10 = Button(
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: go_gestione_spa(self.window),
            relief="flat"
        )
        self.button_10.place(
            x=24.0,
            y=338.0,
            width=162.0,
            height=45.0
        )
            
    
    def relative_to_assets(self, path: str) -> Path:
        return Path(ASSETS_PATH) / Path(path)        

    def load_button_image(self, image_path):
        abs_path = os.getcwd()
        
        assets_path = abs_path + "/assets/frame7"
        
        return PhotoImage(file=Path(assets_path) / Path(image_path))
        
def go_inserimento_prenotazioni(window):
    from InserimentoPrenotazioniApp import InserimentoPrenotazione
    window.destroy()
    root = Tk()
    root.title("Inserimento Prenotazione")
    app = InserimentoPrenotazione(root)
    centrare_finestra(root)
    root.mainloop()

def go_visualizzazione_prenotazioni(window):
    from VisualizzazionePrenotazioniApp import VisualizzazionePrenotazioni
    window.destroy()
    root = Tk()
    root.title("Visualizzazione Prenotazioni")
    app = VisualizzazionePrenotazioni(root)
    centrare_finestra(root)
    root.mainloop()

if __name__ == "__main__":
    root = Tk()
    root.title("FrontOffice")
    app = FrontOfficeApp(root)
    centrare_finestra(root)
    root.mainloop()