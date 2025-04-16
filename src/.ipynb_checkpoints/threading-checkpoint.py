import threading
import time
import random
import string

def generate_random_chars():
    letters = ''.join(random.choices(string.ascii_letters, k=1000))
    print("Generated 1000 random characters")

def generate_random_numbers():
    numbers = [random.randint(1, 100) for _ in range(1000)]
    print("Generated and summed 1000 random numbers")

def run_threading():
    start_time = time.time()

    thread1 = threading.Thread(target=generate_random_chars)
    thread2 = threading.Thread(target=generate_random_numbers)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    end_time = time.time()
    print(f"Time taken (Threading): {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    run_threading()