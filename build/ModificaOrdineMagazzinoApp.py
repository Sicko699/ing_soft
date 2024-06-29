from pathlib import Path
import os
import re
import tkinter as tk
from tkinter import ttk, Tk, Canvas, Entry, Button, PhotoImage
import tkinter.messagebox
from datetime import datetime, timedelta
from main import centrare_finestra, exit_button, go_gestione_magazzino, go_home_button, go_front_office_button, \
    go_back_office_button, go_gestione_servizi, multiplatform_open_read_data_json, multiplatform_open_write_data_json

abs_path = os.getcwd()
ASSETS_PATH = abs_path + "/assets/frame13"

from Magazzino import Magazzino  # Importa la classe Magazzino


class ModificaOrdineMagazzino:
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

        self.combo_var = tk.StringVar()
        self.combo_var.set("")
        self.combo = ttk.Combobox(
            self.canvas,
            textvariable=self.combo_var,
            values=["Lenzuola", "Cuscini", "Materasso", "Topper", "Asciugamani", "Carta igienica", "Spazzolini",
                    "Kit di benvenuto", "Detersivo", "Sapone"],
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

        current_entry = Magazzino.carica_ordine_corrente()
        pattern = r'\s*([^,]+),\s*Quantit\u00e0:\s*([^,]+),\s*Arrivo:\s*([^,]+)'
        match = re.search(pattern, current_entry)
        if match:
            nome_articolo_vecchio = match.group(1)
            quantita_vecchia = match.group(2)
            data_ordine_vecchio = match.group(3)

            self.combo_var.set(nome_articolo_vecchio)
            self.entry_2.insert(0, quantita_vecchia)

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
        current_entry = Magazzino.carica_ordine_corrente()

        pattern = r'\s*([^,]+),\s*Quantit\u00e0:\s*([^,]+),\s*Arrivo:\s*([^,]+)'
        match = re.search(pattern, current_entry)
        if match:
            nome_articolo_vecchio = match.group(1)
            quantita_vecchia = match.group(2)
            data_consegna_vecchia = match.group(3)

            new_nome_articolo = self.combo_var.get()
            new_quantita_articolo = self.entry_2.get()

            if Magazzino.aggiorna_ordine(nome_articolo_vecchio, quantita_vecchia, data_consegna_vecchia,
                                         new_nome_articolo, new_quantita_articolo):
                tkinter.messagebox.showinfo("Avviso", "Modifiche confermate!")
                go_gestione_magazzino(self.window)
            else:
                tkinter.messagebox.showerror("Errore",
                                             "Si è verificato un errore durante il salvataggio delle modifiche.")

    def relative_to_assets(self, path: str) -> Path:
        return Path(ASSETS_PATH) / Path(path)

    def load_button_image(self, image_path):
        return PhotoImage(file=self.relative_to_assets(image_path))


if __name__ == "__main__":
    root = Tk()
    root.title("Modifica Ordine Magazzino")
    app = ModificaOrdineMagazzino(root)
    centrare_finestra(root)
    root.mainloop()
