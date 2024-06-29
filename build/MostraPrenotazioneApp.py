import uuid
from pathlib import Path
import platform, json, os
from tkinter import Tk, Canvas, Button, PhotoImage
from datetime import datetime
from main import go_cerca_camere, centrare_finestra, multiplatform_open_read_current_user, multiplatform_open_read_data_json, multiplatform_open_read_current_prenotazione, multiplatform_open_write_data_json

abs_path = os.getcwd()

ASSETS_PATH = abs_path + "/assets/frame6"

data_prezzi = {
    "prezzi": [
        {
            "Camera Singola": "80",
            "Camera Doppia": "120",
            "Camera Tripla": "160",
            "Camera Quadrupla": "200"
        }
    ]
}

class MostraPrenotazioneApp:
    def __init__(self, window):
        self.window = window
        self.window.geometry("862x519")
        self.window.configure(bg="#FAFFFD")
        
        data = multiplatform_open_read_current_prenotazione()

        tipo_camera = data["tipo_camera"]
        data_arrivo = data["arrivo"]
        data_partenza = data["partenza"]


        arrivo = datetime.strptime(data_arrivo, "%d-%m-%Y")
        partenza = datetime.strptime(data_partenza, "%d-%m-%Y")

        # Calcola la differenza tra le date
        differenza = partenza - arrivo

        # Estrai il numero di giorni dalla differenza
        numero_giorni = differenza.days
        
        prezzo = None
        for prezzi in data_prezzi["prezzi"]:
            if tipo_camera in prezzi:
                prezzo = int(prezzi[tipo_camera])
                break
        

        prezzo_totale = numero_giorni * prezzo
        print(numero_giorni, prezzo, prezzo_totale)
        
        if(tipo_camera == "Camera Singola"):
            numero_ospiti = 1
        elif(tipo_camera == "Camera Doppia"):
            numero_ospiti = 2
        elif(tipo_camera == "Camera Tripla"):
            numero_ospiti = 3
        elif(tipo_camera == "Camera Quadrupla"):
            numero_ospiti = 4
        else:
            numero_ospiti = None
        
        
        
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
            text=tipo_camera,
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
            command=lambda: go_cerca_camere(self.window),
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
        
        assets_path = abs_path + "/assets/frame6"

        return PhotoImage(file=Path(assets_path) / Path(image_path))

    def update_data_json(self):
        # Carica i dati correnti da data.json
        data_json = multiplatform_open_read_data_json()
                
        # Estrai i dati della prenotazione corrente da current_prenotazione.json
        current_prenotazione = multiplatform_open_read_current_prenotazione()
                
        # Estrai i dati dell'utente da current_user.json
        current_user = multiplatform_open_read_current_user()
        
        username = current_user["username"]
                
        # Trova l'utente corrispondente
        user_data = next((user for user in data_json[0]["users"] if user["username"] == username), None)

        if user_data is None:
            print(user_data, username)
            print("Utente non trovato.")
            return

        # Aggiungi il nome e il cognome alla prenotazione
        current_prenotazione["id_utente"] = user_data.get("id_utente", "")
        current_prenotazione["nome"] = user_data.get("nome", "")
        current_prenotazione["cognome"] = user_data.get("cognome", "")
        current_prenotazione["username"] = user_data.get("username", "")
        
        print(current_prenotazione)
        
        tipo_camera = current_prenotazione["tipo_camera"]
        if(tipo_camera == "Camera Singola"):
            numero_ospiti = 1
        elif(tipo_camera == "Camera Doppia"):
            numero_ospiti = 2
        elif(tipo_camera == "Camera Tripla"):
            numero_ospiti = 3
        elif(tipo_camera == "Camera Quadrupla"):
            numero_ospiti = 4
        else:
            numero_ospiti = None

        

        # Trova la camera corrispondente alla prenotazione
        camera_disponibile = False
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
                        id_prenotazione = uuid.uuid4()
                        # Aggiorna le date di arrivo e partenza
                        prenotazioni.append({
                            "arrivo": current_prenotazione["arrivo"],
                            "partenza": current_prenotazione["partenza"],
                            "tipo": current_prenotazione["tipo_camera"],
                            "id_prenotazione": str(id_prenotazione)
                        })
                        
                        print(f"Prenotazione inserita nella camera {current_prenotazione['tipo_camera']} {numero_camera}")
                        prenotazione_utente = {
                            "arrivo": current_prenotazione["arrivo"],
                            "partenza": current_prenotazione["partenza"],
                            "tipo": current_prenotazione["tipo_camera"],
                            "id_prenotazione": str(id_prenotazione)
                        }

                        user_data["prenotazioni"].append(prenotazione_utente)
                        camera_disponibile = True
                        break  # Esci dal ciclo delle camere
                else:
                    continue  # Prova con la prossima camera
                break  # Esci dal ciclo delle camere

        # Se nessuna camera è disponibile, mostra un messaggio
        if not camera_disponibile:
            print("Non ci sono camere disponibili per la prenotazione.")
            return

        # Sovrascrivi il file data.json con i dati aggiornati
        write_data = multiplatform_open_write_data_json(data_json)
        
        print("Dati della prenotazione aggiornati con successo.")



if __name__ == "__main__":
    root = Tk()
    root.title("Mosta Prenotazione")
    app = MostraPrenotazioneApp(root)
    centrare_finestra(root)
    root.mainloop()
