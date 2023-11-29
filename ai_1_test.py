import random
import csv

TOTAL_KEYS = 30  # Nombre total de touches du clavier

def init_population(pop_size):
    # Fonction inchangée
    pass

def new_generation(population, sorted_evals, p_size):
    # Fonction inchangée
    pass

def mate(board1, board2):
    # Fonction inchangée
    pass

def load_word_list(file_path):
    # Fonction inchangée
    pass

def calculate_distance(layout, word):
    # Fonction inchangée
    pass

def write_generation_to_csv(generation, file_path):
    with open(file_path, mode='a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(generation)

# Exemple d'utilisation
population_size = 10
generations = 250  # Modifiez cette valeur si nécessaire
csv_file_path = 'generations_layouts.csv'  # Chemin du fichier CSV

# Vérifier si le fichier CSV existe déjà, sinon le créer avec l'entête
try:
    with open(csv_file_path, 'r') as csvfile:
        pass
except FileNotFoundError:
    with open(csv_file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([f'Touche {i+1}' for i in range(TOTAL_KEYS)])

# Initialiser la population
population = init_population(population_size)

# Charger la liste de mots
word_list = load_word_list('mots_extraits_1.csv')

# Variables pour le suivi de la convergence
layouts_generated = set()

# Boucle sur les générations
gen = 0
while gen < generations:
    # Évaluer la population en calculant la distance totale pour chaque layout
    evals = [sum(calculate_distance(layout, word) for word in word_list) for layout in population]

    # Trier la population en fonction de l'évaluation
    sorted_evals = sorted(range(len(evals)), key=lambda k: evals[k])

    # Récupérer le meilleur layout de cette génération
    current_best_layout = population[sorted_evals[0]]

    # Ajouter le layout à l'ensemble (pour éviter les doublons)
    layouts_generated.add(tuple(current_best_layout))

    # Imprimer le meilleur layout de la génération actuelle
    print(f'Génération {gen+1}: Meilleur layout - {current_best_layout}')

    # Écrire la génération dans le fichier CSV
    write_generation_to_csv(current_best_layout, csv_file_path)

    # Créer une nouvelle génération
    population = new_generation(population, sorted_evals, population_size)

    # Incrémenter le compteur de génération
    gen += 1
