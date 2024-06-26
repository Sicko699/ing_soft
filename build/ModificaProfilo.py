import os, platform, json
import tkinter.messagebox
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from main import centrare_finestra, go_home_button_user, multiplatform_open_write_data_json, multiplatform_open_read_data_json, multiplatform_open_read_current_user
from Clienti import Cliente

abs_path = os.getcwd()

ASSETS_PATH = abs_path + "/assets/frame18"

class ModificaProfilo:
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
            262.0,
            26.0,
            599.0,
            494.0,
            fill="#56AAFF",
            outline=""
        )

        self.profile_manager = Cliente()
        self.load_user_data()

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            430.5,
            96.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FAFFFD",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=314.0,
            y=80.0,
            width=233.0,
            height=30.0
        )

        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            430.5,
            158.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#FAFFFD",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=314.0,
            y=142.0,
            width=233.0,
            height=30.0
        )

        self.canvas.create_text(
            302.0,
            59.0,
            anchor="nw",
            text="Nome",
            fill="#FFFFFF",
            font=("Inter Bold", 16 * -1)
        )

        self.canvas.create_text(
            302.0,
            122.0,
            anchor="nw",
            text="Cognome",
            fill="#FFFFFF",
            font=("Inter Bold", 16 * -1)
        )

        self.entry_image_3 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            430.5,
            221.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#FAFFFD",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_3.place(
            x=314.0,
            y=205.0,
            width=233.0,
            height=30.0
        )

        self.entry_image_4 = PhotoImage(file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            430.5,
            283.0,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#FAFFFD",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_4.place(
            x=314.0,
            y=267.0,
            width=233.0,
            height=30.0
        )

        self.canvas.create_text(
            302.0,
            184.0,
            anchor="nw",
            text="Email",
            fill="#FFFFFF",
            font=("Inter Bold", 16 * -1)
        )

        self.canvas.create_text(
            302.0,
            247.0,
            anchor="nw",
            text="Numero di telefono",
            fill="#FFFFFF",
            font=("Inter Bold", 16 * -1)
        )

        self.entry_image_5 = PhotoImage(file=self.relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            430.5,
            346.0,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            bd=0,
            bg="#FAFFFD",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_5.place(
            x=314.0,
            y=330.0,
            width=233.0,
            height=30.0
        )

        self.entry_image_6 = PhotoImage(file=self.relative_to_assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(
            430.5,
            408.0,
            image=self.entry_image_6
        )
        self.entry_6 = Entry(
            bd=0,
            bg="#FAFFFD",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_6.place(
            x=314.0,
            y=392.0,
            width=233.0,
            height=30.0
        )

        self.entry_1.insert(0, self.nome)
        self.entry_2.insert(0, self.cognome)
        self.entry_3.insert(0, self.email)
        self.entry_4.insert(0, self.telefono)
        self.entry_5.insert(0, self.username)
        self.entry_6.insert(0, self.password)

        self.canvas.create_text(
            302.0,
            309.0,
            anchor="nw",
            text="Username",
            fill="#FFFFFF",
            font=("Inter Bold", 16 * -1)
        )

        self.canvas.create_text(
            302.0,
            372.0,
            anchor="nw",
            text="Password",
            fill="#FFFFFF",
            font=("Inter Bold", 16 * -1)
        )

        self.button_images = {
            f"button_{i}": self.load_button_image(f"button_{i}.png") for i in range(1, 2)
        }

        self.create_buttons()

        self.window.resizable(False, False)

    def load_user_data(self):
        self.nome, self.cognome, self.email, self.telefono, self.username, self.password = self.profile_manager.get_user_info()

    def save_changes(self):
        nome = self.entry_1.get()
        cognome = self.entry_2.get()
        email = self.entry_3.get()
        telefono = self.entry_4.get()
        username = self.entry_5.get()
        password = self.entry_6.get()

        if self.profile_manager.update_user_info(nome, cognome, email, telefono, username, password):
            tkinter.messagebox.showinfo("Avviso", "Modifiche confermate!")
            go_home_button_user(self.window)
        else:
            tkinter.messagebox.showerror("Errore", "Errore durante il salvataggio delle modifiche.")

    def create_buttons(self):
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.save_changes(),
            relief="flat"
        )
        self.button_1.place(
            x=359.0,
            y=443.0,
            width=143.8626708984375,
            height=39.882110595703125
        )

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: go_home_button_user(self.window),
            relief="flat"
        )
        self.button_2.place(
            x=27.0,
            y=21.0,
            width=47.0,
            height=45.0
        )

    def relative_to_assets(self, path: str) -> Path:
        return Path(ASSETS_PATH) / Path(path)

    def load_button_image(self, image_path):
        abs_path = os.getcwd()
        assets_path = abs_path + "/assets/frame18"
        return PhotoImage(file=Path(assets_path) / Path(image_path))

if __name__ == "__main__":
    root = Tk()
    root.title("Modifica Profilo Utente")
    app = ModificaProfilo(root)
    centrare_finestra(root)
    root.mainloop()
