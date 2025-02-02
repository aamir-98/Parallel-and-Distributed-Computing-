from src.sequential import run_sequential
from src.threading import run_threading
from src.processes import run_processes
from src.performance import compute_performance

if __name__ == "__main__":
    print("Running Sequential Execution...")
    run_sequential()

    print("\nRunning Threading Execution...")
    run_threading()

    print("\nRunning Multiprocessing Execution...")
    run_processes()

    print("\nComputing Performance Analysis...")
    compute_performance(sequential_time=1.5, parallel_time=0.8, num_units=2)  