from main import multiplatform_open_read_data_json, multiplatform_open_read_current_user
import json, re, datetime

class Prenotazione:
    def __init__(self):
        self.data = multiplatform_open_read_data_json()
        self.current_user = multiplatform_open_read_current_user()

    def get_current_prenotazione(self):
        with open("current_entry_prenotazione_user.json", "r") as prenotazione_json:
            return json.load(prenotazione_json)

    def find_prenotazione(self, current_prenotazione):
        pattern = r'(\d{2}-\d{2}-\d{4}), (\d{2}-\d{2}-\d{4}), (.+)'
        match = re.search(pattern, current_prenotazione)
        if match:
            arrivo = match.group(1)
            partenza = match.group(2)
            tipo_camera = match.group(3)
            for user in self.data[0]['users']:
                if user['username'] == self.current_user['username'] and user['password'] == self.current_user['password']:
                    prenotazioni = user.get('prenotazioni', [])
                    for prenotazione in prenotazioni:
                        if prenotazione['arrivo'] == arrivo:
                            return prenotazione
        return None

    def check_availability(self, tipo_camera, data_arrivo, data_partenza):
        for categoria_camera in self.data[1]["camere"]:
            for tipo, camere in categoria_camera.items():
                if tipo == tipo_camera:
                    for camera in camere:
                        for numero_camera, prenotazioni in camera.items():
                            for prenotazione in prenotazioni:
                                if prenotazione["arrivo"] == "" and prenotazione["partenza"] == "":
                                    return True
                                if prenotazione["arrivo"] and prenotazione["partenza"]:
                                    arrivo_prenotazione = datetime.strptime(prenotazione["arrivo"], "%d-%m-%Y")
                                    partenza_prenotazione = datetime.strptime(prenotazione["partenza"], "%d-%m-%Y")
                                    if (data_arrivo < partenza_prenotazione and data_partenza > arrivo_prenotazione) or \
                                            (data_arrivo == arrivo_prenotazione and data_partenza == partenza_prenotazione):
                                        return False
                    return True
        return False

    def update_prenotazione(self, arrivo, partenza, tipo_camera, new_arrivo, new_partenza, new_tipo_camera):
        for user in self.data[0]['users']:
            if user['username'] == self.current_user['username'] and user['password'] == self.current_user['password']:
                prenotazioni = user.get('prenotazioni', [])
                for prenotazione in prenotazioni:
                    if prenotazione['arrivo'] == arrivo and prenotazione['partenza'] == partenza and prenotazione['tipo'] == tipo_camera:
                        prenotazione['arrivo'] = new_arrivo
                        prenotazione['partenza'] = new_partenza
                        prenotazione['tipo'] = new_tipo_camera
                        with open("data.json", "w") as file:
                            json.dump(self.data, file, indent=4)
                        return True
        return False

    def load_data(self):
        # Logica per caricare i dati da JSON
        return multiplatform_open_read_data_json()

    def load_current_user(self):
        # Logica per caricare l'utente corrente da JSON
        return multiplatform_open_read_current_user()

    def get_user_prenotazioni(self):
        if self.data and self.current_user:
            users = self.data[0]['users']
            for user in users:
                if user['username'] == self.current_user['username'] and user['password'] == self.current_user['password']:
                    return user.get('prenotazioni', [])
        return []

    def get_prenotazione_details(self, id_prenotazione):
        camere = self.data[1]['camere']
        for tipo_camera in camere:
            for tipo, camere_tipo in tipo_camera.items():
                for camera in camere_tipo:
                    for numero_camera, dettagli in camera.items():
                        for dettaglio in dettagli:
                            if dettaglio.get('id_prenotazione') == id_prenotazione:
                                return dettaglio
        return None

    def delete_prenotazione(self, arrivo, partenza, tipo_camera):
        # Elimina la prenotazione dall'utente
        for user in self.data[0]['users']:
            if user['username'] == self.current_user['username'] and user['password'] == self.current_user['password']:
                prenotazioni = user.get('prenotazioni', [])
                for prenotazione in prenotazioni:
                    if prenotazione['arrivo'] == arrivo and prenotazione['partenza'] == partenza:
                        prenotazioni.remove(prenotazione)
                        break

        # Elimina la prenotazione dalle camere
        for tipo_camera_data in self.data[1]['camere']:
            if tipo_camera in tipo_camera_data:
                camere = tipo_camera_data[tipo_camera]
                for camera in camere:
                    for numero_camera, dettagli in camera.items():
                        for dettaglio in dettagli:
                            if dettaglio['arrivo'] == arrivo and dettaglio['partenza'] == partenza and \
                                    self.current_user['username'] == self.current_user['username']:
                                dettagli.remove(dettaglio)
                                with open("data.json", "w") as file:
                                    json.dump(self.data, file, indent=4)
                                return True
        return False