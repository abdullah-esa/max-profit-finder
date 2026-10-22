# experiments/benchmark.py

import time
import numpy as np
import pandas as pd
from src.divide_conquer import max_subarray_divide_conquer
from src.linear_scan import max_profit_linear

def benchmark_algorithms():
    """
    Measures and compares execution time of Linear Scan vs Divide-and-Conquer
    across varying dataset sizes (N).
    """
    sizes = [100, 500, 1000, 5000, 10000]
    results = []

    print("=" * 60)
    print(f"{'N Size':<10} | {'Linear Scan (s)':<18} | {'Divide & Conquer (s)':<20}")
    print("=" * 60)

    for n in sizes:
        # Generate synthetic price walk data
        np.random.seed(42)
        prices = np.clip(np.cumsum(np.random.randn(n) * 2) + 100, 1.0, None)
        changes = np.diff(prices)

        # Benchmark Linear Scan O(N) over multiple iterations for high precision
        iterations = 100
        start_time = time.perf_counter()
        for _ in range(iterations):
            max_profit_linear(prices)
        linear_time = (time.perf_counter() - start_time) / iterations

        # Benchmark Divide and Conquer O(N log N)
        start_time = time.perf_counter()
        for _ in range(iterations):
            if len(changes) > 0:
                max_subarray_divide_conquer(changes, 0, len(changes) - 1)
        dc_time = (time.perf_counter() - start_time) / iterations

        results.append({
            'N': n, 
            'Linear_Time_sec': linear_time, 
            'Divide_Conquer_Time_sec': dc_time
        })
        
        print(f"{n:<10} | {linear_time:<18.6f} | {dc_time:<20.6f}")

    print("=" * 60)

    # Save results to CSV for plotting or report generation
    df = pd.DataFrame(results)
    df.to_csv('experiments/benchmark_results.csv', index=False)
    print("\nBenchmark results successfully saved to 'experiments/benchmark_results.csv'!")

if __name__ == "__main__":
    benchmark_algorithms()
