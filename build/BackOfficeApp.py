from pathlib import Path
import os, json
from datetime import datetime
from tkinter import Tk, Canvas, Button, PhotoImage
from main import centrare_finestra, exit_button, go_home_button, go_front_office_button, go_gestione_magazzino, \
    go_gestione_servizi, go_gestione_spa

abs_path = os.getcwd()

ASSETS_PATH = abs_path + "/assets/frame8"


class BackOfficeApp:
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
        self.canvas.create_rectangle(
            0.0,
            0.0,
            210.0,
            519.0,
            fill="#3E97F1",
            outline="")

        self.canvas.create_rectangle(
            405.0,
            45.0,
            665.0,
            81.0,
            fill="#56AAFF",
            outline="")

        self.canvas.create_text(
            415.0,
            53.0,
            anchor="nw",
            text="Camere occupate per periodo",
            fill="#FFFFFF",
            font=("Quicksand Medium", 18 * -1)
        )

        # Centering the rectangles and the text
        rect_x_start = 375.0
        rect_x_end = 695.0
        text_x_start = rect_x_start + 80
        percent_x_start = rect_x_end - 50

        self.canvas.create_rectangle(
            rect_x_start,
            116.0,
            rect_x_end,
            176.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            rect_x_start,
            211.0,
            rect_x_end,
            271.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            rect_x_start,
            306.0,
            rect_x_end,
            366.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            rect_x_start,
            401.0,
            rect_x_end,
            461.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_text(
            text_x_start,
            90.0,
            anchor="nw",
            text="1° Trimestre",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.canvas.create_text(
            text_x_start,
            185.0,
            anchor="nw",
            text="2° Trimestre",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.canvas.create_text(
            text_x_start,
            280.0,
            anchor="nw",
            text="3° Trimestre",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.canvas.create_text(
            text_x_start,
            375.0,
            anchor="nw",
            text="4° Trimestre",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.canvas.create_text(
            395.0,
            136.0,
            anchor="nw",
            text="Percentuale occupazione camere",
            fill="#000000",
            font=("Quicksand Medium", 15 * -1)
        )

        self.canvas.create_text(
            395.0,
            230.0,
            anchor="nw",
            text="Percentuale occupazione camere",
            fill="#000000",
            font=("Quicksand Medium", 15 * -1)
        )

        self.canvas.create_text(
            395.0,
            325.0,
            anchor="nw",
            text="Percentuale occupazione camere",
            fill="#000000",
            font=("Quicksand Medium", 15 * -1)
        )

        self.canvas.create_text(
            395.0,
            420.0,
            anchor="nw",
            text="Percentuale occupazione camere",
            fill="#000000",
            font=("Quicksand Medium", 15 * -1)
        )

        self.percent_texts = []
        for y_pos in [136.0, 231.0, 326.0, 421.0]:
            text = self.canvas.create_text(
                percent_x_start,
                y_pos,
                anchor="nw",
                text="",
                fill="#000000",
                font=("Quicksand Medium", 18 * -1)
            )
            self.percent_texts.append(text)

        self.button_images = {
            f"button_{i}": self.load_button_image(f"button_{i}.png") for i in range(1, 8)
        }

        self.create_buttons()
        self.update_occupancy_data()
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
            command=lambda: go_front_office_button(self.window),
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
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.button_4.place(
            x=24.0,
            y=158.0,
            width=162.0,
            height=45.0
        )

        self.button_image_6 = PhotoImage(file=self.relative_to_assets("button_6.png"))
        self.button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: go_gestione_magazzino(self.window),
            relief="flat"
        )
        self.button_6.place(
            x=24.0,
            y=218.0,
            width=162.0,
            height=45.0
        )

        self.button_image_7 = PhotoImage(file=self.relative_to_assets("button_7.png"))
        self.button_7 = Button(
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: go_gestione_servizi(self.window),
            relief="flat"
        )
        self.button_7.place(
            x=24.0,
            y=278.0,
            width=162.0,
            height=45.0
        )

        self.button_image_8 = PhotoImage(file=self.relative_to_assets("button_8.png"))
        self.button_8 = Button(
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: go_gestione_spa(self.window),
            relief="flat"
        )
        self.button_8.place(
            x=24.0,
            y=338.0,
            width=162.0,
            height=45.0
        )

    def relative_to_assets(self, path: str) -> Path:
        return Path(ASSETS_PATH) / Path(path)

    def load_button_image(self, image_path):
        abs_path = os.getcwd()
        assets_path = abs_path + "/assets/frame8"
        return PhotoImage(file=Path(assets_path) / Path(image_path))

    def update_occupancy_data(self):
        try:
            with open('data.json', 'r') as file:
                data = json.load(file)

            # Verifica se il file contiene la sezione 'camere'
            if "camere" not in data[1]:
                print("Errore: Sezione 'camere' non trovata nel file JSON.")
                return

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
                    days_in_month = (datetime(current_year, month + 1, 1) - datetime(current_year, month,
                                                                                     1)).days if month < 12 else 31
                    total_days += days_in_month

                    # Itera su tutte le camere e le relative prenotazioni
                    for tipo_camera in camere_data:
                        for camere_info in tipo_camera.values():
                            for camera_id, prenotazioni in camere_info[0].items():
                                for prenotazione in prenotazioni:
                                    arrivo = prenotazione.get('arrivo')
                                    partenza = prenotazione.get('partenza')

                                    if arrivo and partenza:  # Verifica che entrambe le date siano presenti
                                        try:
                                            arrivo = datetime.strptime(arrivo, '%d-%m-%Y')
                                            partenza = datetime.strptime(partenza, '%d-%m-%Y')

                                            # Controlla se la prenotazione cade nel trimestre
                                            if (arrivo.month >= start_month and arrivo.month <= end_month) or \
                                                    (partenza.month >= start_month and partenza.month <= end_month):
                                                start_date = max(arrivo, datetime(current_year, start_month, 1))
                                                end_date = min(partenza,
                                                               datetime(current_year, end_month, days_in_month))
                                                occupied_days += (end_date - start_date).days + 1
                                        except ValueError as ve:
                                            print(f"Errore nella data della prenotazione: {ve}")

                occupancy_rate = (occupied_days / (total_days * len(camere_data))) * 100
                occupancy_rates.append(round(occupancy_rate, 2))

            for i, rate in enumerate(occupancy_rates):
                self.canvas.itemconfig(self.percent_texts[i], text=f"{rate}%")

        except Exception as e:
            print("Errore durante l'aggiornamento dei dati di occupazione:", e)


if __name__ == "__main__":
    window = Tk()
    app = BackOfficeApp(window)
    centrare_finestra(window)
    window.mainloop()