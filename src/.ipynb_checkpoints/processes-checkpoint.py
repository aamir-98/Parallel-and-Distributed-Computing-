import multiprocessing
import time
import random
import string

def generate_random_chars():
    letters = ''.join(random.choices(string.ascii_letters, k=1000))
    print("Generated 1000 random characters")

def generate_random_numbers():
    numbers = [random.randint(1, 100) for _ in range(1000)]
    print("Generated and summed 1000 random numbers")

def run_processes():
    start_time = time.time()

    process1 = multiprocessing.Process(target=generate_random_chars)
    process2 = multiprocessing.Process(target=generate_random_numbers)

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    end_time = time.time()
    print(f"Time taken (Multiprocessing): {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    run_processes()