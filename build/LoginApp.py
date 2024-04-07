from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from pathlib import Path
import json
import os, platform
from MainApp import MainApp

class LoginApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("862x519")
        self.master.configure(bg="#FAFFFD")

        self.canvas = Canvas(
            self.master,
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
            outline="")

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
            command=lambda: print("button_2 clicked"),
            relief="flat"
        )
        self.button_2.place(
            x=303.0,
            y=288.0,
            width=257.0,
            height=39.0
        )


        self.master.resizable(False, False)

    def relative_to_assets(self, path: str) -> Path:
        return ASSETS_PATH / Path(path)

    def verify_login(self, username, password):
        with open("data.json", "r") as file:
            data = json.load(file)

        users = data["users"]

        for user in users:
            if user["username"] == username and user["password"] == password and user["role"] == "admin":
                return "admin"
            elif user["username"] == username and user["password"] == password and user["role"] == "utente":
                return "utente"

        return False

    ''' def register_clicked(self):
        self.master.destr'''

    def login_clicked(self):
        username = self.entry_1.get()
        password = self.entry_2.get()

        if self.verify_login(username, password) == "admin":
            print("Accesso consentito come admin")
            self.master.destroy()  # Chiude la finestra della LoginApp
            root = Tk()  # Crea una nuova finestra Tk per la MainApp
            app = MainApp(root)  # Avvia la MainApp nella nuova finestra Tk
            root.mainloop()  # Avvia il loop principale della nuova finestra Tk
        elif self.verify_login(username, password) == "utente":
            print("Accesso consentito come utente")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")


if __name__ == "__main__":
    abs = os.getcwd()
    if(platform.system() == "Darwin"):
        ASSETS_PATH = abs + "/assets/frame3"
    else:
        ASSETS_PATH = abs + "/build/assets/frame3"

    root = Tk()
    app = LoginApp(root)
    root.mainloop()

