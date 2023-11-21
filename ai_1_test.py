import random
import csv

TOTAL_KEYS = 30  # Nombre total de touches du clavier

def init_population(pop_size):
    keyboard_chars = list('azertyuiopqsdfghjklmwxcvbn,;:!')
    population = []

    for i in range(pop_size):
        rand_genome = random.sample(keyboard_chars, len(keyboard_chars))
        population.append(rand_genome)

    return population

def new_generation(population, sorted_evals, p_size):
    new_gen = []

    sorted_population = [population[i] for i in sorted_evals]

    # Copier les 10% meilleurs layouts dans la génération suivante
    new_gen.extend(sorted_population[:int(p_size * 0.1)])

    # Combinez deux claviers de la génération précédente pour créer un nouveau
    for _ in range(int(p_size * 0.9)):
        p1 = random.choice(sorted_population[:int(p_size * 0.5)])
        p2 = random.choice(sorted_population[:int(p_size * 0.5)])
        child = mate(p1, p2)
        new_gen.append(child)

    return new_gen

def mate(board1, board2):
    idx = random.randint(0, TOTAL_KEYS - 1)
    length = random.randint(1, TOTAL_KEYS - 1)
    child = ['_' for _ in range(TOTAL_KEYS)]

    # Ajouter les touches du clavier 1
    for _ in range(length):
        if idx >= TOTAL_KEYS:
            idx = 0
        child[idx] = board1[idx]
        idx += 1

    # Ajouter les touches restantes du clavier 2
    child_idx = list(range(idx, idx + length))
    child_idx = [i % TOTAL_KEYS for i in child_idx]
    for idx, child_index in enumerate(child_idx):
        child[child_index] = board2[idx]

    # 10% de chance de mutation
    prob = random.random()
    if prob >= 0.9:
        point1, point2 = random.sample(range(TOTAL_KEYS), 2)
        child[point1], child[point2] = child[point2], child[point1]

    return child

def load_word_list(file_path):
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        word_list = [row[0] for row in reader]
    return word_list

def calculate_distance(layout, word):
    distance = 0
    for i in range(len(word) - 1):
        char1 = word[i]
        char2 = word[i + 1]

        # Vérifier si les caractères sont présents dans le layout
        if char1 not in layout or char2 not in layout:
            continue

        # Trouver les indices des caractères dans la disposition du clavier
        index1 = layout.index(char1)
        index2 = layout.index(char2)

        # Calculer la distance entre les deux touches
        distance += abs(index1 - index2)

    return distance

# Exemple d'utilisation
population_size = 10
generations = 5

# Initialiser la population
population = init_population(population_size)

# Charger la liste de mots
word_list = load_word_list('mots_extraits_1.csv')

for gen in range(generations):
    # Évaluer la population en calculant la distance totale pour chaque layout
    evals = []
    for layout in population:
        total_distance = sum(calculate_distance(layout, word) for word in word_list)
        evals.append(total_distance)

    # Trier la population en fonction de l'évaluation
    sorted_evals = sorted(range(len(evals)), key=lambda k: evals[k])

    # Afficher la meilleure disposition du clavier de cette génération
    print(f"Meilleur layout de la génération {gen + 1}: {population[sorted_evals[0]]}")

    # Créer une nouvelle génération
    population = new_generation(population, sorted_evals, population_size)
