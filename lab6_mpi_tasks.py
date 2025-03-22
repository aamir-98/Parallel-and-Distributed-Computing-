# DSAI 3202 - Lab 6
# Part 1: Calculate Squares using mpi4py

from mpi4py import MPI
import numpy as np
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Set upper bound
n = int(1e6)  # change to 1e8 for final version
chunk_size = n // size
start_index = rank * chunk_size
end_index = (rank + 1) * chunk_size if rank != size - 1 else n

start_time = time.time()

# Compute squares in range
local_squares = [i ** 2 for i in range(start_index + 1, end_index + 1)]

# Gather results at root
all_squares = comm.gather(local_squares, root=0)

if rank == 0:
    squares = [square for sublist in all_squares for square in sublist]
    print("Total squares computed:", len(squares))
    print("Last square:", squares[-1])
    print("Time taken:", time.time() - start_time, "seconds")

# Part 2: Virus Spread Simulation using MPI

import numpy as np

population_size = 100
spread_chance = 0.3
vaccination_rate = np.random.uniform(0.1, 0.5)

# Initialize population: 0 = uninfected, 1 = infected
population = np.zeros(population_size, dtype=int)

if rank == 0:
    infected_indices = np.random.choice(population_size, int(0.1 * population_size), replace=False)
    population[infected_indices] = 1

comm.Bcast(population, root=0)


def spread_virus(population):
    new_population = population.copy()
    for i in range(len(population)):
        if population[i] == 1:
            for j in range(len(population)):
                if population[j] == 0 and np.random.rand() < spread_chance * (1 - vaccination_rate):
                    new_population[j] = 1
    return new_population

# Simulate for 10 steps
for _ in range(10):
    population = spread_virus(population)
    if rank != 0:
        comm.send(population, dest=0)
    else:
        for i in range(1, size):
            received_data = comm.recv(source=i)
            population = np.bitwise_or(population, received_data)

# Calculate infection rate
infected_count = np.sum(population)
infection_rate = infected_count / population_size
print(f"Process {rank} Infection Rate: {infection_rate:.2f}")
