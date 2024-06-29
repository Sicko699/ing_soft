from pathlib import Path
import os
import json
from datetime import datetime

abs_path = os.getcwd()
ASSETS_PATH = abs_path + "/assets/frame8"


class Gestore:
    def __init__(self, data_path):
        self.data_path = data_path

    def update_occupancy_data(self):
        try:
            with open(self.data_path, 'r') as file:
                data = json.load(file)

            # Verifica se il file contiene la sezione 'camere'
            if "camere" not in data[1]:
                print("Errore: Sezione 'camere' non trovata nel file JSON.")
                return [0, 0, 0, 0]

            camere_data = data[1]["camere"]
            current_year = datetime.now().year

            trimesters = {
                1: (1, 3),
                2: (4, 6),
                3: (7, 9),
                4: (10, 12)
            }

            occupancy_rates = []

            for trimester, (start_month, end_month) in trimesters.items():
                occupied_days = 0
                total_days = 0

                for month in range(start_month, end_month + 1):
                    days_in_month = (datetime(current_year, month + 1, 1) - datetime(current_year, month, 1)).days if month < 12 else 31
                    total_days += days_in_month * 24

                    for tipo_camera in camere_data:
                        for camere_info in tipo_camera.values():
                            for camera_id, prenotazioni in camere_info[0].items():
                                for prenotazione in prenotazioni:
                                    arrivo = prenotazione.get('arrivo')
                                    partenza = prenotazione.get('partenza')

                                    if arrivo and partenza:
                                        try:
                                            arrivo = datetime.strptime(arrivo, '%d-%m-%Y')
                                            partenza = datetime.strptime(partenza, '%d-%m-%Y')

                                            if (arrivo.month >= start_month and arrivo.month <= end_month) or \
                                                    (partenza.month >= start_month and partenza.month <= end_month):
                                                start_date = max(arrivo, datetime(current_year, start_month, 1))
                                                end_date = min(partenza, datetime(current_year, end_month, days_in_month))
                                                occupied_days += (end_date - start_date).days + 1
                                        except ValueError as ve:
                                            print(f"Errore nella data della prenotazione: {ve}")

                occupancy_rate = (occupied_days / (total_days * len(camere_data))) * 100
                occupancy_rates.append(round(occupancy_rate, 2))

            return occupancy_rates

        except Exception as e:
            print("Errore durante l'aggiornamento dei dati di occupazione:", e)
            return [0, 0, 0, 0]  # Return default values

