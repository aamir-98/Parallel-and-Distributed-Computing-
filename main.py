from src import train_model
# Run the threading-based training
print("\n--- Running Parallel Training with Threading ---\n")
train_model.train_threading()

# Run the multiprocessing-based training
print("\n--- Running Parallel Training with Multiprocessing ---\n")
train_model.train_multiprocessing()