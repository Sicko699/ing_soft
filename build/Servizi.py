from pathlib import Path
import os, json, re
import tkinter.messagebox
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from main import multiplatform_open_read_data_json, multiplatform_open_write_data_json, go_visualizza_prenotazioni_servizi

abs_path = os.getcwd()
ASSETS_PATH = abs_path + "/assets/frame12"

class Servizio:
    def __init__(self, canvas):
        self.canvas = canvas
        self.entry_list_servizi = []
        self.current_entry_servizi = self.load_current_entry_servizi()

    def invia_prenotazione(self, nome_servizio, numero_camera):
        servizio = {
            "nome_servizio": nome_servizio,
            "numero_camera": numero_camera
        }

        try:
            with open("data.json", "r") as file:
                data = json.load(file)

            # Assuming you want to append 'servizio' to the 'servizi' list in the last dictionary of 'data'
            servizi = data[-1]["spa"]
            servizi.append(servizio)

            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)  # Writing back the entire 'data' dictionary
            print("Servizio spa aggiunto con successo")
        except Exception as e:
            print("Si è verificato un errore:", e)

    def relative_to_assets(self, path: str) -> Path:
        return Path(ASSETS_PATH) / Path(path)

    def load_button_image(self, image_path):
        abs_path = os.getcwd()
        assets_path = abs_path + "/assets/frame12"
        return PhotoImage(file=Path(assets_path) / Path(image_path))

    def save_entry_servizi(self, index):
        current_entry_servizi = self.entry_list_servizi[index].get()

        with open("current_entry_servizi.json", "w") as file:
            json.dump(current_entry_servizi, file)

    def elimina_prenotazione(self, window):
        data = multiplatform_open_read_data_json()

        with open("current_entry_servizi.json", "r") as user_json:
            current_entry_servizi = json.load(user_json)

        pattern = r'Servizio:\s*([^,]+),\s*Numero Camera:\s*([^"]+)'
        match = re.search(pattern, current_entry_servizi)
        tipo = match.group(1)
        numero_camera = match.group(2)

        print(tipo, numero_camera)

        for prenotazione in data[-1]["servizi"]:
            if prenotazione["nome_servizio"] == tipo and prenotazione["numero_camera"] == numero_camera:
                data[-1]["servizi"].remove(prenotazione)
                break

        multiplatform_open_write_data_json(data)
        tkinter.messagebox.showinfo("Avviso", "Prenotazione eliminata con successo!")
        go_visualizza_prenotazioni_servizi(window)

        def load_current_entry_servizi(self):
            with open("current_entry_servizi.json", "r") as user_json:
                current_entry_servizi = json.load(user_json)
            return current_entry_servizi

        def get_current_entry(self):
            pattern = r'Servizio:\s*([^,]+),\s*Numero Camera:\s*([^"]+)'
            match = re.search(pattern, self.current_entry_servizi)
            if match:
                return match.group(1), match.group(2)
            return None, None

        def save_changes(self, new_tipo, new_numero_camera, window):
            data = multiplatform_open_read_data_json()
            tipo, numero_camera = self.get_current_entry()

            for prenotazione in data[-1]["servizi"]:
                if prenotazione["nome_servizio"] == tipo and prenotazione["numero_camera"] == numero_camera:
                    prenotazione["nome_servizio"] = new_tipo
                    prenotazione["numero_camera"] = new_numero_camera
                    break

            multiplatform_open_write_data_json(data)
            tkinter.messagebox.showinfo("Avviso", "Modifiche confermate!")
            go_visualizza_prenotazioni_servizi(window)

        def invia_prenotazione(self, nome_servizio, numero_camera):
            servizio = {
                "nome_servizio": nome_servizio,
                "numero_camera": numero_camera
            }

            try:
                with open("data.json", "r") as file:
                    data = json.load(file)

                data[-1]["servizi"].append(servizio)

                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)

                print("Servizio aggiunto con successo")
            except Exception as e:
                print("Si è verificato un errore:", e)

        @staticmethod
        def relative_to_assets(path: str) -> Path:
            return Path(ASSETS_PATH) / Path(path)

        @staticmethod
        def load_button_image(image_path):
            return PhotoImage(file=Servizio.relative_to_assets(image_path))