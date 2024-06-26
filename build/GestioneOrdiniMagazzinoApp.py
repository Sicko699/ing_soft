from pathlib import Path
import os
import platform
import json
from datetime import datetime  # Importato per gestire le date
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from main import (
    go_modifica_ordine_magazzino,
    exit_button,
    go_home_button,
    go_front_office_button,
    go_back_office_button,
    go_gestione_magazzino,
    go_gestione_servizi,
    go_gestione_spa,
    multiplatform_open_read_data_json,
    centrare_finestra
)

abs_path = os.getcwd()
ASSETS_PATH = abs_path + "/assets/frame10"


class GestioneOrdiniMagazzino:
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
            outline=""
        )

        self.canvas.create_rectangle(
            315.0,
            25.0,
            752.0,
            494.0,
            fill="#FAFFFD",
            outline=""
        )

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            533.5,
            72.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=352.0,
            y=53.0,
            width=363.0,
            height=36.0
        )

        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            533.5,
            122.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=352.0,
            y=103.0,
            width=363.0,
            height=36.0
        )

        self.entry_image_3 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            533.5,
            172.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_3.place(
            x=352.0,
            y=153.0,
            width=363.0,
            height=36.0
        )

        self.entry_image_4 = PhotoImage(file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            533.5,
            222.0,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_4.place(
            x=352.0,
            y=203.0,
            width=363.0,
            height=36.0
        )

        self.entry_image_5 = PhotoImage(file=self.relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            533.5,
            272.0,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_5.place(
            x=352.0,
            y=253.0,
            width=363.0,
            height=36.0
        )

        self.entry_image_6 = PhotoImage(file=self.relative_to_assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(
            533.5,
            322.0,
            image=self.entry_image_6
        )
        self.entry_6 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_6.place(
            x=352.0,
            y=303.0,
            width=363.0,
            height=36.0
        )

        self.entry_image_7 = PhotoImage(file=self.relative_to_assets("entry_7.png"))
        self.entry_bg_7 = self.canvas.create_image(
            533.5,
            372.0,
            image=self.entry_image_7
        )
        self.entry_7 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_7.place(
            x=352.0,
            y=353.0,
            width=363.0,
            height=36.0
        )

        self.button_images = {
            f"button_{i}": self.load_button_image(f"button_{i}.png") for i in range(1, 16)
        }

        self.create_buttons()

        self.window.resizable(False, False)

        self.entry_list = []

        data = multiplatform_open_read_data_json()

        # Filtrare gli ordini di magazzino in base alla data odierna
        today = datetime.today().date()
        magazzino = [ordine for ordine in data[-1]["magazzino"] if
                     datetime.strptime(ordine.get("consegna", ""), "%d-%m-%Y").date() >= today]

        # Popolamento degli entry con gli ordini magazzino
        for i, ordine in enumerate(magazzino[:7]):
            articolo = ordine.get("nome_articolo", "")
            quantita = ordine.get("quantita", "")
            data_ordine = ordine.get("consegna", "")
            entry_value = f"{articolo}, Quantità: {quantita}, Arrivo: {data_ordine}"
            entry = Entry(
                bd=0,
                bg="#EAEEEC",
                fg="#000716",
                highlightthickness=0
            )
            entry.place(
                x=352.0,
                y=53.0 + i * 50,
                width=300.0,
                height=36.0
            )
            entry.insert(0, entry_value)
            self.entry_list.append(entry)

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
            command=lambda: go_nuovo_ordine_magazzino(self.window),
            relief="flat"
        )
        self.button_9.place(
            x=440.0,
            y=418.0,
            width=188.0,
            height=49.0
        )

        self.button_image_10 = PhotoImage(file=self.relative_to_assets("button_10.png"))
        self.button_10 = Button(
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.save_entry(0), go_modifica_ordine_magazzino(self.window)),
            relief="flat"
        )
        self.button_10.place(
            x=684.0,
            y=58.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_11 = PhotoImage(file=self.relative_to_assets("button_11.png"))
        self.button_11 = Button(
            image=self.button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.save_entry(3), go_modifica_ordine_magazzino(self.window)),
            relief="flat"
        )
        self.button_11.place(
            x=684.0,
            y=208.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_12 = PhotoImage(file=self.relative_to_assets("button_12.png"))
        self.button_12 = Button(
            image=self.button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.save_entry(2), go_modifica_ordine_magazzino(self.window)),
            relief="flat"
        )
        self.button_12.place(
            x=684.0,
            y=158.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_13 = PhotoImage(file=self.relative_to_assets("button_13.png"))
        self.button_13 = Button(
            image=self.button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.save_entry(1), go_modifica_ordine_magazzino(self.window)),
            relief="flat"
        )
        self.button_13.place(
            x=684.0,
            y=108.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_14 = PhotoImage(file=self.relative_to_assets("button_14.png"))
        self.button_14 = Button(
            image=self.button_image_14,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.save_entry(4), go_modifica_ordine_magazzino(self.window)),
            relief="flat"
        )
        self.button_14.place(
            x=684.0,
            y=258.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_15 = PhotoImage(file=self.relative_to_assets("button_15.png"))
        self.button_15 = Button(
            image=self.button_image_15,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.save_entry(5), go_modifica_ordine_magazzino(self.window)),
            relief="flat"
        )
        self.button_15.place(
            x=684.0,
            y=308.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_16 = PhotoImage(file=self.relative_to_assets("button_16.png"))
        self.button_16 = Button(
            image=self.button_image_16,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: (self.save_entry(6), go_modifica_ordine_magazzino(self.window)),
            relief="flat"
        )
        self.button_16.place(
            x=684.0,
            y=358.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

    def save_entry(self, index):
        current_entry = self.entry_list[index].get()

        with open("current_entry_ordine.json", "w") as file:
            json.dump(current_entry, file)

    def relative_to_assets(self, path: str) -> Path:
        return Path(ASSETS_PATH) / Path(path)

    def load_button_image(self, image_path):
        abs_path = os.getcwd()
        assets_path = abs_path + "/assets/frame10"
        return PhotoImage(file=Path(assets_path) / Path(image_path))


def go_nuovo_ordine_magazzino(window):
    from NuovoOrdineMagazzinoApp import NuovoOrdineMagazzino
    window.destroy()
    root = Tk()
    root.title("Nuovo Ordine Magazzino")
    app = NuovoOrdineMagazzino(root)
    centrare_finestra(root)
    root.mainloop()


if __name__ == "__main__":
    root = Tk()
    root.title("Gestione Ordini Magazzino")
    app = GestioneOrdiniMagazzino(root)
    centrare_finestra(root)
    root.mainloop()
