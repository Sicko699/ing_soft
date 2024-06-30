from pathlib import Path
import os, platform, json, re
import tkinter.messagebox
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from main import exit_button, go_back_office_button, go_front_office_button, go_gestione_magazzino, go_gestione_servizi, go_gestione_spa, go_home_button, multiplatform_open_read_data_json

abs_path = os.getcwd()

ASSETS_PATH = abs_path + "/assets/frame14"

class VisualizzazionePrenotazioni:
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
            321.0,
            32.0,
            758.0,
            488.0,
            fill="#FAFFFD",
            outline=""
        )

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            539.5,
            82.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=358.0,
            y=63.0,
            width=363.0,
            height=36.0
        )

        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            539.5,
            132.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=358.0,
            y=113.0,
            width=363.0,
            height=36.0
        )

        self.entry_image_3 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            539.5,
            182.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_3.place(
            x=358.0,
            y=163.0,
            width=363.0,
            height=36.0
        )

        self.entry_image_4 = PhotoImage(file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            539.5,
            232.0,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_4.place(
            x=358.0,
            y=213.0,
            width=363.0,
            height=36.0
        )

        self.entry_image_5 = PhotoImage(file=self.relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            539.5,
            282.0,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_5.place(
            x=358.0,
            y=263.0,
            width=363.0,
            height=36.0
        )

        self.entry_image_6 = PhotoImage(file=self.relative_to_assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(
            539.5,
            332.0,
            image=self.entry_image_6
        )
        self.entry_6 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_6.place(
            x=358.0,
            y=313.0,
            width=363.0,
            height=36.0
        )

        self.entry_image_7 = PhotoImage(file=self.relative_to_assets("entry_7.png"))
        self.entry_bg_7 = self.canvas.create_image(
            539.5,
            382.0,
            image=self.entry_image_7
        )
        self.entry_7 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_7.place(
            x=358.0,
            y=363.0,
            width=363.0,
            height=36.0
        )

        self.entry_image_8 = PhotoImage(file=self.relative_to_assets("entry_8.png"))
        self.entry_bg_8 = self.canvas.create_image(
            539.5,
            432.0,
            image=self.entry_image_8
        )
        self.entry_8 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_8.place(
            x=358.0,
            y=413.0,
            width=363.0,
            height=36.0
        )

        self.button_images = {
            f"button_{i}": self.load_button_image(f"button_{i}.png") for i in range(1, 24)
        }

        self.create_buttons()

        self.window.resizable(False, False)
        
        
        data = multiplatform_open_read_data_json()

        numero_prenotazioni = -1
        
        self.entry_list = []

        for tipo_camera, prenotazioni in data[1]['camere'][0].items():
            # Itera sulle prenotazioni della camera
            for camera_numero, camera_prenotazioni in prenotazioni[0].items():
                # Stampare solo i dati richiesti
                for prenotazione in camera_prenotazioni:
                    if prenotazione['arrivo'] and prenotazione['partenza']:
                        arrivo = prenotazione['arrivo']
                        partenza = prenotazione['partenza']
                        
                        '''
                        print("Arrivo:", prenotazione['arrivo'])
                        print("Partenza:", prenotazione['partenza'])
                        print("Nome:", prenotazione['nome'])
                        print("Cognome:", prenotazione['cognome'])
                        print("Numero ospiti:", prenotazione['numero_ospiti'])
                        print("Tipo camera:", prenotazione['tipo_camera'])
                        print()
                        '''
                        numero_prenotazioni +=1
                        
                        if numero_prenotazioni <= 7:
                            entry_value = f"{arrivo}, {partenza}, {tipo_camera}"
                            entry = Entry(
                                bd=0,
                                bg="#EAEEEC",
                                fg="#000716",
                                highlightthickness=0
                            )
                            entry.place(
                                x=366.0,
                                y=63.0 + numero_prenotazioni * 50,
                                width=275.0,
                                height=36.0
                            )
                            entry.insert(0, entry_value)
                            self.entry_list.append(entry)
                            
    def save_entry(self, index):
        current_entry = self.entry_list[index].get()
        
        with open("current_entry_prenotazione.json", "w") as file:
            json.dump(current_entry, file)
        
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
            command=lambda: (self.save_entry(0), go_modifica_prenotazioni_admin(self.window)),
            relief="flat"
        )
        self.button_9.place(
            x=690.0,
            y=68.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_10 = PhotoImage(file=self.relative_to_assets("button_10.png"))
        self.button_10 = Button(
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.save_entry(3), go_modifica_prenotazioni_admin(self.window)),
            relief="flat"
        )
        self.button_10.place(
            x=690.0,
            y=218.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_11 = PhotoImage(file=self.relative_to_assets("button_11.png"))
        self.button_11 = Button(
            image=self.button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.save_entry(2), go_modifica_prenotazioni_admin(self.window)),
            relief="flat"
        )
        self.button_11.place(
            x=690.0,
            y=168.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_12 = PhotoImage(file=self.relative_to_assets("button_12.png"))
        self.button_12 = Button(
            image=self.button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.save_entry(1), go_modifica_prenotazioni_admin(self.window)),
            relief="flat"
        )
        self.button_12.place(
            x=690.0,
            y=118.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_13 = PhotoImage(file=self.relative_to_assets("button_13.png"))
        self.button_13 = Button(
            image=self.button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.save_entry(4), go_modifica_prenotazioni_admin(self.window)),
            relief="flat"
        )
        self.button_13.place(
            x=690.0,
            y=268.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_14 = PhotoImage(file=self.relative_to_assets("button_14.png"))
        self.button_14 = Button(
            image=self.button_image_14,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.save_entry(5), go_modifica_prenotazioni_admin(self.window)),
            relief="flat"
        )
        self.button_14.place(
            x=690.0,
            y=318.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_15 = PhotoImage(file=self.relative_to_assets("button_15.png"))
        self.button_15 = Button(
            image=self.button_image_15,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.save_entry(7), go_modifica_prenotazioni_admin(self.window)),
            relief="flat"
        )
        self.button_15.place(
            x=690.0,
            y=418.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_16 = PhotoImage(file=self.relative_to_assets("button_16.png"))
        self.button_16 = Button(
            image=self.button_image_16,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.save_entry(6), go_modifica_prenotazioni_admin(self.window)),
            relief="flat"
        )
        self.button_16.place(
            x=690.0,
            y=368.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_17 = PhotoImage(file=self.relative_to_assets("button_17.png"))
        self.button_17 = Button(
            image=self.button_image_17,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.save_entry(0), self.elimina_prenotazione()),
            relief="flat"
        )
        self.button_17.place(
            x=654.0,
            y=68.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_18 = PhotoImage(file=self.relative_to_assets("button_18.png"))
        self.button_18 = Button(
            image=self.button_image_18,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.save_entry(1), self.elimina_prenotazione()),
            relief="flat"
        )
        self.button_18.place(
            x=654.0,
            y=118.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_19 = PhotoImage(file=self.relative_to_assets("button_19.png"))
        self.button_19 = Button(
            image=self.button_image_19,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.save_entry(2), self.elimina_prenotazione()),
            relief="flat"
        )
        self.button_19.place(
            x=654.0,
            y=168.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_20 = PhotoImage(file=self.relative_to_assets("button_20.png"))
        self.button_20 = Button(
            image=self.button_image_20,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.save_entry(3), self.elimina_prenotazione()),
            relief="flat"
        )
        self.button_20.place(
            x=654.0,
            y=218.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_21 = PhotoImage(file=self.relative_to_assets("button_21.png"))
        self.button_21 = Button(
            image=self.button_image_21,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.save_entry(4), self.elimina_prenotazione()),
            relief="flat"
        )
        self.button_21.place(
            x=654.0,
            y=268.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_22 = PhotoImage(file=self.relative_to_assets("button_22.png"))
        self.button_22 = Button(
            image=self.button_image_22,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.save_entry(5), self.elimina_prenotazione()),
            relief="flat"
        )
        self.button_22.place(
            x=654.0,
            y=318.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_23 = PhotoImage(file=self.relative_to_assets("button_23.png"))
        self.button_23 = Button(
            image=self.button_image_23,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.save_entry(6), self.elimina_prenotazione()),
            relief="flat"
        )
        self.button_23.place(
            x=654.0,
            y=368.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_24 = PhotoImage(file=self.relative_to_assets("button_24.png"))
        self.button_24 = Button(
            image=self.button_image_24,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.save_entry(7), self.elimina_prenotazione()),
            relief="flat"
        )
        self.button_24.place(
            x=654.0,
            y=418.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

    def elimina_prenotazione(self):
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
                prenotazioni = user.get('prenotazioni', [])
                for prenotazione in prenotazioni:
                    if prenotazione['arrivo'] == arrivo and prenotazione['partenza'] == partenza and prenotazione['tipo_camera'] == tipo_camera:
                        prenotazioni.remove(prenotazione)

                    with open("data.json", "w") as file:
                        json.dump(data, file, indent=4)

            for categoria_camera in data[1]['camere']:
                for tipo, camere in categoria_camera.items():
                    if tipo == tipo_camera:
                        for camera in camere:
                            for numero_camera, dettagli in camera.items():
                                for dettaglio in dettagli:
                                    if dettaglio['arrivo'] == arrivo and dettaglio['partenza'] == partenza and dettaglio['tipo_camera'] == tipo_camera:
                                        dettagli.remove(dettaglio)
                                    
                                    with open("data.json", "w") as file:
                                        json.dump(data, file, indent=4)

            tkinter.messagebox.showinfo("Avviso", "Prenotazione eliminata!")
            go_visualizzazione_prenotazioni(self.window)

    def relative_to_assets(self,path: str) -> Path:
        return Path(ASSETS_PATH) / Path(path)

    def load_button_image(self, image_path):
        abs_path = os.getcwd()
        
        assets_path = abs_path + "/assets/frame14"

        return PhotoImage(file=Path(assets_path) / Path(image_path))

def centrare_finestra(window):
    window.update_idletasks()
    larghezza_finestra = window.winfo_width()
    altezza_finestra = window.winfo_height()
    schermo_larghezza = window.winfo_screenwidth()
    schermo_altezza = window.winfo_screenheight()
    x = (schermo_larghezza - larghezza_finestra) // 2
    y = (schermo_altezza - altezza_finestra) // 2
    window.geometry('{}x{}+{}+{}'.format(larghezza_finestra, altezza_finestra, x, y))

def go_visualizzazione_prenotazioni(window):
    from VisualizzazionePrenotazioniApp import VisualizzazionePrenotazioni
    window.destroy()
    root = Tk()
    root.title("Visualizzazione Prenotazioni")
    app = VisualizzazionePrenotazioni(root)
    centrare_finestra(root)
    root.mainloop()

def go_modifica_prenotazioni_admin(window):
    from ModificaPrenotazioneAdmin import ModificaPrenotazioneAdmin
    window.destroy()
    root = Tk()
    root.title("Modifica Prenotazioni Admin")
    app = ModificaPrenotazioneAdmin(root)
    centrare_finestra(root)
    root.mainloop()

if __name__ == "__main__":
    root = Tk()
    root.title("Visualizzazione Prenotazioni")
    app = VisualizzazionePrenotazioni(root)
    centrare_finestra(root)
    root.mainloop()