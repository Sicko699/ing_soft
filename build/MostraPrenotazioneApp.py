from pathlib import Path
import platform, json, os
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
            command=self.update_data_json,  # Collega il bottone alla funzione di aggiornamento
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

    def update_data_json(self):
    # Carica i dati correnti da data.json
        with open("data.json", "r") as file:
            data_json = json.load(file)

        # Estrai i dati della prenotazione corrente da current_prenotazione.json
        with open("current_prenotazione.json", "r") as file:
            current_prenotazione = json.load(file)

        # Estrai il nome utente corrente da current_user.json
        with open("current_user.json", "r") as file:
            current_user = json.load(file)
            username = current_user["username"]

        # Trova l'utente corrispondente
        user_data = next((user for user in data_json[0]["users"] if user["username"] == username), None)

        if user_data is None:
            print("Utente non trovato.")
            return

        # Aggiungi il nome e il cognome alla prenotazione
        current_prenotazione["nome"] = user_data.get("nome", "")
        current_prenotazione["cognome"] = user_data.get("cognome", "")

        # Trova la camera corrispondente alla prenotazione
        for camera in data_json[1]["camere"]:
            if current_prenotazione["tipo_camera"] in camera:
                prenotazioni_camera = camera[current_prenotazione["tipo_camera"]]
                # Trova la prima cella libera in base alle date di arrivo e partenza
                for numero_camera, prenotazioni in prenotazioni_camera[0].items():
                    cella_disponibile = True
                    for prenotazione in prenotazioni:
                        if prenotazione["arrivo"] == "" and prenotazione["partenza"] == "":
                            continue  # La cella è libera, continua con la prossima camera
                        elif (current_prenotazione["arrivo"] >= prenotazione["partenza"] or
                            current_prenotazione["partenza"] <= prenotazione["arrivo"]):
                            continue  # Le date della prenotazione non si sovrappongono, continua con la prossima camera
                        else:
                            cella_disponibile = False
                            break  # La cella è occupata, esci dal ciclo
                    if cella_disponibile:
                        # Aggiorna le date di arrivo e partenza
                        prenotazioni.append({
                            "arrivo": current_prenotazione["arrivo"],
                            "partenza": current_prenotazione["partenza"],
                            "nome": current_prenotazione["nome"],
                            "cognome": current_prenotazione["cognome"]
                        })
                        print(f"Prenotazione inserita nella camera {current_prenotazione['tipo_camera']} {numero_camera}")
                        break  # Esci dal ciclo delle camere
                else:
                    print(f"Non ci sono camere disponibili per la prenotazione della camera {current_prenotazione['tipo_camera']}")
                    # Gestisci il caso in cui non ci siano camere disponibili per la prenotazione
                    break  # Esci dal ciclo delle camere

        # Sovrascrivi il file data.json con i dati aggiornati
        with open("data.json", "w") as file:
            json.dump(data_json, file, indent=4)

        print("Dati della prenotazione aggiornati con successo.")



if __name__ == "__main__":
    root = Tk()
    app = MostraPrenotazioneApp(root)
    root.mainloop()
