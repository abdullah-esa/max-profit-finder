# Max Profit Finder: Divide-and-Conquer vs. Linear Scan

An algorithmic analysis project implementing the **Maximum Subarray Problem** to find the best stock buy and sell windows. It compares an $O(N \log N)$ Divide-and-Conquer approach against an $O(N)$ Linear Scan (Kadane's Algorithm).

---

## 📁 Repository Architecture

```text
max-profit-finder/
├── README.md               # Project overview and user guide
├── src/                    # Core algorithm implementations
│   ├── divide_conquer.py   # O(N log N) recursive D&C approach
│   └── linear_scan.py      # O(N) single-pass greedy approach
├── tests/                  # Automated test suite
│   └── test_algorithms.py  # Pytest unit tests & Faker randomized simulations
├── experiments/            # Performance testing scripts
│   ├── benchmark.py        # Execution timing script
│   └── generate_charts.py  # Matplotlib visualization generator
├── data/                   # Input datasets
│   └── stock_prices.csv    # Sample time-series price data
├── docs/                   # Academic report and diagrams
│   ├── report.md           # Two-page formal report
│   └── figures/            # Benchmark performance plots
├── demo/                   # Video walkthrough assets
│   └── script.md           # 5-minute video presentation script
└── REFLECTION.md           # Personal insights and future work

```

---

## 🚀 Step-by-Step Usage Guide

### For Normal Users (Cross-Platform)

1. **Clone or Download** the project repository.
2. **Install Dependencies:**
```bash
pip install pandas numpy pytest faker matplotlib

```


3. **Run Unit Tests:**
```bash
pytest -v

```


4. **Run Performance Benchmarks:**
```bash
PYTHONPATH=. python experiments/benchmark.py

```


5. **Generate Performance Charts:**
```bash
PYTHONPATH=. python experiments/generate_charts.py

```



### For Linux (Fedora) Users

1. **Install Prerequisites (DNF):**
```bash
sudo dnf update -y
sudo dnf install -y python3 python3-pip git

```


2. **Install Dependencies (in your active virtual environment or conda):**
```bash
pip install pandas numpy pytest faker matplotlib

```


3. **Run Unit Tests:**
```bash
PYTHONPATH=. python -m pytest tests/test_algorithms.py -v

```


4. **Run Benchmarks & Generate Graphs:**
```bash
PYTHONPATH=. python experiments/benchmark.py
PYTHONPATH=. python experiments/generate_charts.py

```



