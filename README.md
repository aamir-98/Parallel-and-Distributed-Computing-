# Genetic Algorithm for City Navigation

## Overview
This project implements a parallelized Genetic Algorithm (GA) to optimize the shortest route for a single vehicle delivering goods in a city. The algorithm minimizes the total travel distance using MPI4PY for distributed computing.

## Objectives
- Implement a Genetic Algorithm for the Traveling Salesman Problem (TSP)
- Optimize the route of a single vehicle
- Parallelize computation to improve performance

## Genetic Algorithm Explanation
Genetic Algorithms are optimization techniques inspired by natural selection. The main steps include:
1. **Initialization**: Generate a population of potential solutions (routes).
2. **Fitness Evaluation**: Calculate the total distance of each route.
3. **Selection**: Choose the best routes based on fitness.
4. **Crossover**: Create new routes by combining existing ones.
5. **Mutation**: Randomly modify routes to maintain diversity.
6. **Elitism**: Preserve the best routes from each generation.
7. **Termination**: Repeat the process until the algorithm converges or reaches a predefined number of generations.

## Implementation Details
### **1. Fitness Function**
- The fitness function calculates the total travel distance of a given route.
- A large penalty is applied for infeasible routes (disconnected paths).

### **2. Selection Method (Tournament Selection)**
- A subset of routes is randomly chosen.
- The best route among them is selected for reproduction.

### **3. Crossover (Order Crossover)**
- Two parent routes exchange genetic material to produce new routes.

### **4. Mutation**
- Two random cities in the route are swapped with a probability of `mutation_rate`.

### **5. Parallelization with MPI4PY**
- The genetic algorithm is distributed across multiple processes to improve efficiency.
- Fitness evaluation, crossover, and mutation operations are parallelized using `mpi4py`.

## Performance and Results
### **Execution Time**
- The program was executed using `mpiexec -n 4 python genetic_algorithm_trial.py`
- The execution time was approximately **20.3 seconds**.
- The best route found had a **total distance of 1265**.

### **Comparison with Sequential Execution**
| Approach       | Execution Time (seconds) | Best Distance |
|---------------|-------------------------|--------------|
| Sequential    | ~40-50                   | ~1400        |
| Parallel (MPI)| ~20.3                     | **1265**     |

## Enhancements Implemented
1. **Adaptive Mutation Rate**: The mutation probability decreases over generations to balance exploration and exploitation.
2. **Elitism**: Top-performing routes are preserved across generations.
3. **Regeneration on Stagnation**: If no improvement is seen for `5` generations, the population is regenerated.
4. **Parallelization with MPI**: Distributes fitness evaluation, selection, crossover, and mutation.

## Future Improvements
- Implement support for multiple delivery vehicles.
- Run the program on multiple machines using AWS.
- Explore alternative selection and mutation strategies.

## How to Run the Program
1. **Install Dependencies** (See `requirements.txt`)
   ```sh
   pip install -r requirements.txt
   ```
2. **Run the program in parallel using MPI**:
   ```sh
   mpiexec -n 4 python genetic_algorithm_trial.py
   ```
3. **Change the distance matrix to test on an extended city**
   ```sh
   mv city_distances_extended.csv city_distances.csv
   ```

## Repository Structure
```
/Parallel-and-Distributed-Computing
│── ShortestRoute/
│   ├── genetic_algorithm_trial.py   # Main script
│   ├── genetic_algorithms_functions.py # GA helper functions
│   ├── city_distances.csv          # Distance matrix (default)
│   ├── city_distances_extended.csv # Extended city map
│   ├── __init__.py                 # Package initializer
│── README.md
│── requirements.txt
```

## Thank you
## Aamir Ahmed 

