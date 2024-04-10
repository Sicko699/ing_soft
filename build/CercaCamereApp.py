import tkinter as tk
from tkinter import Tk, Button, ttk, PhotoImage
from tkcalendar import Calendar
from pathlib import Path
import os
import platform

abs_path = os.getcwd()
if platform.system() == "Darwin":
    ASSETS_PATH = abs_path + "/assets/frame5"
else:
    ASSETS_PATH = abs_path + "/build/assets/frame5"

class CercaCamere:
    def __init__(self, window):
        self.window = window
        self.window.geometry("862x519")
        self.window.configure(bg="#FAFFFD")

        self.canvas = tk.Canvas(
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
            91.0,
            599.0,
            414.0,
            fill="#56AAFF",
            outline=""
        )

        self.arrival_button = Button(
            self.canvas,
            text="Seleziona data di arrivo",
            command=self.open_arrival_calendar,
            bg="#FAFFFD",
            fg="#000716",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            font=("Inter Bold", 12)
        )
        self.arrival_button.place(x=302.0, y=145.0, width=257, height=32)

        self.departure_button = Button(
            self.canvas,
            text="Seleziona data di partenza",
            command=self.open_departure_calendar,
            bg="#FAFFFD",
            fg="#000716",
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            font=("Inter Bold", 12)
        )
        self.departure_button.place(x=302.0, y=207.0, width=257, height=32)

        self.canvas.create_text(
            302.0,
            124.0,
            anchor="nw",
            text="Data di arrivo",
            fill="#FFFFFF",
            font=("Quicksand", 16 * -1)
        )

        self.canvas.create_text(
            302.0,
            187.0,
            anchor="nw",
            text="Data di partenza",
            fill="#FFFFFF",
            font=("Quicksand", 16 * -1)
        )
        
        self.canvas.create_text(
            302.0,
            249.0,
            anchor="nw",
            text="Tipologia Camera",
            fill="#FFFFFF",
            font=("Quicksand", 16 * -1)
        )

        self.combo_var = tk.StringVar()
        self.combo_var.set("Camera Singola")
        self.combo = ttk.Combobox(
            self.canvas,
            textvariable=self.combo_var,
            values=["Camera Singola", "Camera Doppia", "Camera Tripla", "Camera Quadrupla"],
            state="readonly",
            width=20,
            height=5,
<<<<<<< HEAD
            font=("Quicksand", 16)
=======
            font=("Quicksand", 16 * -1)
>>>>>>> 191a56996f8a7bbd47698fc4e737c0d48080166e
        )
        self.combo.place(x=302.0, y=270, width=257, height=32)

        self.button_images = {
            f"button_{i}": self.load_button_image(f"button_{i}.png") for i in range(1, 1)
        }
        
        self.button_image_1 = PhotoImage(file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )

        self.button_1.place(
            x=359.0,
            y=339.0,
            width=143.8626708984375,
            height=39.882110595703125
        )

        self.window.resizable(False, False)
        
    def open_arrival_calendar(self):
        self.arrival_calendar = tk.Toplevel(self.window)
        self.arrival_calendar.geometry("330x270")
        self.arrival_calendar.title("Seleziona data di arrivo")
        
        cal_arrival = Calendar(self.arrival_calendar, selectmode="day", date_pattern="dd-mm-yyyy", font="Quicksand 14", cursor="hand1")
        cal_arrival.grid(row=0, column=0, padx=10, pady=10)
        
        confirm_button = Button(self.arrival_calendar, text="Conferma", command=self.confirm_arrival_date)
        confirm_button.grid(row=1, column=0, pady=10)


    def confirm_arrival_date(self):
        selected_date = self.arrival_calendar.winfo_children()[0].get_date()
        self.arrival_button.config(text=selected_date)
        self.arrival_calendar.destroy()
        
    def open_departure_calendar(self):
        self.departure_calendar = tk.Toplevel(self.window)
        self.departure_calendar.geometry("330x270")
        self.departure_calendar.title("Seleziona data di partenza")
        
        cal_departure = Calendar(self.departure_calendar, selectmode="day", date_pattern="dd-mm-yyyy", 
                                 font="Quicksand 14", cursor="hand1")
        cal_departure.grid(row=0, column=0, padx=10, pady=10)
        
        confirm_button = Button(self.departure_calendar, text="Conferma", command=self.confirm_departure_date)
        confirm_button.grid(row=1, column=0, pady=10)
        
    def confirm_departure_date(self):
        selected_date = self.departure_calendar.winfo_children()[0].get_date()
        self.departure_button.config(text=selected_date)
        self.departure_calendar.destroy()

    def relative_to_assets(self, path: str) -> Path:
        return Path(ASSETS_PATH) / Path(path)

    def load_button_image(self, image_path):
        abs_path = os.getcwd()
        if platform.system() == "Darwin":
            assets_path = abs_path + "/assets/frame5"
        else:
            assets_path = abs_path + "/build/assets/frame5"

        return tk.PhotoImage(file=Path(assets_path) / Path(image_path))
    
if __name__ == "__main__":
    root = Tk()
    app = CercaCamere(root)
    root.mainloop()
