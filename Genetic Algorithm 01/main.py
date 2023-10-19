"""
Simple Genetic Algorithm (GA)

1. Individual - Potential Solution
2. Population - Collection of Individual
3. Generation
4. Fitness Score
5. Selection Process
6. Crossover Function
7. Mutation
8. Elitism

Termination Conditions:
9. Reach generation limit
10. Found optimum solution
"""

import string
import random

TARGET = "I love Python"
GENES = string.ascii_letters + " "
GENERATION_LIMIT = 100
POPULATION_LIMIT = 100


def create_inidividual():
    return "".join(random.choices(GENES, k=len(TARGET)))


def create_population():
    return [create_inidividual() for _ in range(POPULATION_LIMIT)]


def fitness_score(individu):
    score = 0
    for gene_i, gene_tar in zip(individu, TARGET):
        if gene_i == gene_tar:
            score += 1
    return score


def select_pair(population):
    score_map = [fitness_score(individu) for individu in population]
    return random.choices(population, weights=score_map, k=2)


def crossover(parent_a, parent_b):
    offspring = ""
    for gene_a, gene_b in zip(parent_a, parent_b):
        prob = random.random()
        if prob < 0.45:
            offspring += gene_a
        elif prob < 0.9:
            offspring += gene_b
        else:
            offspring += mutate_gene()
    return offspring


def mutate_gene():
    return random.choice(GENES)


def main():
    population = create_population()
    for i in range(GENERATION_LIMIT):
        population = sorted(population, key=lambda x: fitness_score(x), reverse=True)
        print(f"Generation [{i}] : {population[:3]}")

        if population[0] == TARGET:
            print(f"Solution Found in Generation {i}")
            break

        new_generation = population[: int(POPULATION_LIMIT * 0.05)]

        while len(new_generation) < POPULATION_LIMIT:
            parent_a, parent_b = select_pair(population[: int(POPULATION_LIMIT * 0.5)])
            offspring = crossover(parent_a, parent_b)
            new_generation.append(offspring)

        population = new_generation
    else:
        population = sorted(population, key=lambda x: fitness_score(x), reverse=True)
        print(f"Solution Not Found: {population[:3]}")


main()
