from pathlib import Path
import os, platform, json
from datetime import datetime, timedelta
from tkinter import ttk, Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
from main import multiplatform_open_write_data_json, multiplatform_open_read_data_json, exit_button, go_gestione_spa, go_back_office_button, go_front_office_button, go_gestione_magazzino, go_gestione_servizi, go_home_button

abs_path = os.getcwd()

ASSETS_PATH = abs_path + "/assets/frame13"

class NuovoOrdineMagazzino:
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
            command=lambda: self.invia_ordine(),
            relief="flat"
        )
        self.button_9.place(
            x=463.9482421875,
            y=328.764892578125,
            width=149.4329833984375,
            height=49.16864776611328
        )

    def relative_to_assets(self,path: str) -> Path:
        return Path(ASSETS_PATH) / Path(path)
    
    def load_button_image(self, image_path):
        abs_path = os.getcwd()
        
        assets_path = abs_path + "/assets/frame13"

        return PhotoImage(file=Path(assets_path) / Path(image_path))

    def invia_ordine(self):
        nome_articolo = self.combo_var.get()
        quantita = self.entry_2.get()

        # Calcola le date di spedizione e consegna
        oggi = datetime.now().date()
        data_spedizione = oggi + timedelta(days=1)
        data_consegna = oggi + timedelta(days=3)

        ordine = {
            "nome_articolo": nome_articolo,
            "quantita": quantita,
            "data": oggi.strftime("%d-%m-%Y"),
            "spedizione": data_spedizione.strftime("%d-%m-%Y"),
            "consegna": data_consegna.strftime("%d-%m-%Y")
        }

        # Stampa dell'ordine per il controllo
        print("Ordine da aggiungere:", ordine)

        # Tentativo di leggere e aggiornare il file JSON
        try:
            data = multiplatform_open_read_data_json()
            # Aggiungi l'ordine al magazzino
            magazzino = data[3]["magazzino"]  # Assumendo che gli ordini magazzino siano nel quarto elemento di data
            magazzino.append(ordine)

            write_data = multiplatform_open_write_data_json(data)
            
            print("Ordine aggiunto con successo al file JSON.")
        except Exception as e:
            print("Si è verificato un errore durante l'aggiunta dell'ordine al file JSON:", e)

            
if __name__ == "__main__":
    root = Tk()
    app = NuovoOrdineMagazzino(root)
    root.mainloop()