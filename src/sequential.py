import time
import random
from src.square import square

# Define global variable for list size
NUMBER_SIZE = 10**6  

def run_sequential():
    """Runs sequential square computation."""
    numbers = [random.randint(1, 100) for _ in range(NUMBER_SIZE)]

    start = time.time()
    results = [square(num) for num in numbers] 
    end = time.time()

    print(f"Processed {len(results)} numbers.")
    return end - start
