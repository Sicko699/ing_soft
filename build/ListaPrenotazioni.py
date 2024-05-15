from pathlib import Path
import os, platform, json, re
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from main import go_home_button_user, multiplatform_open_read_current_user, multiplatform_open_read_data_json

abs_path = os.getcwd()

ASSETS_PATH = abs_path + "/assets/frame21"

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

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            430.0,
            137.0,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=249.0,
            y=119.0,
            width=363.0,
            height=36.0
        )

        self.entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            430.0,
            187.0,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_2.place(
            x=249.0,
            y=169.0,
            width=363.0,
            height=36.0
        )

        self.entry_image_3 = PhotoImage(file=self.relative_to_assets("entry_3.png"))
        self.entry_bg_3 = self.canvas.create_image(
            430.0,
            237.0,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_3.place(
            x=249.0,
            y=219.0,
            width=363.0,
            height=36.0
        )

        self.entry_image_4 = PhotoImage(file=self.relative_to_assets("entry_4.png"))
        self.entry_bg_4 = self.canvas.create_image(
            430.0,
            287.0,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_4.place(
            x=249.0,
            y=269.0,
            width=363.0,
            height=36.0
        )

        self.entry_image_5 = PhotoImage(file=self.relative_to_assets("entry_5.png"))
        self.entry_bg_5 = self.canvas.create_image(
            430.0,
            337.0,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_5.place(
            x=249.0,
            y=319.0,
            width=363.0,
            height=36.0
        )

        self.entry_image_6 = PhotoImage(file=self.relative_to_assets("entry_6.png"))
        self.entry_bg_6 = self.canvas.create_image(
            430.0,
            387.0,
            image=self.entry_image_6
        )
        self.entry_6 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_6.place(
            x=249.0,
            y=369.0,
            width=363.0,
            height=36.0
        )    

        self.button_images = {
            f"button_{i}": self.load_button_image(f"button_{i}.png") for i in range(1, 13)
        }

        self.window.resizable(False, False)

        self.show_prenotazioni()

        self.create_buttons()

    def show_prenotazioni(self):
        self.entry_list = []
        current_user = multiplatform_open_read_current_user()
        data = multiplatform_open_read_data_json()
        if data and current_user:
            for user in data[0]['users']:
                if user['username'] == current_user['username'] and user['password'] == current_user['password']:
                    prenotazioni = user.get('prenotazioni', [])
                    for i, prenotazione in enumerate(prenotazioni):
                        entry_text = f"Tipo: {prenotazione['tipo_camera']}, Arrivo: {prenotazione['arrivo']}"
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
                        entry.insert(0, entry_text)
                        self.entry_list.append(entry)

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
            command=lambda: (self.save_entry(0), self.elimina_prenotazione()),
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
            command=lambda: self.save_entry(1),
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
            command=lambda: self.save_entry(2),
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
            command=lambda: self.save_entry(3),
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
            command=lambda: self.save_entry(4),
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
            command=lambda: self.save_entry(5),
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

    def save_entry(self, index):
        current_entry_user = self.entry_list[index].get()

        with open("current_entry_prenotazione_user.json", "w") as file:
            json.dump(current_entry_user, file)

    def elimina_prenotazione(self):
        data = multiplatform_open_read_data_json()
        current_user = multiplatform_open_read_current_user()

        with open("current_entry_prenotazione_user.json", "r") as user_json:
            current_entry_user = json.load(user_json)
        
        pattern = r'Tipo:\s*([^,]+),\s*Arrivo:\s*([^,]+)'
        match = re.search(pattern, current_entry_user)
        tipo = match.group(1)
        arrivo = match.group(2)

        print(tipo, arrivo)

        if data and current_user:
            for user in data[0]['users']:
                if user['username'] == current_user['username'] and user['password'] == current_user['password']:
                    prenotazioni = user.get('prenotazioni', [])
                    for prenotazione in enumerate(prenotazioni[:6]):
                        if prenotazione['tipo_camera'] == tipo and prenotazione['arrivo'] == arrivo:
                            print("Eliminato con successo")
                            break

    def relative_to_assets(self,path: str) -> Path:
        return Path(ASSETS_PATH) / Path(path)
    
    def load_button_image(self, image_path):
        abs_path = os.getcwd()

        assets_path = abs_path + "/assets/frame21"

        return PhotoImage(file=Path(assets_path) / Path(image_path))

if __name__ == "__main__":
    root = Tk()
    app = ListaPrenotazioni(root)
    root.mainloop()