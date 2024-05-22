from pathlib import Path
import os, platform, json
from tkcalendar import Calendar
from datetime import datetime
from tkinter import Tk, ttk, Canvas, Entry, Text, Button, PhotoImage
from main import centrare_finestra, exit_button, go_home_button, go_back_office_button, go_front_office_button, go_gestione_magazzino, go_gestione_servizi, go_gestione_spa
import tkinter as tk

abs = os.getcwd()

ASSETS_PATH = abs + "/assets/frame15"

class InserimentoPrenotazione:
    def __init__(self,window):
        self.window = window
        self.window.geometry("862x519")
        self.window.configure(bg = "#FAFFFD")

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
            outline=""
        )
        
        self.canvas.create_rectangle(
            374.0,
            34.0,
            708.0,
            486.0,
            fill="#FAFFFD",
            outline=""
        )

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            541.5,
            88.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=437.0,
            y=74.0,
            width=209.0,
            height=26.0
        )

        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            541.5,
            140.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=437.0,
            y=126.0,
            width=209.0,
            height=26.0
        )

        self.entry_image_3 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            541.5,
            244.5,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_3.place(
            x=437.0,
            y=231.0,
            width=209.0,
            height=25.0
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
        self.combo.place(x=430.0, y=283.0, width=225, height=25)
        
        self.arrival_button = Button(
            self.canvas,
            text="Seleziona data di arrivo",
            command=lambda: self.open_arrival_calendar(),
            bg="#FAFFFD",
            fg="#000716",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            font=("Inter Bold", 12)
        )
        self.arrival_button.place(x=437.0, y=335.0, width=233, height=30)

        self.departure_button = Button(
            self.canvas,
            text="Seleziona data di partenza",
            command=lambda: self.open_departure_calendar(),
            bg="#FAFFFD",
            fg="#000716",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            font=("Inter Bold", 12)
        )
        self.departure_button.place(x=437.0, y=388.0, width=233, height=30)

        self.canvas.create_text(
            431.0,
            317.0,
            anchor="nw",
            text="Check-in",
            fill="#000000",
            font=("Quicksand Medium", 14 * -1)
        )

        self.canvas.create_text(
            431.0,
            370.0,
            anchor="nw",
            text="Check-out",
            fill="#000000",
            font=("Quicksand Medium", 14 * -1)
        )

        self.canvas.create_text(
            431.0,
            213.0,
            anchor="nw",
            text="Email",
            fill="#000000",
            font=("Quicksand Medium", 14 * -1)
        )

        self.entry_image_7 = PhotoImage(file=self.relative_to_assets("entry_7.png"))
        self.entry_bg_7 = self.canvas.create_image(
            541.5,
            192.5,
            image=self.entry_image_7
        )
        self.entry_7 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_7.place(
            x=437.0,
            y=179.0,
            width=209.0,
            height=25.0
        )

        self.canvas.create_text(
            431.0,
            160.0,
            anchor="nw",
            text="Cellulare",
            fill="#000000",
            font=("Quicksand Medium", 14 * -1)
        )

        self.canvas.create_text(
            431.0,
            55.0,
            anchor="nw",
            text="Nome",
            fill="#000000",
            font=("Quicksand Medium", 14 * -1)
        )
        
        self.canvas.create_text(
            431.0,
            107.0,
            anchor="nw",
            text="Cognome",
            fill="#000000",
            font=("Quicksand Medium", 14 * -1)
        )

        self.canvas.create_text(
            431.0,
            265.0,
            anchor="nw",
            text="Tipo camera",
            fill="#000000",
            font=("Quicksand Medium", 14 * -1)
        )
        
        self.button_images = {
            f"button_{i}": self.load_button_image(f"button_{i}.png") for i in range(1, 9)
        }

        self.create_buttons()

        self.window.resizable(False, False)

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
            
            cal_departure = Calendar(self.departure_calendar, selectmode="day", date_pattern="dd-mm-yyyy", 
                                    font="Quicksand 14", cursor="hand1")
            cal_departure.grid(row=0, column=0, padx=10, pady=10)
            
            confirm_button = Button(self.departure_calendar, text="Conferma", command=self.confirm_departure_date)
            confirm_button.grid(row=1, column=0, pady=10)

    def confirm_departure_date(self):
        selected_date = self.departure_calendar.winfo_children()[0].get_date()
        self.departure_button.config(text=selected_date)
        self.departure_calendar.destroy()

        
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
            command=lambda: go_back_office_button(self.window),
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

        self.button_image_9 = PhotoImage(file=self.relative_to_assets("button_9.png"))
        self.button_9 = Button(
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.update_data_json(), self.check_availability(), go_front_office_button(self.window)),
            relief="flat"
        )
        self.button_9.place(
            x=485.0224609375,
            y=432.7666015625,
            width=111.9908447265625,
            height=34.65187454223633
        )

    def check_availability(self):

        tipo_camera = self.combo_var.get()

        data_arrivo = datetime.strptime(self.arrival_button.cget("text"), "%d-%m-%Y")
        data_partenza = datetime.strptime(self.departure_button.cget("text"), "%d-%m-%Y")

        with open("data.json", "r") as file:
            data = json.load(file)

        for categoria_camera in data[1]['camere']:
            for tipo, camere in categoria_camera.items():
                if tipo == tipo_camera:
                    for camera in camere:
                        for numero_camera, prenotazioni in camera.items():
                            for prenotazione in prenotazioni:
                                if prenotazione["arrivo"] == "" and prenotazione["partenza"] == "":
                                    print(f"La camera {numero_camera} è disponibile nell'intervallo selezionato")
                                    current_prenotazione_admin = {
                                        "arrivo": data_arrivo.strftime("%d-%m-%Y"),
                                        "partenza": data_partenza.strftime("%d-%m-%Y"),
                                        "tipo_camera": tipo_camera
                                    }
                                    
                                    with open("current_prenotazione_admin.json", "w") as file:
                                        write_current_prenotazione = json.dump(current_prenotazione_admin, file)
                                        return write_current_prenotazione
                                    return
                                if prenotazione["arrivo"] and prenotazione["partenza"]:
                                    arrivo_prenotazione = datetime.strptime(prenotazione["arrivo"], "%d-%m-%Y")
                                    partenza_prenotazione = datetime.strptime(prenotazione["partenza"], "%d-%m-%Y")
                    print("Tutte le camere disponibili nell'intervallo selezionato.")
                    return
        print("Nessuna camera disponibile nell'intervallo selezionato")

    def update_data_json(self):
        
        with open("data.json", "r") as file:
            data_json = json.load(file)
        
        with open("current_prenotazione_admin.json", "r") as file:
            current_prenotazione = json.load(file)

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

        camera_disponibile = False
        for camera in data_json[1]['camere']:
            if current_prenotazione["tipo_camera"] in camera:
                prenotazioni_camera = camera[current_prenotazione["tipo_camera"]]
                for numero_camera, prenotazioni in prenotazioni_camera[0].items():
                    camera_disponibile = True
                    for prenotazione in prenotazioni:
                        if prenotazione["arrivo"] == "" and prenotazione["partenza"] == "":
                            continue
                        elif(current_prenotazione["arrivo"] >= prenotazione["partenza"] or
                             current_prenotazione["partenza"] <= prenotazione["arrivo"]):
                            continue
                        else:
                            camera_disponibile = False
                            break
                    if camera_disponibile:
                        prenotazioni.append({
                            "arrivo": current_prenotazione["arrivo"],
                            "partenza": current_prenotazione["partenza"]
                        })

                        camera_disponibile = True
                        break
                else:
                    continue
                break
        
        if not camera_disponibile:
            print("Non ci sono camere disponibili per la prenotazione")
            return

        with open("data.json", "w") as file:
            write_data = json.dump(data_json, file, indent=4)
        
        print("Dari della prenotazione aggiornati con successo")

    def load_button_image(self, image_path):
        abs_path = os.getcwd()

        assets_path = abs_path + "/assets/frame15"

        return PhotoImage(file=Path(assets_path) / Path(image_path))


    def relative_to_assets(self,path: str) -> Path:
        return Path(ASSETS_PATH) / Path(path)
    
if __name__ == "__main__":
    root = Tk()
    root.title("Inserimento Prenotazioni")
    app = InserimentoPrenotazione(root)
    centrare_finestra(root)
    root.mainloop()