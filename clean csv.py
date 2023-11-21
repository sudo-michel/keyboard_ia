import requests
from bs4 import BeautifulSoup
import csv
import re

url = "https://fr.wiktionary.org/wiki/Wiktionnaire:Liste_de_1750_mots_fran%C3%A7ais_les_plus_courants"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Trouver toutes les balises <a> avec href et title
anchor_tags = soup.find_all('a', {'href': True, 'title': True})

# Liste pour stocker les mots extraits
tableau_mots = []

# Extraire le texte de chaque balise <a> et vérifier les caractères
for anchor_tag in anchor_tags:
    mot = anchor_tag.text.strip()
    # Vérifier si le mot ne contient que des caractères alphabétiques
    if re.match('^[a-zA-Z]+$', mot):
        tableau_mots.append(mot)

# Écrire les mots dans un fichier CSV
with open('mots_extraits_1.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Mots Extraits'])
    for mot in tableau_mots:
        writer.writerow([mot])

print("Les mots ont été extraits avec succès et enregistrés dans le fichier CSV.")
