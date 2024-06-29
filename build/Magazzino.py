from datetime import datetime, timedelta
from main import multiplatform_open_read_data_json, multiplatform_open_write_data_json
import json

class Magazzino:
    @staticmethod
    def aggiungi_ordine(ordine):
        try:
            data = multiplatform_open_read_data_json()
            magazzino = data[3]["magazzino"]  # Assumendo che gli ordini magazzino siano nel quarto elemento di data
            magazzino.append(ordine)
            multiplatform_open_write_data_json(data)
            return True
        except Exception as e:
            print("Si è verificato un errore durante l'aggiunta dell'ordine al file JSON:", e)
            return False

    @staticmethod
    def carica_ordine_corrente():
        with open("current_entry_ordine.json", "r") as user_json:
            current_entry = json.load(user_json)
        return current_entry

    @staticmethod
    def aggiorna_ordine(nome_articolo_vecchio, quantita_vecchia, data_consegna_vecchia, new_nome_articolo, new_quantita_articolo):
        try:
            data = multiplatform_open_read_data_json()

            new_data_ordine = datetime.now().strftime("%d-%m-%Y")
            new_data_spedizione = (datetime.now() + timedelta(days=1)).strftime("%d-%m-%Y")
            new_data_consegna = (datetime.now() + timedelta(days=3)).strftime("%d-%m-%Y")

            for ordine in data[-1]["magazzino"]:
                if ordine["nome_articolo"] == nome_articolo_vecchio and ordine["quantita"] == quantita_vecchia and ordine["consegna"] == data_consegna_vecchia:
                    ordine["nome_articolo"] = new_nome_articolo
                    ordine["quantita"] = new_quantita_articolo
                    ordine["data"] = new_data_ordine
                    ordine["spedizione"] = new_data_spedizione
                    ordine["consegna"] = new_data_consegna
                    break

            multiplatform_open_write_data_json(data)
            return True
        except Exception as e:
            print(f"Si è verificato un errore durante l'aggiornamento dell'ordine: {e}")
            return False