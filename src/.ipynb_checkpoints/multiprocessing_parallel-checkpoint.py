import time
import multiprocessing

def process_sum(start, end, queue):
    """Compute sum of numbers from start to end and put in queue."""
    queue.put(sum(range(start, end)))

def multiprocessing_sum(n, num_processes=multiprocessing.cpu_count()):  
    """Compute sum of numbers from 1 to n using multiprocessing."""
    start_time = time.time()

    step = n // num_processes
    processes = []
    queue = multiprocessing.Queue()

    for i in range(num_processes):
        start = i * step + 1
        end = (i + 1) * step + 1 if i != num_processes - 1 else n + 1
        process = multiprocessing.Process(target=process_sum, args=(start, end, queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()  # Wait for all processes to finish

    total = sum(queue.get() for _ in range(num_processes))  # Combine results
    end_time = time.time()

    execution_time = end_time - start_time
    print(f"Multiprocessing Sum: {total}")
    print(f"Execution Time (Processes): {execution_time:.6f} seconds")

if __name__ == "__main__":
    multiprocessing_sum(10**7)