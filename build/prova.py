from main import multiplatform_open_read_data_json

data = multiplatform_open_read_data_json()

for tipo_camera, prenotazioni in data[1]['camere'][0].items():
    for camera_numero, camera_prenotazioni in prenotazioni[0].items():
        for prenotazione in camera_prenotazioni:
            if prenotazione['arrivo'] and prenotazione['partenza']:
                print("Arrivo:", prenotazione['arrivo'])
                print("Partenza:", prenotazione['partenza'])
                print("Nome:", prenotazione['nome'])
                print("Cognome:", prenotazione['cognome'])
                print("Numero ospiti:", prenotazione['numero_ospiti'])
                print("Tipo camera:", prenotazione['tipo_camera'])
                print()
                
print(enumerate(data[1]["camere"][0].items()))