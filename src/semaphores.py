import time
import random
from multiprocessing import Semaphore, Process, Lock, Queue

class ConnectionPool:
    """Manages a limited number of connections using a semaphore."""
    
    def __init__(self, size):
        self.semaphore = Semaphore(size)
        self.lock = Lock() 
        self.queue = Queue()

        # Populate the queue with connections
        for i in range(size):
            self.queue.put(f"Connection {i}")

    def get_connection(self):
        """Acquires a connection from the pool."""
        self.semaphore.acquire()
        with self.lock: 
            if not self.queue.empty():
                return self.queue.get()
            else:
                self.semaphore.release() 
                return None

    def release_connection(self, conn):
        """Releases a connection back into the pool."""
        if conn:
            with self.lock:
                self.queue.put(conn)
            self.semaphore.release()

def access_database(pool, process_id):
    """Simulates database access by acquiring and releasing a connection."""
    print(f"Process {process_id} waiting for connection...")
    conn = pool.get_connection()
    if conn:
        print(f"Process {process_id} acquired {conn}")
        time.sleep(random.uniform(1, 3))  # Simulate database work
        print(f"Process {process_id} releasing {conn}")
        pool.release_connection(conn)
    else:
        print(f"Process {process_id} could not acquire a connection.")

def run_semaphore_test():
    """Runs the semaphore-based connection pool simulation."""
    pool_size = 3
    num_processes = 5
    pool = ConnectionPool(pool_size)
    
    processes = [Process(target=access_database, args=(pool, i)) for i in range(num_processes)]

    for p in processes:
        p.start()
    for p in processes:
        p.join()
