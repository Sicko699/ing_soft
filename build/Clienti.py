from main import multiplatform_open_read_data_json, multiplatform_open_read_current_user, multiplatform_open_write_data_json

class Cliente:
    def __init__(self):
        self.data_json = self.load_data_json()
        self.current_user = self.load_current_user()
        self.user_data = self.find_current_user_data()

    def load_data_json(self):
        return multiplatform_open_read_data_json()

    def load_current_user(self):
        return multiplatform_open_read_current_user()

    def find_current_user_data(self):
        username = self.current_user["username"]
        user_data = next((user for user in self.data_json[0]["users"] if user["username"] == username), None)
        if user_data is None:
            print("Utente non trovato.")
        return user_data

    def get_user_info(self):
        if self.user_data:
            nome = self.user_data.get("nome", "")
            cognome = self.user_data.get("cognome", "")
            email = self.user_data.get("email", "")
            telefono = self.user_data.get("telefono", "")
            username = self.user_data.get("username", "")
            password = self.user_data.get("password", "")
            return nome, cognome, email, telefono, username, password
        return None, None, None, None, None, None

    def update_user_info(self, nome, cognome, email, telefono, username, password):
        if self.user_data:
            for user in self.data_json[0]["users"]:
                if user["username"] == self.current_user["username"]:
                    user["nome"] = nome
                    user["cognome"] = cognome
                    user["email"] = email
                    user["telefono"] = telefono
                    user["username"] = username
                    user["password"] = password
                    break

            multiplatform_open_write_data_json(self.data_json)
            return True
        return False
