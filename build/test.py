import tkinter as tk
from tkcalendar import Calendar

def print_selected_dates():
    arrival_date = cal_arrival.get_date()
    departure_date = cal_departure.get_date()
    print("Data di arrivo:", arrival_date)
    print("Data di partenza:", departure_date)

root = tk.Tk()
root.geometry("600x400")

# Widget di calendario per la data di arrivo
cal_arrival_label = tk.Label(root, text="Seleziona la data di arrivo:")
cal_arrival_label.pack(pady=10)
cal_arrival = Calendar(root, selectmode="day")
cal_arrival.pack(pady=5)

# Widget di calendario per la data di partenza
cal_departure_label = tk.Label(root, text="Seleziona la data di partenza:")
cal_departure_label.pack(pady=10)
cal_departure = Calendar(root, selectmode="day")
cal_departure.pack(pady=5)

# Pulsante per stampare le date selezionate
button = tk.Button(root, text="Conferma date", command=print_selected_dates)
button.pack(pady=10)

root.mainloop()
