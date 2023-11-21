import requests
from bs4 import BeautifulSoup
import csv

url = "https://fr.wiktionary.org/wiki/Wiktionnaire:Liste_de_1750_mots_fran%C3%A7ais_les_plus_courants"
response = requests.get(url)

# Imprimer le contenu HTML pour vérification
print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', {'class': 'wikitable'})

if table:
    rows = table.find_all('tr')
    tableau_mots = []

    for row in rows[1:]:
        cols = row.find_all(['td', 'th'])
        mot = cols[0].text.strip()
        tableau_mots.append(mot)

    with open('mots_extraits.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Mots Extraits'])
        for mot in tableau_mots:
            writer.writerow([mot])

    print("Les mots ont été extraits avec succès et enregistrés dans le fichier CSV.")
else:
    print("Aucun tableau trouvé avec la classe 'wikitable'. Vérifiez la structure de la page.")
