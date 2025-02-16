import time

def sequential_sum(n):
    """Compute sum of numbers from 1 to n using a loop (manual calculation)."""
    start_time = time.time()  # Start timer
    total = 0
    for i in range(1, n + 1):
        total += i  
    end_time = time.time()  # End timer

    execution_time = end_time - start_time  # Calculate time taken
    print(f"Sequential Sum: {total}")
    print(f"Execution Time: {execution_time:.6f} seconds")

if __name__ == "__main__":
    sequential_sum(10**7)  