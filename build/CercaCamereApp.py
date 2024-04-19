import tkinter as tk
from tkinter import Tk, Button, ttk, PhotoImage
from tkcalendar import Calendar
from pathlib import Path
import platform, json, os
from datetime import datetime
from main import exit_button

abs_path = os.getcwd()
if platform.system() == "Darwin":
    ASSETS_PATH = abs_path + "/assets/frame19"
else:
    ASSETS_PATH = abs_path + "/build/assets/frame19"

class CercaCamere:
    def __init__(self, window):
        self.window = window
        self.window.geometry("862x519")
        self.window.configure(bg="#FAFFFD")

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
            outline=""
        )

        self.arrival_button = Button(
            self.canvas,
            text="Seleziona data di arrivo",
            command=self.open_arrival_calendar,
            bg="#FAFFFD",
            fg="#000716",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            font=("Inter Bold", 12)
        )
        self.arrival_button.place(x=314.0, y=145.0, width=233, height=30)

        self.departure_button = Button(
            self.canvas,
            text="Seleziona data di partenza",
            command=self.open_departure_calendar,
            bg="#FAFFFD",
            fg="#000716",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            font=("Inter Bold", 12)
        )
        self.departure_button.place(x=314.0, y=207.0, width=233, height=30)

        self.canvas.create_text(
            314.0,
            124.0,
            anchor="nw",
            text="Data di arrivo",
            fill="#FFFFFF",
            font=("Quicksand", 16 * -1)
        )

        self.canvas.create_text(
            314.0,
            187.0,
            anchor="nw",
            text="Data di partenza",
            fill="#FFFFFF",
            font=("Quicksand", 16 * -1)
        )
        
        self.canvas.create_text(
            314.0,
            249.0,
            anchor="nw",
            text="Tipologia Camera",
            fill="#FFFFFF",
            font=("Quicksand", 16 * -1)
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
        self.combo.place(x=314.0, y=270, width=233, height=30)

        self.button_images = {
            f"button_{i}": self.load_button_image(f"button_{i}.png") for i in range(1, 1)
        }
        
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.check_availability,
            relief="flat"
        )

        self.button_1.place(
            x=359.0,
            y=339.0,
            width=143.8626708984375,
            height=39.882110595703125
        )

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: exit_button(self.window),
            relief="flat"
        )
        self.button_2.place(
            x=407.0,
            y=439.0,
            width=47.0,
            height=45.0
        )

        self.button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: go_lista_prenotazioni(self.window),
            relief="flat"
        )
        self.button_3.place(
            x=240.0,
            y=444.0,
            width=152.0,
            height=36.0
        )

        self.button_image_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: go_modifica_profilo(self.window),
            relief="flat"
        )
        self.button_4.place(
            x=469.0,
            y=444.0,
            width=152.0,
            height=36.0
        )

        self.window.resizable(False, False)
        
    def open_arrival_calendar(self):
        if platform.system() == "Darwin":
            self.arrival_calendar = tk.Toplevel(self.window)
            self.arrival_calendar.geometry("330x270")
            self.arrival_calendar.title("Seleziona data di arrivo")
        
            cal_arrival = Calendar(self.arrival_calendar, selectmode="day", date_pattern="dd-mm-yyyy", font="Quicksand 14", cursor="hand1")
            cal_arrival.grid(row=0, column=0, padx=10, pady=10)
            
            confirm_button = Button(self.arrival_calendar, text="Conferma", command=self.confirm_arrival_date)
            confirm_button.grid(row=1, column=0, pady=10)
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
            self.departure_calendar = tk.Toplevel(self.window)
            self.departure_calendar.geometry("330x270")
            self.departure_calendar.title("Seleziona data di partenza")
            
            cal_departure = Calendar(self.departure_calendar, selectmode="day", date_pattern="dd-mm-yyyy", 
                                    font="Quicksand 14", cursor="hand1")
            cal_departure.grid(row=0, column=0, padx=10, pady=10)
            
            confirm_button = Button(self.departure_calendar, text="Conferma", command=self.confirm_departure_date)
            confirm_button.grid(row=1, column=0, pady=10)
        else:
            self.departure_calendar = tk.Toplevel(self.window)
            self.departure_calendar.geometry("390x300")
            self.departure_calendar.title("Seleziona data di partenza")
            
            cal_departure = Calendar(self.departure_calendar, selectmode="day", date_pattern="dd-mm-yyyy", 
                                    font="Quicksand 14", cursor="hand1")
            cal_departure.grid(row=0, column=0, padx=10, pady=10)
            
            confirm_button = Button(self.departure_calendar, text="Conferma", command=self.confirm_departure_date)
            confirm_button.grid(row=1, column=0, pady=10)

    def confirm_departure_date(self):
        selected_date = self.departure_calendar.winfo_children()[0].get_date()
        self.departure_button.config(text=selected_date)
        self.departure_calendar.destroy()

    def relative_to_assets(self, path: str) -> Path:
        return Path(ASSETS_PATH) / Path(path)

    def load_button_image(self, image_path):
        abs_path = os.getcwd()
        if platform.system() == "Darwin":
            assets_path = abs_path + "/assets/frame5"
        else:
            assets_path = abs_path + "/build/assets/frame5"

        return tk.PhotoImage(file=Path(assets_path) / Path(image_path))
    
    def check_availability(self):
    # Ottieni il tipo di camera selezionato
        tipo_camera = self.combo_var.get()

        # Ottieni le date di arrivo e partenza
        data_arrivo = datetime.strptime(self.arrival_button.cget("text"), "%d-%m-%Y")
        data_partenza = datetime.strptime(self.departure_button.cget("text"), "%d-%m-%Y")
        print(tipo_camera, data_arrivo, data_partenza)
        # Carica i dati dal file JSON
        if platform.system() == "Darwin":
            with open("data.json", "r") as file:
                data = json.load(file)
        else:
            with open(r"build/data.json", "r") as file:
                data = json.load(file)

        # Cerca la camera corrispondente
        for categoria_camera in data[1]["camere"]:
            for tipo, camere in categoria_camera.items():
                if tipo == tipo_camera:
                    for camera in camere:
                        for numero_camera, prenotazioni in camera.items():
                            for prenotazione in prenotazioni:
                                # Se la prenotazione è vuota, la camera è libera
                                if  prenotazione["arrivo"] == "" and prenotazione["partenza"]=="":
                                    print(f"La camera {numero_camera} è disponibile nell'intervallo selezionato.")
                                    current_prenotazione = {
                                        "arrivo": data_arrivo.strftime("%d-%m-%Y"),
                                        "partenza": data_partenza.strftime("%d-%m-%Y"),
                                        "tipo_camera": tipo_camera
                                        }

                                    # Scrivi i dettagli dell'utente nel file current_user.json
                                    if platform.system() == "Darwin":
                                        with open("current_prenotazione.json", "w") as file:
                                            json.dump(current_prenotazione, file)
                                    else:
                                        with open(r"build/current_prenotazione.json", "w") as file:
                                            json.dump(current_prenotazione, file)
                                    return
                                if prenotazione["arrivo"] and prenotazione["partenza"]:
                                    arrivo_prenotazione = datetime.strptime(prenotazione["arrivo"], "%d-%m-%Y")
                                    partenza_prenotazione = datetime.strptime(prenotazione["partenza"], "%d-%m-%Y")

                    print("Tutte le camere sono disponibili nell'intervallo selezionato.")
                    return
        print("Nessuna camera disponibile nell'intervallo selezionato.")

def go_lista_prenotazioni(window):
    from ListaPrenotazioni import ListaPrenotazioni
    window.destroy()
    root = Tk()
    app = ListaPrenotazioni(root)
    root.mainloop()

def go_modifica_profilo(window):
    from ModificaProfilo import ModificaProfilo
    window.destroy()
    root = Tk()
    app = ModificaProfilo(root)
    root.mainloop()

if __name__ == "__main__":
    root = Tk()
    app = CercaCamere(root)
    root.mainloop()
