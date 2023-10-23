"""
Genetic Algorithm (GA) to solve Knapsack Problem

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
import random

import item

POPULATION_LIMIT = 5
GENERATION_LIMIT = 50
WEIGHT_LIMIT = 3000
ITEM_SET = [
    item.Item("Item 1", 5, 1000),
    item.Item("Item 2", 3, 500),
    item.Item("Item 3", 1, 3000),
    item.Item("Item 4", 4, 1300),
]

MUTATION_PROB = 0.15
TOLERANCE = 10


def create_individual():
    return [random.randint(0, 1) for _ in range(len(ITEM_SET))]


def create_population():
    possible = []
    while len(possible) < POPULATION_LIMIT and len(possible) < pow(2, len(ITEM_SET)):
        new_individual = create_individual()
        if new_individual in possible:
            continue
        possible.append(create_individual())
    return possible


def calculate_fitness(individual):
    weight = 0
    value = 0
    for i, state in enumerate(individual):
        if state == 0:
            continue
        weight += ITEM_SET[i].weight
        if weight > WEIGHT_LIMIT:
            return 0
        value += ITEM_SET[i].value
    return value


def tournament_selection(population):
    candidate_1, candidate_2 = random.sample(population, k=2)

    fitness_1 = calculate_fitness(candidate_1)
    fitness_2 = calculate_fitness(candidate_2)

    if fitness_1 > fitness_2:
        return candidate_1
    else:
        return candidate_2


def select_pair(population):
    parent_1 = tournament_selection(population)
    parent_2 = tournament_selection(population)
    return parent_1, parent_2


def crossover(parent_1, parent_2):
    offspring = []
    for s1, s2 in zip(parent_1, parent_2):
        prob = random.random()
        if prob < 0.5:
            offspring.append(s1)
        else:
            offspring.append(s2)

    if random.random() <= MUTATION_PROB:
        offspring = mutate(offspring)

    return offspring


def mutate(individual):
    idx = random.randrange(len(individual))
    individual[idx] = individual[idx] ^ 1
    return individual


def main():
    population = create_population()
    population.sort(key=lambda x: calculate_fitness(x), reverse=True)

    tol = 0
    past_best = population[0]
    for i in range(GENERATION_LIMIT):
        print(f"Gen {i+1}: {population[0]} --- {calculate_fitness(population[0])}")
        new_population = []
        while len(new_population) < POPULATION_LIMIT:
            parent_1, parent_2 = select_pair(population[: int(POPULATION_LIMIT * 0.5)])
            offspring = crossover(parent_1, parent_2)
            new_population.append(offspring)
        new_population.sort(key=lambda x: calculate_fitness(x), reverse=True)

        if past_best == new_population[0]:
            tol += 1
        else:
            tol = 0
            past_best = new_population[0]

        if tol == TOLERANCE:
            t = population[0]
            print(f"Found solution at Gen {i+1}: Value = {calculate_fitness(t)}")
            break

        population = new_population


if __name__ == "__main__":
    main()
