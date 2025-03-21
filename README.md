# Parallel and Distributed Computing - Assignment 1 (Part 1)

## Overview
This project is part of Assignment 1 for the Parallel and Distributed Computing course (DSAI 3202). It focuses on comparing different approaches to parallel computation using Python, including **multiprocessing**, **threading**, and **semaphores**.

The primary goal is to compute squares of large lists of numbers efficiently and compare different parallelization techniques.

## Files Structure
```
/Parallel-and-Distributed-Computing/
├── src/
│   ├── __init__.py           # Package initialization
│   ├── square.py             # Function to compute square of a number
│   ├── sequential.py         # Sequential execution for benchmarking
│   ├── multiprocessing.py    # Multiprocessing implementation (process-based parallelism)
│   ├── semaphores.py         # Semaphore-based connection pool simulation
├── main.py                   # Entry point to run the program
├── README.md                 # Documentation file (this file)
├── requirements.txt          # Dependencies
```

## Installation
To run the project, ensure you have **Python 3.8+** installed along with the required dependencies.

1. Clone the repository:
   ```sh
   cd Parallel-and-Distributed-Computing-
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Mac/Linux
   venv\Scripts\activate     # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Execution
Run the `main.py` file to compare different computation methods:
```sh
python main.py
```

## Parallelization Methods Used
### 1. Sequential Execution
- Processes numbers one by one in a for-loop.
- Baseline for performance comparison.

### 2. Multiprocessing Approaches
- **Multiprocessing (one process per chunk)**: Uses multiple **Process** instances to distribute workload.
- **Pool.map()**: Uses a process pool to map function calls to multiple inputs.
- **Pool.apply()**: Calls `apply()` asynchronously in multiple processes.
- **ProcessPoolExecutor**: High-level multiprocessing using `concurrent.futures`.

### 3. Semaphore-Based Connection Pool
- Simulates a **database connection pool** with limited resources.
- Uses `multiprocessing.Semaphore` to control access.

## Expected Output
When running `python main.py`, you should see output similar to:
```
=== Running Square Computations ===

Sequential Execution:
Processed 1000000 numbers.
Time Taken: 0.0580 seconds

Multiprocessing (one process per number):
Processed 1000000 numbers.
Time Taken: 0.0590 seconds

Multiprocessing Pool (map):
Time Taken: 1.1127 seconds

Multiprocessing Pool (apply):
Time Taken: 167.9701 seconds

ProcessPoolExecutor:
Time Taken: 106.4556 seconds

=== Running Semaphore-Based Connection Pool ===
Process 0 waiting for connection...
Process 1 waiting for connection...
Process 2 waiting for connection...
Process 0 acquired Connection 0
Process 1 acquired Connection 1
Process 2 acquired Connection 2
Process 3 waiting for connection...
Process 4 waiting for connection...
Process 3 could not acquire a connection.
Process 2 releasing Connection 2
Process 2 releasing Connection 2
...
```

---
### Author: *Aamir Ahmed*
*Parallel and Distributed Computing - DSAI 3202*

