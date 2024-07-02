from pathlib import Path
import uuid
import os, platform, json, re
from tkcalendar import Calendar
import tkinter.messagebox
from datetime import datetime
from tkinter import Tk, ttk, Canvas, Entry, Text, Button, PhotoImage
from main import multiplatform_open_read_data_json, centrare_finestra, exit_button, go_home_button, go_back_office_button, go_front_office_button, go_gestione_magazzino, go_gestione_servizi, go_gestione_spa
import tkinter as tk

abs = os.getcwd()

ASSETS_PATH = abs + "/assets/frame15"

class ModificaPrenotazioneAdmin:
    def __init__(self,window):
        self.window = window
        self.window.geometry("862x519")
        self.window.configure(bg = "#FAFFFD")

        self.arrival_calendar = None
        self.departure_calendar = None

        data = multiplatform_open_read_data_json()

        with open("current_entry_prenotazione.json", "r") as prenotazione_json:
            current_prenotazione = json.load(prenotazione_json)

        self.arrivo = ""
        self.partenza = ""
        self.tipo_camera = ""

        pattern = r'(\d{2}-\d{2}-\d{4}), (\d{2}-\d{2}-\d{4}), (.+)'

        match = re.search(pattern, current_prenotazione)
        if match:
            self.arrivo = match.group(1)
            self.partenza = match.group(2)
            self.tipo_camera = match.group(3)
            i = 0

                      
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
        self.combo.place(x=430.0, y=283.0, width=225, height=25)
        
        self.arrival_button = Button(
            self.canvas,
            text=self.arrivo,
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
            text=self.partenza,
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

        if data:
            for user in data[0]["users"]:
                if (user["role"] == "admin"):
                    prenotazioni = user.get('prenotazioni', [])
                    for prenotazione in prenotazioni:
                        arrivo_utente = prenotazione["arrivo"]
                        partenza_utente = prenotazione["partenza"]
                        tipo_camera = prenotazione["tipo_camera"]

                        if (arrivo_utente == self.arrivo and partenza_utente == self.partenza and tipo_camera == self.tipo_camera):
                            nome = prenotazione["nome"]
                            cognome = prenotazione["cognome"]
                            cellulare = prenotazione["cellulare"]
                            email = prenotazione["email"]

                            self.entry_1.insert(0, nome)
                            self.entry_2.insert(0, cognome)
                            self.entry_3.insert(0, email)
                            self.entry_7.insert(0, cellulare)
                    
                elif(user["role"] == "utente"):
                    prenotazioni = user.get('prenotazioni', [])
                    for prenotazione in prenotazioni:
                        arrivo_utente = prenotazione["arrivo"]
                        partenza_utente = prenotazione["partenza"]
                        tipo_camera = prenotazione ["tipo_camera"]

                        if(arrivo_utente == self.arrivo and partenza_utente == self.partenza and tipo_camera == self.tipo_camera):
                            nome = user["nome"]
                            cognome = user["cognome"]
                            cellulare = user["telefono"]
                            email = user["email"]

                            self.entry_1.insert(0, nome)
                            self.entry_2.insert(0, cognome)
                            self.entry_3.insert(0, email)
                            self.entry_7.insert(0, cellulare)

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
            command=lambda: (self.check_availability(), self.modifica_prenotazione(), go_front_office_button(self.window)),
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

        camera_trovata = False
        for categoria_camera in data[1]['camere']:
            if tipo_camera in categoria_camera:
                for camera in categoria_camera[tipo_camera]:
                    for numero_camera, prenotazioni in camera.items():
                        camera_disponibile = True
                        for prenotazione in prenotazioni:
                            if prenotazione["arrivo"] and prenotazione["partenza"]:
                                arrivo_prenotazione = datetime.strptime(prenotazione["arrivo"], "%d-%m-%Y")
                                partenza_prenotazione = datetime.strptime(prenotazione["partenza"], "%d-%m-%Y")
                                if not(data_arrivo >= partenza_prenotazione or data_partenza <= arrivo_prenotazione):
                                    camera_disponibile = False
                                    break
                        if camera_disponibile:
                            id_prenotazione = uuid.uuid4()
                            current_prenotazione_admin = {
                                "arrivo": data_arrivo.strftime("%d-%m-%Y"),
                                "partenza": data_partenza.strftime("%d-%m-%Y"),
                                "tipo_camera": tipo_camera,
                                "id_prenotazione": str(id_prenotazione)
                            }
                            with open("current_prenotazione_admin.json", "w") as file:
                                json.dump(current_prenotazione_admin, file, indent=4)
                            camera_trovata = True

                            prenotazione_modificata_admin = {
                                "nome": self.entry_1.get(),
                                "cognome": self.entry_2.get(),
                                "cellulare": self.entry_7.get(),
                                "email": self.entry_3.get(),
                                "tipo_camera": self.combo_var.get(),
                                "arrivo": self.arrival_button.cget("text"),
                                "partenza": self.departure_button.cget("text"),
                                "id_prenotazione": str(id_prenotazione),
                                "role": "admin"
                            }

                            prenotazione_modificata_utente = {
                                "arrivo": self.arrival_button.cget("text"),
                                "partenza": self.departure_button.cget("text"),
                                "tipo_camera": self.combo_var.get(),
                                "id_prenotazione": str(id_prenotazione),
                                "role": "utente"
                            }

                            for user in data[0]["users"]:
                                for prenotazione in user.get("prenotazioni", []):
                                    if prenotazione["arrivo"] == self.arrivo and prenotazione["partenza"] == self.partenza and prenotazione["tipo_camera"] == self.tipo_camera and prenotazione["role"] == "admin":
                                        prenotazione.update(prenotazione_modificata_admin)
                                        break
                                    elif(prenotazione["arrivo"] == self.arrivo and prenotazione["partenza"] == self.partenza and prenotazione["tipo_camera"] and prenotazione["role"] == "utente"):
                                        prenotazione.update(prenotazione_modificata_utente)
                                
                            with open("data.json", "w") as file:
                                json.dump(data, file, indent=4)
        
                            break

                    if camera_trovata:
                        break  # Exit the loop since we found an available camera
            if camera_trovata:
                break  # Exit the loop since we found an available camera

        if not camera_trovata:
            print("Nessuna camera disponibile nell'intervallo selezionato")

        data = multiplatform_open_read_data_json()

        with open("current_entry_prenotazione.json", "r") as prenotazione_json:
            current_entry_admin = json.load(prenotazione_json)

        pattern = r'(\d{2}-\d{2}-\d{4}), (\d{2}-\d{2}-\d{4}), (.+)'

        match = re.search(pattern, current_entry_admin)
        if match:
            arrivo = match.group(1)
            partenza = match.group(2)
            tipo_camera = match.group(3)

            for categoria_camera in data[1]["camere"]:
                for tipo, camere in categoria_camera.items():
                    if tipo == tipo_camera:
                        for camera in camere:
                            for numero_camera, dettagli in camera.items():
                                for dettaglio in dettagli:
                                    if dettaglio['arrivo'] == self.arrivo and dettaglio['partenza'] == self.partenza and dettaglio["tipo_camera"] == self.tipo_camera:
                                        dettaglio['arrivo'] = self.arrival_button.cget("text")
                                        dettaglio['partenza'] = self.departure_button.cget("text")
                                        dettaglio['tipo_camera'] = self.combo_var.get()

                                        dettagli.remove(dettaglio)

                                        if dettaglio['tipo_camera'] == "Camera Singola":
                                            numero_ospiti = 1
                                        elif dettaglio['tipo_camera'] == "Camera Doppia":
                                            numero_ospiti = 2
                                        elif dettaglio['tipo_camera'] == "Camera Tripla":
                                            numero_ospiti = 3
                                        elif dettaglio['tipo_camera'] == "Camera Quadrupla":
                                            numero_ospiti = 4
                                        else:
                                            numero_ospiti = None

                                        camera_disponibile = False
                                        for camera_tipo in data[1]["camere"]:
                                            if dettaglio["tipo_camera"] in camera_tipo:
                                                prenotazioni_camera = camera_tipo[dettaglio["tipo_camera"]]
                                                for numero_camera, prenotazioni in prenotazioni_camera[0].items():
                                                    cella_disponibile = True
                                                    for prenotazione in prenotazioni:
                                                        if prenotazione["arrivo"] == "" and prenotazione["partenza"] == "":
                                                            continue  # La cella è libera, continua con la prossima camera
                                                        elif (datetime.strptime(dettaglio["arrivo"], "%d-%m-%Y") >= datetime.strptime(prenotazione["partenza"], "%d-%m-%Y") or
                                                            datetime.strptime(dettaglio["partenza"], "%d-%m-%Y") <= datetime.strptime(prenotazione["arrivo"], "%d-%m-%Y")):
                                                            continue  # Le date della prenotazione non si sovrappongono, continua con la prossima camera
                                                        else:
                                                            cella_disponibile = False
                                                            break  # La cella è occupata, esci dal ciclo
                                                    if cella_disponibile:
                                                        prenotazioni.append({
                                                            "arrivo": dettaglio["arrivo"],
                                                            "partenza": dettaglio["partenza"],
                                                            "tipo_camera": dettaglio["tipo_camera"],
                                                            "id_prenotazione": dettaglio['id_prenotazione']
                                                        })
                                                        break  # Esce dal ciclo delle camere disponibili

                                        # Salva le modifiche nel file JSON
                                        with open("data.json", "w") as file:
                                            json.dump(data, file, indent=4)
                                        tkinter.messagebox.showinfo("Avviso", "Modifiche confermate!")
                                        return  # Esce dal ciclo delle camere disponibili

            print("Nessuna corrispondenza trovata per aggiornare le prenotazioni delle camere.")

    def modifica_prenotazione(self):
        data = multiplatform_open_read_data_json()

        with open("current_entry_prenotazione.json", "r") as prenotazione_json:
            current_entry_admin = json.load(prenotazione_json)

        pattern = r'(\d{2}-\d{2}-\d{4}), (\d{2}-\d{2}-\d{4}), (.+)'

        match = re.search(pattern, current_entry_admin)
        if match:
            arrivo = match.group(1)
            partenza = match.group(2)
            tipo_camera = match.group(3)
        
        if data:
            for user in data[0]['users']:
                for prenotazione in user.get('prenotazioni', []):
                    if prenotazione['arrivo'] == self.arrivo and prenotazione['partenza'] == self.partenza and prenotazione['tipo_camera'] == self.tipo_camera:
                        prenotazione['arrivo'] = self.arrival_button.cget("text")
                        prenotazione['partenza'] = self.departure_button.cget("text")
                        prenotazione['tipo_camera'] = self.combo_var.get()

                        break  # Exit the loop after updating the correct booking

            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)

            for categoria_camera in data[1]["camere"]:
                for tipo, camere in categoria_camera.items():
                    if tipo == tipo_camera:
                        for camera in camere:
                            for numero_camera, dettagli in camera.items():
                                for dettaglio in dettagli:
                                    if dettaglio['arrivo'] == self.arrivo and dettaglio['partenza'] == self.partenza and dettaglio["tipo_camera"] == self.tipo_camera:
                                        dettaglio['arrivo'] = self.arrival_button.cget("text")
                                        dettaglio['partenza'] = self.departure_button.cget("text")
                                        dettaglio['tipo_camera'] = self.combo_var.get()

                                        dettagli.remove(dettaglio)

                                        if dettaglio['tipo_camera'] == "Camera Singola":
                                            numero_ospiti = 1
                                        elif dettaglio['tipo_camera'] == "Camera Doppia":
                                            numero_ospiti = 2
                                        elif dettaglio['tipo_camera'] == "Camera Tripla":
                                            numero_ospiti = 3
                                        elif dettaglio['tipo_camera'] == "Camera Quadrupla":
                                            numero_ospiti = 4
                                        else:
                                            numero_ospiti = None

                                        camera_disponibile = False
                                        for camera_tipo in data[1]["camere"]:
                                            if dettaglio["tipo_camera"] in camera_tipo:
                                                prenotazioni_camera = camera_tipo[dettaglio["tipo_camera"]]
                                                for numero_camera, prenotazioni in prenotazioni_camera[0].items():
                                                    cella_disponibile = True
                                                    for prenotazione in prenotazioni:
                                                        if prenotazione["arrivo"] == "" and prenotazione["partenza"] == "":
                                                            continue  # La cella è libera, continua con la prossima camera
                                                        elif (datetime.strptime(dettaglio["arrivo"], "%d-%m-%Y") >= datetime.strptime(prenotazione["partenza"], "%d-%m-%Y") or
                                                            datetime.strptime(dettaglio["partenza"], "%d-%m-%Y") <= datetime.strptime(prenotazione["arrivo"], "%d-%m-%Y")):
                                                            continue  # Le date della prenotazione non si sovrappongono, continua con la prossima camera
                                                        else:
                                                            cella_disponibile = False
                                                            break  # La cella è occupata, esci dal ciclo
                                                    if cella_disponibile:
                                                        prenotazioni.append({
                                                            "arrivo": dettaglio["arrivo"],
                                                            "partenza": dettaglio["partenza"],
                                                            "tipo_camera": dettaglio["tipo_camera"],
                                                            "id_prenotazione": dettaglio['id_prenotazione']
                                                        })
                                                        break  # Esce dal ciclo delle camere disponibili

                                        # Salva le modifiche nel file JSON
                                        with open("data.json", "w") as file:
                                            json.dump(data, file, indent=4)
                                        return  # Esce dal ciclo delle camere disponibili

    def load_button_image(self, image_path):
        abs_path = os.getcwd()

        assets_path = abs_path + "/assets/frame15"

        return PhotoImage(file=Path(assets_path) / Path(image_path))


    def relative_to_assets(self,path: str) -> Path:
        return Path(ASSETS_PATH) / Path(path)

if __name__ == "__main__":
    root = Tk()
    root.title("Modifica Prenotazioni")
    app = ModificaPrenotazioneAdmin(root)
    centrare_finestra(root)
    root.mainloop()