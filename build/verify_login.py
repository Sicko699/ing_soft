import platform, json

def verify_login(username, password):
        if platform.system() == "Darwin":
            with open("data.json", "r") as file:
                data = json.load(file)
        else:
            with open(r"build/data.json", "r") as file:
                data = json.load(file)

        users_data = data[0]["users"]  # Accedi al primo elemento della lista e quindi a "users" nel dizionario
        for user in users_data:
            if user["username"] == username and user["password"] == password and user["role"] == "admin":
                return "admin"
            elif user["username"] == username and user["password"] == password and user["role"] == "utente":
                return "utente"

        return False