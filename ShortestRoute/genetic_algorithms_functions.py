"""
Genetic Algorithm Helper Functions
-----------------------------------
This file contains various helper functions used in the Genetic Algorithm.
It includes:
- Fitness Calculation
- Adaptive Mutation Rate
- Local Search Optimization
- Tournament-Based Selection
- Order Crossover (OX)
- Mutation Operation
- Unique Population Generation

Author: Aamir Ahmed
Course: DSAI 3202 - Parallel & Distributed Computing
"""

import numpy as np

def compute_fitness(route, dist_matrix):
    """
    Evaluates the total distance of a given route.

    Args:
        route (list): A sequence representing city travel order.
        dist_matrix (numpy array): A 2D matrix where [i, j] is the distance from city i to city j.

    Returns:
        float: Negative of the total distance (for optimization).
    """
    total_distance = sum(dist_matrix[route[idx], route[idx + 1]] for idx in range(len(route) - 1))
    return -total_distance  # Negative for minimization


def adjust_mutation_rate(current_gen, max_gen, initial_prob=0.1, final_prob=0.01):
    """Gradually decreases mutation probability as generations progress."""
    return initial_prob - (initial_prob - final_prob) * (current_gen / max_gen)


def local_route_optimization(route, dist_matrix):
    """Performs a local optimization using a modified 2-opt swap technique."""
    improved = True
    while improved:
        improved = False
        for x in range(1, len(route) - 1):
            for y in range(x + 1, len(route)):
                temp_route = route[:x] + route[x:y][::-1] + route[y:]
                if compute_fitness(temp_route, dist_matrix) < compute_fitness(route, dist_matrix):
                    route = temp_route
                    improved = True
    return route


def tournament_selection(population, fitness_scores, num_rounds=4):
    """Executes a tournament-style selection to choose the best candidates."""
    chosen_routes = []
    for _ in range(num_rounds):
        contenders = np.random.choice(len(population), 3, replace=False)
        best_idx = contenders[np.argmin(fitness_scores[contenders])]
        chosen_routes.append(population[best_idx])
    return chosen_routes


def order_based_crossover(parent_A, parent_B):
    """Applies Order Crossover (OX) to produce a new route."""
    size = len(parent_A)
    start, stop = sorted(np.random.choice(range(size), 2, replace=False))
    
    child_route = [None] * size
    child_route[start:stop + 1] = parent_A[start:stop + 1]

    remaining_vals = [city for city in parent_B if city not in child_route[start:stop + 1]]
    index = 0

    for i in range(size):
        if child_route[i] is None:
            child_route[i] = remaining_vals[index]
            index += 1
            
    return child_route


def perform_mutation(route, mutation_prob=0.1):
    """Randomly swaps two cities within a route based on mutation probability."""
    if np.random.rand() < mutation_prob:
        a, b = np.random.choice(len(route), 2, replace=False)
        route[a], route[b] = route[b], route[a]
    return route


def generate_initial_population(pop_size, num_cities):
    """
    Generates an initial unique population of travel paths.
    
    Args:
        pop_size (int): Number of routes to generate.
        num_cities (int): Number of cities in the problem.

    Returns:
        list: A list of unique route sequences.
    """
    unique_routes = set()
    while len(unique_routes) < pop_size:
        new_route = [0] + list(np.random.permutation(np.arange(1, num_cities)))  
        unique_routes.add(tuple(new_route))  
    return [list(route) for route in unique_routes]
