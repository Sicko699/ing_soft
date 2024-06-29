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
        self.tipo_camera = ""

        # Definizione del pattern regex
        pattern = r'(\d{2}-\d{2}-\d{4}), (\d{2}-\d{2}-\d{4}), (.+)'

        # Ricerca della corrispondenza
        match = re.search(pattern, current_prenotazione)
        if match:
            self.arrivo = match.group(1)
            self.partenza = match.group(2)
            self.tipo_camera = match.group(3)
            if data and current_user:
                for user in data[0]['users']:
                    if user['username'] == current_user['username'] and user['password'] == current_user['password']:
                        prenotazioni = user.get('prenotazioni', [])
                        for prenotazione in prenotazioni:
                            if  prenotazione['arrivo'] == self.arrivo:
                                prenotazione_modificare = prenotazione
                                print("prenotazione", prenotazione_modificare)
                                self.arrivo = prenotazione_modificare['arrivo']
                                self.partenza = prenotazione_modificare['partenza']
                                self.tipo_camera = prenotazione_modificare['tipo']

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
        self.combo_var.set(self.tipo_camera)
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
            command=lambda: (self.check_availability(), self.modifica_prenotazione()),
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
                cal.selection_set(datetime.strptime(initial_date, "%d-%m-%Y"))

            confirm_button = ttk.Button(calendar_frame, text="Conferma",
                                        command=lambda: confirm_command(cal.get_date(), calendar_frame))
            confirm_button.grid(row=1, column=0, pady=10)
        else:
            calendar_top = tk.Toplevel(self.window)
            calendar_top.geometry("390x300")
            calendar_top.title("Seleziona data")

            cal = Calendar(calendar_top, selectmode="day", date_pattern="dd-mm-yyyy",
                           font="Quicksand 14", cursor="hand1")
            cal.pack(padx=10, pady=10)
            if initial_date:
                cal.selection_set(datetime.strptime(initial_date, "%d-%m-%Y"))

            confirm_button = ttk.Button(calendar_top, text="Conferma",
                                        command=lambda: confirm_command(cal.get_date(), calendar_top))
            confirm_button.pack(pady=10)

    def confirm_arrival_date(self, date, widget):
        self.arrival_button.config(text=date)
        widget.destroy()

    def confirm_departure_date(self, date, widget):
        self.departure_button.config(text=date)
        widget.destroy()

    def check_availability(self):
        data_arrivo = datetime.strptime(self.arrival_button.cget("text"), "%d-%m-%Y")
        data_partenza = datetime.strptime(self.departure_button.cget("text"), "%d-%m-%Y")
        tipo_camera = self.combo.get()

        if not self.prenotazione.check_availability(tipo_camera, data_arrivo, data_partenza):
            tk.messagebox.showinfo("Disponibilità",
                                   "Non c'è disponibilità per la camera selezionata nelle date indicate.")
        else:
            tk.messagebox.showinfo("Disponibilità", "Camera disponibile!")

    def modifica_prenotazione(self):
        new_arrivo = self.arrival_button.cget("text")
        new_partenza = self.departure_button.cget("text")
        new_tipo_camera = self.combo.get()

        if self.prenotazione.update_prenotazione(self.arrivo, self.partenza, self.tipo_camera, new_arrivo, new_partenza,
                                                 new_tipo_camera):
            tk.messagebox.showinfo("Modifica Prenotazione", "Prenotazione modificata con successo!")
        else:
            tk.messagebox.showerror("Errore", "Errore nella modifica della prenotazione.")

    def load_button_image(self, image_name):
        return PhotoImage(file=self.relative_to_assets(image_name))

    def relative_to_assets(self, path):
        return ASSETS_PATH / Path(path)


if __name__ == "__main__":
    root = Tk()
    root.title("Modifica Prenotazione")
    app = ModificaPrenotazione(root)
    centrare_finestra(root)
    root.mainloop()