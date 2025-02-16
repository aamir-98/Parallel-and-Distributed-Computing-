import sys
sys.path.append("./src")  
# Import the functions from src/
import sequential
import threading_parallel
import multiprocessing_parallel

if __name__ == "__main__":
    print("\n--- Running Sequential Sum ---")
    sequential.sequential_sum(10**7)  # Runs sequential sum
    
    print("\n--- Running Threaded Sum ---")
    threading_parallel.threaded_sum(10**7)  # Runs threaded sum
    
    print("\n--- Running Multiprocessing Sum ---")
    multiprocessing_parallel.multiprocessing_sum(10**7)  # Runs multiprocessing sum