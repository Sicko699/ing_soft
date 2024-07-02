import tkinter as tk
from tkinter import Tk, Button, ttk, PhotoImage
from tkcalendar import Calendar
from pathlib import Path
import platform, json, os
from datetime import datetime
from main import multiplatform_open_read_data_json, multiplatform_open_write_current_prenotazione

class Camere:
    def __init__(self, window):
        self.window = window

    def open_arrival_calendar(self):
        if platform.system() == "Darwin":
            self.arrival_calendar = ttk.Frame(self.window)
            self.arrival_calendar.pack(padx=10, pady=10)

            self.cal_arrival = Calendar(self.arrival_calendar, selectmode="day", date_pattern="dd-mm-yyyy", font="Quicksand 14", cursor="hand1")
            self.cal_arrival.grid(row=0, column=0, padx=10, pady=10)

            self.confirm_button = ttk.Button(self.arrival_calendar, text="Conferma", command=self.confirm_arrival_date)
            self.confirm_button.grid(row=1, column=0, pady=10)
        else:
            self.arrival_calendar = tk.Toplevel(self.window)
            self.arrival_calendar.geometry("390x300")
            self.arrival_calendar.title("Seleziona data di arrivo")

            cal_arrival = Calendar(self.arrival_calendar, selectmode="day", date_pattern="dd-mm-yyyy", font="Quicksand 14", cursor="hand1")
            cal_arrival.grid(row=0, column=0, padx=10, pady=10)

            confirm_button = Button(self.arrival_calendar, text="Conferma", command=self.confirm_arrival_date)
            confirm_button.grid(row=1, column=0, pady=10)

    def confirm_arrival_date(self):
        selected_date = self.arrival_calendar.winfo_children()[0].get_date()
        self.arrival_button.config(text=selected_date)
        self.arrival_calendar.destroy()

    def open_departure_calendar(self):
        if platform.system() == "Darwin":
            self.departure_calendar = ttk.Frame(self.window)
            self.departure_calendar.pack(padx=10, pady=10)

            self.cal_departure = Calendar(self.departure_calendar, selectmode="day", date_pattern="dd-mm-yyyy", font="Quicksand 14", cursor="hand1")
            self.cal_departure.grid(row=0, column=0, padx=10, pady=10)

            self.confirm_button = ttk.Button(self.departure_calendar, text="Conferma", command=self.confirm_departure_date)
            self.confirm_button.grid(row=1, column=0, pady=10)
        else:
            self.departure_calendar = tk.Toplevel(self.window)
            self.departure_calendar.geometry("390x300")
            self.departure_calendar.title("Seleziona data di partenza")

            cal_departure = Calendar(self.departure_calendar, selectmode="day", date_pattern="dd-mm-yyyy", font="Quicksand 14", cursor="hand1")
            cal_departure.grid(row=0, column=0, padx=10, pady=10)

            confirm_button = Button(self.departure_calendar, text="Conferma", command=self.confirm_departure_date)
            confirm_button.grid(row=1, column=0, pady=10)

    def confirm_departure_date(self):
        selected_date = self.departure_calendar.winfo_children()[0].get_date()
        self.departure_button.config(text=selected_date)
        self.departure_calendar.destroy()

    def check_availability_2(self):
        # Ottieni il tipo di camera selezionato
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
                            camera_disponibile = True
                            for prenotazione in prenotazioni:
                                if prenotazione["arrivo"] and prenotazione["partenza"]:
                                    print(prenotazione)
                                    # Se la prenotazione è vuota, la camera è libera
                                    arrivo_prenotazione = datetime.strptime(prenotazione["arrivo"], "%d-%m-%Y")
                                    partenza_prenotazione = datetime.strptime(prenotazione["partenza"], "%d-%m-%Y")
                                    if not (data_arrivo >= partenza_prenotazione or data_partenza <= arrivo_prenotazione):
                                        camera_disponibile = False
                                        break

                            if camera_disponibile:
                                print(f"La camera {numero_camera} è disponibile nell'intervallo selezionato.")
                                current_prenotazione = {
                                    "arrivo": data_arrivo.strftime("%d-%m-%Y"),
                                    "partenza": data_partenza.strftime("%d-%m-%Y"),
                                    "tipo_camera": tipo_camera
                                }
                                # Scrivi i dettagli dell'utente nel file current_user.json
                                multiplatform_open_write_current_prenotazione(current_prenotazione)
                                return
                    print("Tutte le camere sono disponibili nell'intervallo selezionato.")
                    return
        print("Nessuna camera disponibile nell'intervallo selezionato.")