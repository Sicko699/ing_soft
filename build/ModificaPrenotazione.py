import re
import tkinter as tk
from tkinter import Tk, Button, ttk, PhotoImage
from tkcalendar import Calendar
from pathlib import Path
import platform, json, os
from datetime import datetime
from CercaCamereApp import go_lista_prenotazioni
from main import centrare_finestra, multiplatform_open_read_data_json, multiplatform_open_write_current_prenotazione, \
    multiplatform_open_read_current_user

abs_path = os.getcwd()

ASSETS_PATH = abs_path + "/assets/frame20"

class ModificaPrenotazione:
    def __init__(self, window):
        self.window = window
        self.window.geometry("862x519")
        self.window.configure(bg="#FAFFFD")

        self.arrival_calendar = None
        self.departure_calendar = None

        data = multiplatform_open_read_data_json()
        current_user = multiplatform_open_read_current_user()
        with open("current_entry_prenotazione_user.json", "r") as prenotazione_json:
            current_prenotazione = json.load(prenotazione_json)
            print(current_prenotazione)

        # Initialize attributes to default values
        self.arrivo = ""
        self.partenza = ""

        pattern = r"Arrivo:\s*(\d{2}-\d{2}-\d{4}),\s*Partenza:\s*(\d{2}-\d{2}-\d{4})"

        match = re.search(pattern, current_prenotazione)
        if match:
            arrivo = match.group(1)
            partenza = match.group(2)
            print(f"Arrivo: {arrivo}, Partenza: {partenza}")
            if data and current_user:
                for user in data[0]['users']:
                    if user['username'] == current_user['username'] and user['password'] == current_user['password']:
                        prenotazioni = user.get('prenotazioni', [])
                        for prenotazione in prenotazioni:
                            if prenotazione['tipo_camera'] == tipo and prenotazione['arrivo'] == self.arrivo:
                                prenotazione_modificare = prenotazione
                                print("prenotazione", prenotazione_modificare)
                                self.partenza = prenotazione_modificare['partenza']
                                self.tipo_camera = prenotazione_modificare['tipo_camera']

        self.canvas = tk.Canvas(
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
            262.0,
            91.0,
            599.0,
            399.0,
            fill="#56AAFF",
            outline="")

        self.arrival_button = Button(
            self.canvas,
            text=self.arrivo,
            command=self.open_arrival_calendar,
            bg="#FAFFFD",
            fg="#000716",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            font=("Inter Bold", 12)
        )
        self.arrival_button.place(x=302.0, y=145.0, width=257, height=32)

        self.departure_button = Button(
            self.canvas,
            text=self.partenza,
            command=self.open_departure_calendar,
            bg="#FAFFFD",
            fg="#000716",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            font=("Inter Bold", 12)
        )
        self.departure_button.place(x=302.0, y=207.0, width=257, height=32)

        self.canvas.create_text(
            302.0,
            124.0,
            anchor="nw",
            text="Data di arrivo",
            fill="#FFFFFF",
            font=("Inter Bold", 16 * -1)
        )

        self.canvas.create_text(
            302.0,
            249.0,
            anchor="nw",
            text="Tipologia camera",
            fill="#FFFFFF",
            font=("Inter Bold", 16 * -1)
        )

        self.canvas.create_text(
            302.0,
            187.0,
            anchor="nw",
            text="Data di partenza",
            fill="#FFFFFF",
            font=("Inter Bold", 16 * -1)
        )

        self.combo_var = tk.StringVar()
        self.combo_var.set("Camera Singola")
        self.combo = ttk.Combobox(
            self.canvas,
            textvariable=self.combo_var,
            values=["Camera Singola", "Camera Doppia", "Camera Tripla", "Camera Quadrupla"],
            state="readonly",
            width=20,
            height=5,
            font=("Quicksand", 16 * -1)
        )
        self.combo.place(x=302.0, y=270, width=257, height=32)

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
            x=359.0,
            y=333.0,
            width=143.8626708984375,
            height=39.882110595703125
        )

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: go_lista_prenotazioni(self.window),
            relief="flat"
        )
        self.button_2.place(
            x=27.0,
            y=21.0,
            width=47.0,
            height=45.0
        )

    def open_arrival_calendar(self):
        self.open_calendar(self.arrivo, self.confirm_arrival_date)

    def open_departure_calendar(self):
        self.open_calendar(self.partenza, self.confirm_departure_date)

    def open_calendar(self, initial_date, confirm_command):
        if platform.system() == "Darwin":
            calendar_frame = ttk.Frame(self.window)
            calendar_frame.pack(padx=10, pady=10)

            cal = Calendar(calendar_frame, selectmode="day", date_pattern="dd-mm-yyyy",
                           font="Quicksand 14", cursor="hand1")
            cal.grid(row=0, column=0, padx=10, pady=10)
            if initial_date:
                cal.set_date(initial_date)

            confirm_button = ttk.Button(calendar_frame, text="Conferma", command=lambda: confirm_command(cal.get_date(), calendar_frame))
            confirm_button.grid(row=1, column=0, pady=10)
        else:
            calendar_top = tk.Toplevel(self.window)
            calendar_top.geometry("390x300")
            calendar_top.title("Seleziona data")

            cal = Calendar(calendar_top, selectmode="day", date_pattern="dd-mm-yyyy",
                           font="Quicksand 14", cursor="hand1")
            cal.grid(row=0, column=0, padx=10, pady=10)
            if initial_date:
                cal.set_date(initial_date)

            confirm_button = Button(calendar_top, text="Conferma", command=lambda: confirm_command(cal.get_date(), calendar_top))
            confirm_button.grid(row=1, column=0, pady=10)

    def confirm_arrival_date(self, selected_date, calendar_widget):
        self.arrival_button.config(text=selected_date)
        calendar_widget.destroy()

    def confirm_departure_date(self, selected_date, calendar_widget):
        self.departure_button.config(text=selected_date)
        calendar_widget.destroy()

    def relative_to_assets(self, path: str) -> Path:
        return Path(ASSETS_PATH) / Path(path)

    def load_button_image(self, image_path):
        abs_path = os.getcwd()

        assets_path = abs_path + "/assets/frame20"

        return PhotoImage(file=Path(assets_path) / Path(image_path))

    def check_availability(self):
        tipo_camera = self.combo_var.get()

        # Ottieni le date di arrivo e partenza
        data_arrivo = datetime.strptime(self.arrival_button.cget("text"), "%d-%m-%Y")
        data_partenza = datetime.strptime(self.departure_button.cget("text"), "%d-%m-%Y")
        print(tipo_camera, data_arrivo, data_partenza)
        # Carica i dati dal file JSON
        data = multiplatform_open_read_data_json()

        # Cerca la camera corrispondente
        for categoria_camera in data[1]["camere"]:
            for tipo, camere in categoria_camera.items():
                if tipo == tipo_camera:
                    for camera in camere:
                        for numero_camera, prenotazioni in camera.items():
                            for prenotazione in prenotazioni:
                                # Se la prenotazione è vuota, la camera è libera
                                if prenotazione["arrivo"] == "" and prenotazione["partenza"] == "":
                                    print(f"La camera {numero_camera} è disponibile nell'intervallo selezionato.")
                                    current_prenotazione = {
                                        "arrivo": data_arrivo.strftime("%d-%m-%Y"),
                                        "partenza": data_partenza.strftime("%d-%m-%Y"),
                                        "tipo_camera": tipo_camera
                                    }

                                    # Scrivi i dettagli dell'utente nel file current_user.json
                                    current_prenotazione = multiplatform_open_write_current_prenotazione(current_prenotazione)
                                    return
                                if prenotazione["arrivo"] and prenotazione["partenza"]:
                                    arrivo_prenotazione = datetime.strptime(prenotazione["arrivo"], "%d-%m-%Y")
                                    partenza_prenotazione = datetime.strptime(prenotazione["partenza"], "%d-%m-%Y")

                                    # Verifica se le date si sovrappongono
                                    if (data_arrivo < partenza_prenotazione and data_partenza > arrivo_prenotazione) or \
                                            (data_arrivo == arrivo_prenotazione and data_partenza == partenza_prenotazione):
                                        print(f"La camera {numero_camera} non è disponibile nell'intervallo selezionato.")
                                        return
                    print("Tutte le camere sono disponibili nell'intervallo selezionato.")
                    return
        print("Nessuna camera disponibile nell'intervallo selezionato.")

if __name__ == "__main__":
    root = Tk()
    root.title("Modifica Prenotazione")
    app = ModificaPrenotazione(root)
    centrare_finestra(root)
    root.mainloop()
