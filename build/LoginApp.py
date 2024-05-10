import sys
sys.dont_write_bytecode = True

from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from pathlib import Path
import json, tempfile
import os
import platform
import faulthandler; faulthandler.enable()
import verify_login
from main import go_home_button, go_cerca_camere, multiplatform_open_write_current_user

abs_path = os.getcwd()

ASSETS_PATH = abs_path + "/assets/frame3"

class LoginApp:
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
            106.0,
            599.0,
            413.0,
            fill="#56AAFF",
            outline=""
        )

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            431.5,
            191.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FAFFFD",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=315.0,
            y=172.0,
            width=233.0,
            height=36.0
        )

        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            431.5,
            269.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#FAFFFD",
            fg="#000716",
            highlightthickness=0,
            show="*"
        )
        self.entry_2.place(
            x=315.0,
            y=250.0,
            width=233.0,
            height=37.0
        )

        self.canvas.create_text(
            303.0,
            147.0,
            anchor="nw",
            text="Username",
            fill="#FFFFFF",
            font=("Inter Bold", 18)
        )

        self.canvas.create_text(
            303.0,
            226.0,
            anchor="nw",
            text="Password",
            fill="#FFFFFF",
            font=("Inter Bold", 18)
        )

        self.button_images = {
            f"button_{i}": self.load_button_image(f"button_{i}.png") for i in range(1, 2)
        }

        self.create_buttons()

        self.window.resizable(False, False)

    def create_buttons(self):
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.login_clicked,
            relief="flat"
        )
        self.button_1.place(
            x=358.91162109375,
            y=329.33056640625,
            width=143.8626708984375,
            height=38.523895263671875
        )

        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: go_registrazione(self.window),
            relief="flat"
        )
        self.button_2.place(
            x=303.0,
            y=288.0,
            width=257.0,
            height=39.0
        )

    def relative_to_assets(self, path: str) -> Path:
        return Path(ASSETS_PATH) / Path(path)

    def login_clicked(self):
        username = self.entry_1.get()
        password = self.entry_2.get()

        if verify_login.verify_login(username, password) == "admin":
            print("Accesso consentito come admin")
            go_home_button(self.window)
            
        elif verify_login.verify_login(username, password) == "utente":
            print("Accesso consentito come utente")
            current_user = {"username": username, "password": password}

            # Scrivi i dettagli dell'utente nel file current_user.json
            current_user = multiplatform_open_write_current_user(current_user)

            go_cerca_camere(self.window)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def load_button_image(self, image_path):
        abs_path = os.getcwd()
        
        assets_path = abs_path + "/assets/frame3"

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
    

def go_registrazione(window):
    from RegistrazioneApp import RegistrazioneApp
    window.destroy()
    root = Tk()
    app = RegistrazioneApp(root)
    root.mainloop()

if __name__ == "__main__":
    root = Tk()
    root.title("Login")
    app = LoginApp(root)
    centrare_finestra(root)
    root.mainloop()