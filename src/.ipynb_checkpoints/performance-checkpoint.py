def compute_performance(sequential_time, parallel_time, num_units):
    speedup = sequential_time / parallel_time
    efficiency = speedup / num_units
    amdahls_speedup = 1 / ((1 - 0.9) + (0.9 / num_units))  # Assuming 90% parallelizable workload
    gustafsons_speedup = num_units - (0.1 * (num_units - 1))  # Assuming 10% serial workload

    print(f"Speedup: {speedup:.2f}")
    print(f"Efficiency: {efficiency:.2f}")
    print(f"Amdahl's Speedup: {amdahls_speedup:.2f}")
    print(f"Gustafson's Speedup: {gustafsons_speedup:.2f}")

if __name__ == "__main__":
    compute_performance(sequential_time=1.5, parallel_time=0.8, num_units=2)  # Replace with actual values