import random

TOTAL_KEYS = 30  # Nombre total de touches du clavier

# Create starting population of the Ist generation
def init_population(pop_size):
    keyboard_chars = list('azertyuiopqsdfghjklmwxcvbn,;:!')

    population = []

# Initialize population with random layouts
    for i in range(pop_size):
        rand_genome = keyboard_chars[:]
        random.shuffle(rand_genome)
        population.append(rand_genome)

    return population

# create the next generation of layouts
def new_generation(population, sorted_evals, p_size):
    new_gen = []

    # sort the population by distance
    sorted_population =[]
    for i in sorted_evals:
        sorted_population.append(population[i])


    # copy the best 10% of layout to the next generation

    for i in range(int(p_size*0.1)):
        new_gen.append(sorted_population[i])

    # combine two keyborads from the previous generation to create a new one

    for _ in range(int(p_size*0.9)):
        p1 = random.choice(sorted_population[:int(p_size*0.5)])
        p2 = random.choice(sorted_population[:int(p_size*0.5)])
        child = mate(p1, p2)
        new_gen.append(child)

    return new_gen


# combine two keyborads together
def mate(board1, board2):
    idx = random.randint(0, 29)
    length = random.randint(1, 29)
    child = ['_' for i in range(30)]

    # add keys from keyboard 1
    for i in range(length):
        if idx > 29:
            idx = 0
        child[idx] = board1[idx]
        idx += 1

    # add remining keys from keyboard 2
    child_idx = idx
    while '_' in child:
        if idx > 29:
            idx = 0
        if child_idx > 29:
            child_idx = 0
        char =  board2[idx]
        if char in child:
            idx += 1
            continue
        child[child_idx] = board2[idx]
        child_idx += 1
        idx += 1

    # 10% chance of mutation
    prob = random.random()
    if prob >= 0.9:
        point1 = random.randint(0, 29)
        point2 = random.randint(0, 29)
        allele1 = child[point1]
        allele2 = child[point2]
        child[point1] = allele2
        child[point2] = allele1

    return child

