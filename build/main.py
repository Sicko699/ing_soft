from tkinter import Tk
import platform, json

def centrare_finestra(window):
    window.update_idletasks()
    larghezza_finestra = window.winfo_width()
    altezza_finestra = window.winfo_height()
    schermo_larghezza = window.winfo_screenwidth()
    schermo_altezza = window.winfo_screenheight()
    x = (schermo_larghezza - larghezza_finestra) // 2
    y = (schermo_altezza - altezza_finestra) // 2
    window.geometry('{}x{}+{}+{}'.format(larghezza_finestra, altezza_finestra, x, y))


def exit_button(window):
    from LoginApp import LoginApp
    window.destroy()
    root = Tk()
    app = LoginApp(root)
    centrare_finestra(root)
    root.mainloop()

def go_home_button(window):
    from MainApp import MainApp
    window.destroy()
    root = Tk()
    app = MainApp(root)
    centrare_finestra(root)
    root.mainloop()

def go_front_office_button(window):
    from FrontOfficeApp import FrontOfficeApp
    window.destroy()
    root = Tk()
    app = FrontOfficeApp(root)
    centrare_finestra(root)
    root.mainloop()

def go_back_office_button(window):
    from BackOfficeApp import BackOfficeApp
    window.destroy()
    root = Tk()
    app = BackOfficeApp(root)
    centrare_finestra(root)
    root.mainloop()
    
def go_gestione_magazzino(window):
    from GestioneOrdiniMagazzinoApp import GestioneOrdiniMagazzino
    window.destroy()
    root = Tk()
    app = GestioneOrdiniMagazzino(root)
    centrare_finestra(root)
    root.mainloop()
    
def go_gestione_servizi(window):
    from GestioneServiziApp import GestioneServizi
    window.destroy()
    root = Tk()
    app = GestioneServizi(root)
    centrare_finestra(root)
    root.mainloop()
    
def go_gestione_spa(window):
    from GestionePrenotazioniSpaApp import GestionePrenotazioniSpa
    window.destroy()
    root = Tk()
    app = GestionePrenotazioniSpa(root)
    centrare_finestra(root)
    root.mainloop()
    
def go_home_button_user(window):
    from CercaCamereApp import CercaCamere
    window.destroy()
    root = Tk()
    app = CercaCamere(root)
    centrare_finestra(root)
    root.mainloop()

def go_mostra_prenotazione(window):
    from MostraPrenotazioneApp import MostraPrenotazioneApp
    window.destroy()
    root = Tk()
    app = MostraPrenotazioneApp(root)
    centrare_finestra(root)
    root.mainloop()
    
def go_cerca_camere(window):
    from CercaCamereApp import CercaCamere
    window.destroy()
    root = Tk()
    app = CercaCamere(root)
    centrare_finestra(root)
    root.mainloop()
    
def go_lista_prenotazioni(window):
    from ListaPrenotazioni import ListaPrenotazioni
    window.destroy()
    root = Tk()
    app = ListaPrenotazioni(root)
    centrare_finestra(root)
    root.mainloop()

def multiplatform_open_read_data_json():
    if platform.system() == "Darwin":
        with open("data.json", "r") as json_file:
            data_json = json.load(json_file)
    else:
        with open(r"build/data.json", "r") as json_file:
            data_json = json.load(json_file)
    return data_json

def multiplatform_open_read_current_user():
    if platform.system() == "Darwin":
        with open("current_user.json", "r") as user_file:
            current_user = json.load(user_file)
    else:
        with open(r"build/current_user.json", "r") as user_file:
            current_user = json.load(user_file)
    return current_user

def multiplatform_open_read_current_prenotazione():
    if platform.system() == "Darwin":
        with open("current_prenotazione.json", "r") as file:
            current_prenotazione = json.load(file)
    else:
        with open(r"build/current_prenotazione.json", "r") as file:
            current_prenotazione = json.load(file)
    return current_prenotazione

def multiplatform_open_write_data_json(data_json):
    if platform.system() == "Darwin":
        with open("data.json", "w") as file:
            write_data_json = json.dump(data_json, file, indent=4)
    else:
        with open(r"build/data.json", "w") as file:
            write_data_json = json.dump(data_json, file, indent=4)
    return write_data_json

def multiplatform_open_write_current_user(current_user):
    if platform.system() == "Darwin":
        with open("current_user.json", "w") as file:
            write_current_user = json.dump(current_user, file)
    else:
        with open(r"build/current_user.json", "w") as file:
            write_current_user = json.dump(current_user, file)
    return write_current_user

def multiplatform_open_write_current_prenotazione(current_prenotazione):
    if platform.system() == "Darwin":
        with open("current_prenotazione.json", "w") as file:
            write_current_prenotazione = json.dump(current_prenotazione, file)
    else:
        with open(r"build/current_prenotazione.json", "w") as file:
            write_current_prenotazione = json.dump(current_prenotazione, file)
    return write_current_prenotazione

def multiplatform_open_read_entry_json():
    if platform.system() == "Darwin":
        with open("current_entry.json", "r") as user_json:
            current_entry = json.load(user_json)
    else:
        with open(r"build/current_entry.json", "r") as user_json:
            current_entry = json.load(user_json)
    return current_entry

def go_modifica_profilo(window):
    from ModificaProfilo import ModificaProfilo
    window.destroy()
    root = Tk()
    app = ModificaProfilo(root)
    centrare_finestra(root)
    root.mainloop()    
    
def go_nuova_prenotazione_spa(window):
    from NuovaPrenotazioneSpaApp import NuovaPrenotazioneSpa
    window.destroy()
    root = Tk()
    app = NuovaPrenotazioneSpa(root)
    centrare_finestra(root)
    root.mainloop()
    
def go_modifica_prenotazione_spa(window):
    from ModificaPrenotazioneSpa import ModificaPrenotazioneSpa
    window.destroy()
    root = Tk()
    app = ModificaPrenotazioneSpa(root)
    centrare_finestra(root)
    root.mainloop()