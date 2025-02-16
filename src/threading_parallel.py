import time
import threading

def partial_sum(start, end, result, index):
    """Compute sum of numbers from start to end and store in result list."""
    result[index] = sum(range(start, end))

def threaded_sum(n, num_threads=4):
    """Compute sum of numbers from 1 to n using threads."""
    start_time = time.time()
    
    step = n // num_threads
    threads = []
    result = [0] * num_threads  # Store results from each thread

    for i in range(num_threads):
        start = i * step + 1
        end = (i + 1) * step + 1 if i != num_threads - 1 else n + 1
        thread = threading.Thread(target=partial_sum, args=(start, end, result, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join() 

    total = sum(result)  
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Threaded Sum: {total}")
    print(f"Execution Time (Threads): {execution_time:.6f} seconds")

if __name__ == "__main__":
    threaded_sum(10**7)