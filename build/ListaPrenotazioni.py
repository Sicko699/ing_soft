from pathlib import Path
import os, platform, json
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from main import go_home_button_user, multiplatform_open_read_current_user, multiplatform_open_read_data_json

abs_path = os.getcwd()
if platform.system() == "Darwin":
    ASSETS_PATH = abs_path + "/assets/frame21"
else:
    ASSETS_PATH = abs_path + "/build/assets/frame21"

class ListaPrenotazioni:
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
            212.0,
            88.0,
            649.0,
            432.0,
            fill="#FAFFFD",
            outline="")

        self.entries = []
        for i in range(6):
            entry = Entry(
                bd=0,
                bg="#EAEEEC",
                fg="#000716",
                highlightthickness=0
            )
            entry.place(
                x=249.0,
                y=119.0 + i * 50,
                width=363.0,
                height=36.0
            )
            self.entries.append(entry)    

        self.button_images = {
            f"button_{i}": self.load_button_image(f"button_{i}.png") for i in range(1, 13)
        }

        self.create_buttons()

        self.window.resizable(False, False)

        self.show_current_user_prenotazioni()

    def show_current_user_prenotazioni(self):
        current_user = multiplatform_open_read_current_user()
        data = multiplatform_open_read_data_json()
        if data and current_user:
            for user in data[0]['users']:
                if user['username'] == current_user['username'] and user['password'] == current_user['password']:
                    prenotazioni = user.get('prenotazioni', [])
                    for i, prenotazione in enumerate(prenotazioni):
                        entry_text = f"Tipo: {prenotazione['tipo_camera']}, Arrivo: {prenotazione['arrivo']}"
                        self.entries[i].insert(0, entry_text)
                    break

    def create_buttons(self):
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(
            x=581.0,
            y=124.0,
            width=28.398725509643555,
            height=28.398725509643555
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
            x=581.0,
            y=274.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_3 clicked"),
            relief="flat"
        )
        self.button_3.place(
            x=581.0,
            y=224.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.button_4.place(
            x=581.0,
            y=174.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_5 = PhotoImage(file=self.relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_5 clicked"),
            relief="flat"
        )
        self.button_5.place(
            x=581.0,
            y=324.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_6 = PhotoImage(file=self.relative_to_assets("button_6.png"))
        self.button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_6 clicked"),
            relief="flat"
        )
        self.button_6.place(
            x=581.0,
            y=374.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_7 = PhotoImage(file=self.relative_to_assets("button_7.png"))
        self.button_7 = Button(
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_7 clicked"),
            relief="flat"
        )
        self.button_7.place(
            x=545.0,
            y=124.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_8 = PhotoImage(file=self.relative_to_assets("button_8.png"))
        self.button_8 = Button(
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_8 clicked"),
            relief="flat"
        )
        self.button_8.place(
            x=545.0,
            y=174.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_9 = PhotoImage(file=self.relative_to_assets("button_9.png"))
        self.button_9 = Button(
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_9 clicked"),
            relief="flat"
        )
        self.button_9.place(
            x=545.0,
            y=224.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_10 = PhotoImage(file=self.relative_to_assets("button_10.png"))
        self.button_10 = Button(
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_10 clicked"),
            relief="flat"
        )
        self.button_10.place(
            x=545.0,
            y=274.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_11 = PhotoImage(file=self.relative_to_assets("button_11.png"))
        self.button_11 = Button(
            image=self.button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_11 clicked"),
            relief="flat"
        )
        self.button_11.place(
            x=545.0,
            y=324.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_12 = PhotoImage(file=self.relative_to_assets("button_12.png"))
        self.button_12 = Button(
            image=self.button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_12 clicked"),
            relief="flat"
        )
        self.button_12.place(
            x=545.0,
            y=374.0,
            width=28.398725509643555,
            height=28.398725509643555
        )

        self.button_image_13 = PhotoImage(file=self.relative_to_assets("button_13.png"))
        self.button_13 = Button(
            image=self.button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: go_home_button_user(self.window),
            relief="flat"
        )
        self.button_13.place(
            x=27.0,
            y=21.0,
            width=47.0,
            height=45.0
        )

    def relative_to_assets(self,path: str) -> Path:
        return Path(ASSETS_PATH) / Path(path)
    
    def load_button_image(self, image_path):
        abs_path = os.getcwd()
        if platform.system() == "Darwin":
            assets_path = abs_path + "/assets/frame21"
        else:
            assets_path = abs_path + "/build/assets/frame21"

        return PhotoImage(file=Path(assets_path) / Path(image_path))

if __name__ == "__main__":
    root = Tk()
    app = ListaPrenotazioni(root)
    root.mainloop()
