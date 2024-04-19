from pathlib import Path
import os, platform, json
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from main import go_home_button

abs_path = os.getcwd()
if platform.system() == "Darwin":
    ASSETS_PATH = abs_path + "/assets/frame4"
else:
    ASSETS_PATH = abs_path + "/build/assets/frame4"

class RegistrazioneApp:
    def __init__(self, window):
        self.window = window
        self.window.geometry("862x519")
        self.window.configure(bg = "#FAFFFD")
        
        self.canvas = Canvas(
            window,
            bg = "#FAFFFD",
            height = 519,
            width = 862,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        
        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            262.0,
            26.0,
            599.0,
            494.0,
            fill="#56AAFF",
            outline="")

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
            highlightthickness=0,
            show="*"
        )
        self.entry_6.place(
            x=314.0,
            y=392.0,
            width=233.0,
            height=30.0
        )
        
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
            f"button_{i}": self.load_button_image(f"button_{i}.png") for i in range(1, 1)
        }

        self.create_buttons()

        self.window.resizable(False, False)
    
    def create_buttons(self):
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: [self.registrazione(), go_cerca_camere(self.window)],
            relief="flat"
        )
        self.button_1.place(
            x=359.0,
            y=443.0,
            width=143.8626708984375,
            height=39.882110595703125
        )

    def relative_to_assets(self, path: str) -> Path:
        return Path(ASSETS_PATH) / Path(path)

    def load_button_image(self, image_path):
        abs_path = os.getcwd()
        if platform.system() == "Darwin":
            assets_path = abs_path + "/assets/frame4"
        else:
            assets_path = abs_path + "/build/assets/frame4"

        return PhotoImage(file=Path(assets_path) / Path(image_path))
    
    def registrazione(self):
        # Raccogli i dati inseriti dall'utente
        nome = self.entry_1.get()
        cognome = self.entry_2.get()
        email = self.entry_3.get()
        telefono = self.entry_4.get()
        username = self.entry_5.get()
        password = self.entry_6.get()
        role = "utente"
        prenotazione = {}

        # Crea un dizionario con i dati dell'utente
        utente = {
            "nome": nome,
            "cognome": cognome,
            "email": email,
            "telefono": telefono,
            "username": username,
            "password": password,
            "role": role,
            "prenotazioni": prenotazione
        }

        try:
            if platform.system() == "Darwin":
                with open("data.json", "r") as file:
                    data = json.load(file)
            else:
                with open(r"build/data.json", "r") as file:
                    data = json.load(file)
        except FileNotFoundError:
            data = [{"users": []}]  # Inizializza con una lista contenente un dizionario vuoto se il file non esiste

        # Accedi al dizionario all'interno della lista e quindi alla lista degli utenti
        users_data = data[0] if data else {"users": []}
        users_list = users_data.get("users", [])  # Get the users list

        # Aggiungi il nuovo utente alla lista
        users_list.append(utente)

        # Aggiorna il dizionario con i dati dell'utente
        users_data["users"] = users_list
        
        current_user = {"username": username, "password": password}

            # Scrivi i dettagli dell'utente nel file current_user.json
        if platform.system() == "Darwin":
            with open("current_user.json", "w") as file:
                json.dump(current_user, file)
        else:
            with open(r"build/current_user.json", "w") as file:
                json.dump(current_user, file)

        if platform.system() == "Darwin":
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
        else:
            with open(r"build/data.json", "w") as file:
                json.dump(data, file, indent=4)


        print("Registrazione completata con successo!")


    
def go_cerca_camere(window):
    from CercaCamereApp import CercaCamere
    window.destroy()
    root = Tk()
    app = CercaCamere(root)
    root.mainloop()
        
if __name__ == '__main__':    
    root = Tk()
    app = RegistrazioneApp(root)
    root.mainloop()