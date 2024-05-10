from pathlib import Path
import os, platform, json, re
import tkinter.messagebox
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from main import go_visualizza_prenotazioni_servizi, exit_button, go_back_office_button, go_front_office_button, go_gestione_magazzino, go_gestione_servizi, go_gestione_spa, go_home_button, multiplatform_open_read_data_json, multiplatform_open_write_data_json

abs_path = os.getcwd()

ASSETS_PATH = abs_path + "/assets/frame12"

class ModificaPrenotazioneServizi:
    def __init__(self,window):
        self.window = window
        self.window.geometry("862x519")
        self.window.configure(bg = "#FAFFFD")
        
        self.tipo = None
        self.numero_camera = None
        
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
            341.0,
            110.0,
            731.0,
            410.0,
            fill="#FAFFFD",
            outline=""
        )

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            536.0,
            185.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=398.0,
            y=166.0,
            width=276.0,
            height=37.0
        )

        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            536.0,
            260.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=398.0,
            y=241.0,
            width=276.0,
            height=36.0
        )

        self.canvas.create_text(
            386.0,
            146.0,
            anchor="nw",
            text="Nome servizio",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.canvas.create_text(
            386.0,
            221.0,
            anchor="nw",
            text="Camera",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.button_images = {
            f"button_{i}": self.load_button_image(f"button_{i}.png") for i in range(1, 9)
        }

        self.create_buttons()

        self.window.resizable(False, False)
        
        with open("current_entry_servizi.json", "r") as user_json:
            current_entry_servizi = json.load(user_json)
                
        print(current_entry_servizi, "ciao")
                
        pattern = r'Servizio:\s*([^,]+),\s*Numero Camera:\s*([^"]+)'
        match = re.search(pattern, current_entry_servizi)
        
        if match:
            tipo = match.group(1)
            numero_camera = match.group(2)
        
        print(tipo, numero_camera)
        
        self.entry_1.insert(0, tipo)
        self.entry_2.insert(0, numero_camera)

    def save_changes(self):
        data = multiplatform_open_read_data_json()
        
        with open("current_entry_servizi.json", "r") as user_json:
            current_entry_servizi = json.load(user_json)
                
        pattern = r'Servizio:\s*([^,]+),\s*Numero Camera:\s*([^"]+)'
        match = re.search(pattern, current_entry_servizi)
        tipo = match.group(1)
        numero_camera = match.group(2)
    
        print(tipo, numero_camera)
            
        new_tipo = self.entry_1.get()
        new_numero_camera = self.entry_2.get()
            
        for prenotazione in data[-1]["servizi"]:
            if prenotazione["nome_servizio"] == tipo and prenotazione["numero_camera"] == numero_camera:
                prenotazione["nome_servizio"] = new_tipo
                prenotazione["numero_camera"] = new_numero_camera
                break
                    
        write_data = multiplatform_open_write_data_json(data)
        tkinter.messagebox.showinfo("Avviso", "Modifiche confermate!")
        go_visualizza_prenotazioni_servizi(self.window)
        
        
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
            command=self.save_changes,
            relief="flat"
        )
        self.button_9.place(
            x=442.0,
            y=320.0,
            width=187.0,
            height=49.0
        )

    def invia_prenotazione(self):
        nome_servizio = self.entry_1.get()
        numero_camera = self.entry_2.get()
        
        servizio = {
            "nome_servizio" : nome_servizio,
            "numero_camera" : numero_camera
        }
        
        try:
            with open("data.json", "r") as file:
                data = json.load(file)

            # Assuming you want to append 'servizio' to the 'servizi' list in the last dictionary of 'data'
            servizi = data[-1]["servizi"]
            servizi.append(servizio)
            
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)  # Writing back the entire 'data' dictionary        
            print("Servizio aggiunto con successo")
        except Exception as e:
            print("Si è verificato un errore:", e)

    def relative_to_assets(self,path: str) -> Path:
        return Path(ASSETS_PATH) / Path(path)

    def load_button_image(self, image_path):
        abs_path = os.getcwd()

        assets_path = abs_path + "/assets/frame12"

        return PhotoImage(file=Path(assets_path) / Path(image_path))
    
if __name__ == "__main__":
    root = Tk()
    app = ModificaPrenotazioneServizi(root)
    root.mainloop()