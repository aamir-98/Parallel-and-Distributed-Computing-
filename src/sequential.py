import time
import random
import string

def generate_random_chars():
    letters = ''.join(random.choices(string.ascii_letters, k=1000))
    return letters

def generate_random_numbers():
    numbers = [random.randint(1, 100) for _ in range(1000)]
    return sum(numbers)

def run_sequential():
    start_time = time.time()
    generate_random_chars()
    generate_random_numbers()
    end_time = time.time()
    
    print(f"Time taken (Sequential Execution): {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    run_sequential()