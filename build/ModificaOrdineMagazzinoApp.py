from pathlib import Path
import os, platform, json, re
import tkinter.messagebox
from datetime import datetime, timedelta
from tkinter import ttk, Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
from main import centrare_finestra, multiplatform_open_write_data_json, multiplatform_open_read_data_json, exit_button, go_gestione_spa, go_back_office_button, go_front_office_button, go_gestione_magazzino, go_gestione_servizi, go_home_button

abs_path = os.getcwd()

ASSETS_PATH = abs_path + "/assets/frame13"

class ModificaOrdineMagazzino:
    def __init__(self,window):
        self.window = window
        self.window.geometry("862x519")
        self.window.configure(bg = "#FAFFFD")
        
        self.nome_articolo = None
        self.quantita = None

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
        
        self.combo_var = tk.StringVar()
        self.combo_var.set("")
        self.combo = ttk.Combobox(
            self.canvas,
            textvariable=self.combo_var,
            values=["Lenzuola", "Cuscini", "Materasso", "Topper", "Asciugamani", "Carta igienica", "Spazzolini", "Kit di benvenuto", "Detersivo", "Sapone"],
            state="readonly",
            width=20,
            height=5,
            font=("Quicksand", 16 * -1)
        )
        self.combo.place(x=390.0, y=166, width=299, height=37)

        self.canvas.create_rectangle(
            344.0,
            110.0,
            734.0,
            410.0,
            fill="#FAFFFD",
            outline=""
        )

        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            539.0,
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
            x=401.0,
            y=241.0,
            width=276.0,
            height=36.0
        )

        self.canvas.create_text(
            389.0,
            146.0,
            anchor="nw",
            text="Nome articolo",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.canvas.create_text(
            389.0,
            221.0,
            anchor="nw",
            text="Quantità",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.button_images = {
            f"button_{i}": self.load_button_image(f"button_{i}.png") for i in range(1, 9)
        }

        self.create_buttons()

        self.window.resizable(False, False)

        with open("current_entry_ordine.json", "r") as user_json:
            current_entry = json.load(user_json)

        print(current_entry, "ciao")

        pattern = r'\s*([^,]+),\s*Quantit\u00e0:\s*([^,]+),\s*Arrivo:\s*([^,]+)'
        match = re.search(pattern, current_entry)
        nome_articolo = match.group(1)
        quantita = match.group(2)
        data_ordine_vecchio = match.group(3)
        
        print(nome_articolo, quantita, data_ordine_vecchio, "hola")

        self.combo_var.set(nome_articolo)
        self.entry_2.insert(0, quantita)

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
            command=lambda: self.save_changes(),
            relief="flat"
        )
        self.button_9.place(
            x=463.9482421875,
            y=328.764892578125,
            width=149.4329833984375,
            height=49.16864776611328
        )

    def save_changes(self):
        with open("data.json", "r") as user_file:
            data = json.load(user_file)

        with open("current_entry_ordine.json", "r") as user_json:
            current_entry = json.load(user_json)
        
        print(current_entry)

        pattern = r'\s*([^,]+),\s*Quantit\u00e0:\s*([^,]+),\s*Arrivo:\s*([^,]+)'
        match = re.search(pattern, current_entry)

        if match:
            nome_articolo_vecchio = match.group(1)
            quantita_vecchia = match.group(2)
            data_ordine_vecchio = match.group(3)

            new_nome_articolo = self.combo_var.get()
            new_quantita = self.entry_2.get()
            new_data_ordine = datetime.now().date()
            new_data_spedizione = new_data_ordine + timedelta(days=1)
            new_data_consegna = new_data_ordine + timedelta(days=3)

            print(new_nome_articolo, new_quantita, new_data_ordine, new_data_spedizione, new_data_consegna)

            nuova_prenotazione = {
                "nome_articolo": new_nome_articolo,
                "quantita": new_quantita,
                "data": new_data_ordine.strftime("%d-%m-%Y"),
                "spedizione": new_data_spedizione.strftime("%d-%m-%Y"),
                "consegna": new_data_ordine.strftime("%d-%m-%Y")
            }
            data[-1]["magazzino"].append(nuova_prenotazione)
            print("Aggiunta nuova prenotazione!")
            print(data[-1]["magazzino"], "\n")

    def relative_to_assets(self,path: str) -> Path:
        return Path(ASSETS_PATH) / Path(path)
    
    def load_button_image(self, image_path):
        abs_path = os.getcwd()
        
        assets_path = abs_path + "/assets/frame13"

        return PhotoImage(file=Path(assets_path) / Path(image_path))
            
if __name__ == "__main__":
    root = Tk()
    root.title("Modifica Ordine Magazzino")
    app = ModificaOrdineMagazzino(root)
    centrare_finestra(root)
    root.mainloop()