from pathlib import Path
import os, platform, json
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from main import exit_button, go_gestione_magazzino, go_back_office_button, go_front_office_button, go_gestione_servizi, go_gestione_spa, go_home_button

abs_path = os.getcwd()
if platform.system() == "Darwin":
    ASSETS_PATH = abs_path + "/assets/frame16"
else:
    ASSETS_PATH = abs_path + "/build/assets/frame16"

class PrenotazioneServizi:
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

        self.canvas.create_rectangle(
            344.0,
            110.0,
            734.0,
            410.0,
            fill="#FAFFFD",
            outline=""
        )

        self.entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            539.0,
            185.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#EAEEEC",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=401.0,
            y=166.0,
            width=276.0,
            height=37.0
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
            text="Nome servizio",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.canvas.create_text(
            389.0,
            221.0,
            anchor="nw",
            text="Camera",
            fill="#000000",
            font=("Quicksand Medium", 16 * -1)
        )

        self.create_buttons()

        self.window.resizable(False, False)
        
    def fill_entry(self, text):
        self.entry_1.delete(0, 'end')
        self.entry_1.insert(0, text)
        
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

        self.button_image_10 = PhotoImage(file=self.relative_to_assets("button_10.png"))
        self.button_10 = Button(
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.invia_servizio(),
            relief="flat"
        )
        self.button_10.place(
            x=445.0,
            y=315.0,
            width=187.0,
            height=49.0
        )    
        
    def invia_servizio(self):
        nome_servizio = self.entry_1.get()
        numero_camera = self.entry_2.get()
        
        servizio = {
            "nome_servizio" : nome_servizio,
            "numero_camera" : numero_camera
        }
        
        try:
            if platform.system() == "Darwin":
                with open("data.json", "r") as file:
                    data = json.load(file)
            else:
                with open(r"build/data.json", "r") as file:
                    data = json.load(file)    
            # Assuming you want to append 'servizio' to the 'servizi' list in the last dictionary of 'data'
            servizi = data[-1]["servizi"]
            servizi.append(servizio)
            
            if platform.system() == "Darwin":
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)  # Writing back the entire 'data' dictionary
            else:
                with open(r"build/data.json", "w") as file:
                    json.dump(data, file, indent=4)        
                print("Servizio aggiunto con successo")
        except Exception as e:
            print("Si è verificato un errore:", e)

        

    def relative_to_assets(self,path: str) -> Path:
        return Path(ASSETS_PATH) / Path(path)
    
    def load_button_image(self, image_path):
        abs_path = os.getcwd()
        if platform.system() == "Darwin":
            assets_path = abs_path + "/assets/frame16"
        else:
            assets_path = abs_path + "/build/assets/frame16"

        return PhotoImage(file=Path(assets_path) / Path(image_path))
    
if __name__ == "__main__":        
    root = Tk()
    app = PrenotazioneServizi(root)
    root.mainloop()