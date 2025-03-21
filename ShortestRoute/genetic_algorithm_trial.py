"""
Parallelized Genetic Algorithm for Solving TSP (Traveling Salesman Problem)
-----------------------------------------------------------------------------
This script implements a **parallelized** Genetic Algorithm to find 
the shortest path in the Traveling Salesman Problem (TSP).

Techniques Utilized:
- Tournament Selection
- Order Crossover (OX)
- Adaptive Mutation
- Elitism
- Local Search Optimization

Parallel processing is applied for:
- Fitness evaluation
- Crossover and mutation
- Local search optimizations

Author: Aamir Ahmed
Course: DSAI 3202 - Parallel & Distributed Computing
"""

import numpy as np
import pandas as pd
import multiprocessing
from genetic_algorithms_functions import (
    compute_fitness, tournament_selection, order_based_crossover, perform_mutation, 
    generate_initial_population, adjust_mutation_rate, local_route_optimization
)

# Load Distance Matrix
dist_matrix = pd.read_csv('city_distances.csv').to_numpy()

# Genetic Algorithm Parameters
elite_count = 2  # Number of top individuals retained
city_count = dist_matrix.shape[0]  # Number of cities in the dataset
population_size = 10000  # Population size
tournament_rounds = 4  # Number of tournament rounds
mutation_prob = 0.1  # Initial mutation probability
max_generations = 200  # Maximum allowed generations
stagnation_limit = 5  # Threshold before population reset

# Initialize Population
np.random.seed(42)  # Ensure reproducibility
routes_population = generate_initial_population(population_size, city_count)
best_score = float('inf')  # Best fitness tracker
stagnation_counter = 0  # Stagnation monitor

import time
start_timer = time.time()  # Start execution timer

# Set up parallel processing pool
pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())

# Main Evolution Loop
for generation in range(max_generations):
    """
    Performs the evolutionary cycle including:
    - Fitness computation
    - Selection using tournaments
    - Crossover
    - Mutation
    - Local search refinement
    """

    # Compute Fitness in Parallel
    fitness_values = np.array([-compute_fitness(route, dist_matrix) for route in routes_population])
    current_best = np.min(fitness_values)
    
    # Track Best Performance & Detect Stagnation
    if current_best < best_score:
        best_score = current_best
        stagnation_counter = 0  # Reset stagnation counter
    else:
        stagnation_counter += 1  # Increment if no improvement

    # Reset Population if Stagnation Occurs
    if stagnation_counter >= stagnation_limit:
        print(f"⚠️ Population reset triggered at generation {generation} due to stagnation")
        best_route = routes_population[np.argmin(fitness_values)]
        routes_population = generate_initial_population(population_size - 1, city_count)
        routes_population.append(best_route)
        stagnation_counter = 0
        continue

    # Adjust Mutation Probability
    mutation_prob = adjust_mutation_rate(generation, max_generations)

    # Preserve Elite Solutions
    elite_indices = np.argsort(fitness_values)[:elite_count]
    elite_routes = [routes_population[i] for i in elite_indices]

    # Selection & Crossover (Parallelized)
    selected_parents = tournament_selection(routes_population, fitness_values)
    offspring_routes = pool.starmap(order_based_crossover, [(selected_parents[i][1:], selected_parents[i + 1][1:]) for i in range(0, len(selected_parents), 2)])
    offspring_routes = [[0] + child for child in offspring_routes]  # Ensure city 0 is the starting point

    # Mutation (Parallelized)
    mutated_offspring = pool.starmap(perform_mutation, [(route, mutation_prob) for route in offspring_routes])

    # Local Search Refinement (Parallelized)
    best_idx = np.argmin(fitness_values)
    routes_population[best_idx] = pool.apply(local_route_optimization, (routes_population[best_idx], dist_matrix))

    # Restore Elite Individuals
    for i in range(elite_count):
        routes_population[np.argmax(fitness_values)] = elite_routes[i]

    # Display Progress
    print(f"Generation {generation}: Best fitness = {current_best}")

# Execution Time
end_timer = time.time()
print(f"✅ Execution Duration: {end_timer - start_timer:.2f} seconds")

# Evaluate & Output Best Route
fitness_values = np.array([-compute_fitness(route, dist_matrix) for route in routes_population])
best_idx = np.argmin(fitness_values)
best_route_found = routes_population[best_idx]
print("🏆 Optimal Route Found:", best_route_found)
print("📏 Total Distance:", -compute_fitness(best_route_found, dist_matrix))

# Clean Up Processing Pool
pool.close()
pool.join()
