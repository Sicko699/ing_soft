from tkinter import Tk

def exit_button(window):
    from LoginApp import LoginApp
    window.destroy()
    root = Tk()
    app = LoginApp(root)
    root.mainloop()

def go_home_button(window):
    from MainApp import MainApp
    window.destroy()
    root = Tk()
    app = MainApp(root)
    root.mainloop()

def go_front_office_button(window):
    from FrontOfficeApp import FrontOfficeApp
    window.destroy()
    root = Tk()
    app = FrontOfficeApp(root)
    root.mainloop()

def go_back_office_button(window):
    from BackOfficeApp import BackOfficeApp
    window.destroy()
    root = Tk()
    app = BackOfficeApp(root)
    root.mainloop()
    
def go_gestione_magazzino(window):
    from GestioneOrdiniMagazzinoApp import GestioneOrdiniMagazzino
    window.destroy()
    root = Tk()
    app = GestioneOrdiniMagazzino(root)
    root.mainloop()
    
def go_gestione_servizi(window):
    from GestioneServiziApp import GestioneServizi
    window.destroy()
    root = Tk()
    app = GestioneServizi(root)
    root.mainloop()
    
def go_gestione_spa(window):
    from GestionePrenotazioniSpaApp import GestionePrenotazioniSpa
    window.destroy()
    root = Tk()
    app = GestionePrenotazioniSpa(root)
    root.mainloop()
    
def go_home_button_user(window):
    from CercaCamereApp import CercaCamere
    window.destroy()
    root = Tk()
    app = CercaCamere(root)
    root.mainloop()

def go_mostra_prenotazione(window):
    from MostraPrenotazioneApp import MostraPrenotazioneApp
    window.destroy()
    root = Tk()
    app = MostraPrenotazioneApp(root)
    root.mainloop()
    
def go_cerca_camere(window):
    from CercaCamereApp import CercaCamere
    window.destroy()
    root = Tk()
    app = CercaCamere(root)
    root.mainloop()
    
def go_lista_prenotazioni(window):
    from ListaPrenotazioni import ListaPrenotazioni
    window.destroy()
    root = Tk()
    app = ListaPrenotazioni(root)
    root.mainloop()
    
def go_modifica_profilo(window):
    from ModificaProfilo import ModificaProfilo
    window.destroy()
    root = Tk()
    app = ModificaProfilo(root)
    root.mainloop()    
    
def go_nuova_prenotazione_spa(window):
    from NuovaPrenotazioneSpaApp import NuovaPrenotazioneSpa
    window.destroy()
    root = Tk()
    app = NuovaPrenotazioneSpa(root)
    root.mainloop()
    
def go_modifica_prenotazione_spa(window):
    from ModificaPrenotazioneSpa import ModificaPrenotazioneSpa
    window.destroy()
    root = Tk()
    app = ModificaPrenotazioneSpa(root)
    root.mainloop()