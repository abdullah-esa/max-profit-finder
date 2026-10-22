# experiments/generate_charts.py

import pandas as pd
import matplotlib.pyplot as plt
import os

def generate_performance_chart():
    # Load benchmark results
    csv_path = 'experiments/benchmark_results.csv'
    if not os.path.exists(csv_path):
        print("Error: benchmark_results.csv not found. Run benchmark.py first!")
        return

    df = pd.read_csv(csv_path)

    # Ensure output directory exists
    os.makedirs('docs/figures', exist_ok=True)

    # Plotting
    plt.figure(figsize=(8, 5))
    plt.plot(df['N'], df['Linear_Time_sec'], marker='o', label='Linear Scan O(N)', color='#2563eb', linewidth=2)
    plt.plot(df['N'], df['Divide_Conquer_Time_sec'], marker='s', label='Divide & Conquer O(N log N)', color='#dc2626', linewidth=2)

    plt.title('Algorithm Performance Benchmark: Max Profit Finder', fontsize=12, fontweight='bold')
    plt.xlabel('Dataset Size (N days)', fontsize=10)
    plt.ylabel('Execution Time (seconds)', fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()

    # Save figure
    output_path = 'docs/figures/benchmark_plot.png'
    plt.savefig(output_path, dpi=300)
    print(f"Performance chart successfully saved to '{output_path}'!")

if __name__ == "__main__":
    generate_performance_chart()