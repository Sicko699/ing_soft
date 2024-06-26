from pathlib import Path
import os, platform
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from main import centrare_finestra, go_visualizza_prenotazioni_servizi, go_front_office_button, go_back_office_button, exit_button, go_home_button, go_gestione_magazzino, go_gestione_spa

abs = os.getcwd()

ASSETS_PATH = abs + "/assets/frame17"
    
class GestioneServizi:
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
        
        self.image_image_1 = PhotoImage(file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            403.0,
            381.0,
            image=self.image_image_1
        )

        
        self.image_image_2 = PhotoImage(file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            401.0,
            174.0,
            image=self.image_image_2
        )
        
        self.image_image_3 = PhotoImage(file=self.relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            673.0,
            167.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(file=self.relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            673.0,
            380.0,
            image=self.image_image_4
        )

        self.button_images = {
            f"button_{i}": self.load_button_image(f"button_{i}.png") for i in range(1, 12)
        }

        self.create_buttons()

        self.window.resizable(False, False)


    def create_buttons(self):
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: button_1_click(self.window),
            relief="flat"
        )
        self.button_1.place(
            x=285.0,
            y=296.0,
            width=232.0,
            height=174.0
        )


        self.button_image_2 = PhotoImage(file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: exit_button(self.window),
            relief="flat"
        )
        self.button_2.place(
            x=46.0,
            y=452.0,
            width=47.0,
            height=45.0
        )
        
        self.button_image_3 = PhotoImage(file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: go_home_button(self.window),
            relief="flat"
        )
        self.button_3.place(
            x=116.0,
            y=452.0,
            width=47.0,
            height=45.0
        )
        
        self.button_image_4 = PhotoImage(file=self.relative_to_assets("button_4.png"))
        self.button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: go_front_office_button(self.window),
            relief="flat"
        )
        self.button_4.place(
            x=24.0,
            y=98.0,
            width=162.0,
            height=45.0
        )

        self.button_image_5 = PhotoImage(file=self.relative_to_assets("button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: go_back_office_button(self.window),
            relief="flat"
        )
        self.button_5.place(
            x=24.0,
            y=158.0,
            width=162.0,
            height=45.0
        )

        self.button_image_7 = PhotoImage(file=self.relative_to_assets("button_7.png"))
        self.button_7 = Button(
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: go_gestione_magazzino(self.window),
            relief="flat"
        )
        self.button_7.place(
            x=24.0,
            y=218.0,
            width=162.0,
            height=45.0
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
            command=lambda: go_gestione_spa(self.window),
            relief="flat"
        )
        self.button_9.place(
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
            command=lambda: button_10_click(self.window),
            relief="flat"
        )
        self.button_10.place(
            x=285.0,
            y=89.0,
            width=232.0,
            height=174.0
        )

        self.button_image_11 = PhotoImage(file=self.relative_to_assets("button_11.png"))
        self.button_11 = Button(
            image=self.button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: button_11_click(self.window),
            relief="flat"
        )
        self.button_11.place(
            x=558.0,
            y=89.0,
            width=232.0,
            height=174.0
        )
        
        self.button_image_12 = PhotoImage(file=self.relative_to_assets("button_12.png"))
        self.button_12 = Button(
            image=self.button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: button_12_click(self.window),
            relief="flat"
        )
        self.button_12.place(
            x=558.0,
            y=296.0,
            width=232.0,
            height=174.0
        )

        self.button_image_13 = PhotoImage(file=self.relative_to_assets("button_5 copy.png"))
        self.button_13 = Button(
            image=self.button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: go_visualizza_prenotazioni_servizi(self.window),
            relief="flat"
        )
        self.button_13.place(
            x=441.0,
            y=13.0,
            width=190.0,
            height=67.0
        )

    def relative_to_assets(self,path: str) -> Path:
        return Path(ASSETS_PATH) / Path(path)

    def load_button_image(self, image_path):
        abs_path = os.getcwd()
        
        assets_path = abs_path + "/assets/frame17"

        return PhotoImage(file=Path(assets_path) / Path(image_path))

def button_10_click(window):
    from PrenotazioneServiziApp import PrenotazioneServizi
    window.destroy()
    root = Tk() 
    root.title("Prenotazione Servizi")
    prenotazione_servizi = PrenotazioneServizi(root)
    prenotazione_servizi.fill_entry("Visita guidata")
    centrare_finestra(root) 
    root.mainloop()

def button_1_click(window):
    from PrenotazioneServiziApp import PrenotazioneServizi
    window.destroy()
    root = Tk()
    root.title("Prenotazione Servizi")
    prenotazione_servizi = PrenotazioneServizi(root)
    prenotazione_servizi.fill_entry("Giro in barca")
    centrare_finestra(root)
    root.mainloop()
    
def button_11_click(window):
    from PrenotazioneServiziApp import PrenotazioneServizi
    window.destroy()
    root = Tk()
    root.title("Prenotazione Servizi") 
    prenotazione_servizi = PrenotazioneServizi(root)
    prenotazione_servizi.fill_entry("Noleggio biciclette")
    centrare_finestra(root) 
    root.mainloop()
    
def button_12_click(window):
    from PrenotazioneServiziApp import PrenotazioneServizi
    window.destroy()
    root = Tk()
    root.title("Prenotazione Servizi")
    prenotazione_servizi = PrenotazioneServizi(root)
    prenotazione_servizi.fill_entry("Piscina privata")
    centrare_finestra(root)
    root.mainloop()


if __name__ == "__main__":
    root = Tk()
    root.title("Gestione Servizi")
    app = GestioneServizi(root)
    centrare_finestra(root)
    root.mainloop()