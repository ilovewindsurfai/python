import csv
import json
import requests

def read_csv(file_path):
    data = []
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
    except Exception as e:
        print(f"Erreur lors de la lecture du fichier CSV: {e}")
    return data

def map_to_json_template(csv_row, json_template):
    # Créer une copie du modèle JSON pour éviter de modifier l'original
    mapped_data = json_template.copy()

    # Mapper les valeurs du CSV aux champs du modèle JSON
    for key, value in csv_row.items():
        if key in mapped_data:
            mapped_data[key] = value

    return mapped_data

def send_to_api(api_url, json_data):
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(api_url, headers=headers, json=json_data)
        if response.status_code == 200:
            print("Données envoyées avec succès.")
            return response.json()
        else:
            print(f"Erreur: {response.status_code}")
            print(f"Réponse: {response.text}")
            return None
    except Exception as e:
        print(f"Une erreur s'est produite: {e}")
        return None

# Exemple d'utilisation
csv_file_path = 'chemin/vers/votre/fichier.csv'  # Remplacez par le chemin de votre fichier CSV
api_url = 'https://example.com/api/post'  # Remplacez par l'URL de votre API

# Modèle JSON (exemple)
json_template = {
    "name": "",
    "age": "",
    "email": ""
}

csv_data = read_csv(csv_file_path)
for row in csv_data:
    json_data = map_to_json_template(row, json_template)
    response = send_to_api(api_url, json_data)
    if response:
        print("Réponse de l'API:", response)
