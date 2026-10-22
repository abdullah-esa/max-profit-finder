# tests/test_algorithms.py

import numpy as np
import pytest
from faker import Faker
from src.divide_conquer import max_subarray_divide_conquer
from src.linear_scan import max_profit_linear

fake = Faker()

def solve_divide_and_conquer(prices):
    """Helper wrapper to format raw prices into daily changes for D&C."""
    changes = np.diff(prices)
    if len(changes) == 0:
        return 0, 0, 0.0
    buy_idx, sell_idx, profit = max_subarray_divide_conquer(changes, 0, len(changes) - 1)
    # D&C operates on differences, so sell index is shifted by +1 in the price array
    return buy_idx, sell_idx + 1, float(profit)


# =====================================================================
# 1. Deterministic Edge Cases
# =====================================================================
@pytest.mark.parametrize("case_name, prices", [
    ("Strictly Decreasing", [150.0, 130.0, 110.0, 90.0, 70.0]),
    ("Strictly Increasing", [10.0, 25.0, 45.0, 80.0, 120.0]),
    ("Flat Market", [50.0, 50.0, 50.0, 50.0, 50.0]),
    ("Single Valley", [100.0, 80.0, 60.0, 90.0, 110.0]),
    ("Peak at Start", [200.0, 100.0, 50.0, 25.0, 10.0]),
])
def test_edge_cases(case_name, prices):
    """Validates algorithms against well-defined market behaviors."""
    lin_buy, lin_sell, lin_profit = max_profit_linear(prices)
    dc_buy, dc_sell, dc_profit = solve_divide_and_conquer(prices)

    # Both approaches must agree on the exact maximum profit
    assert pytest.approx(lin_profit, rel=1e-5) == dc_profit, f"Failed on {case_name}"


# =====================================================================
# 2. Randomized Property Testing with Faker & NumPy
# =====================================================================
def test_randomized_market_simulations():
    """
    Generates 50 randomized market datasets using Faker for mock metadata 
    and NumPy random walks for price trajectories. Verifies O(N log N) D&C 
    matches O(N) Linear Scan on every iteration.
    """
    np.random.seed(42) # Reproducible randomness for unit testing

    for iteration in range(50):
        # Use Faker to generate mock asset name context for test logging
        mock_company = fake.company()
        mock_ticker = fake.lexify(text="???").upper()
        
        # Randomize dataset length between 10 and 300 days
        n_days = np.random.randint(10, 300)
        
        # Generate random price walk using normal distribution noise
        base_price = np.random.uniform(20.0, 1000.0)
        daily_volatility = np.random.normal(loc=0.05, scale=3.0, size=n_days)
        prices = np.clip(np.cumsum(np.concatenate([[base_price], daily_volatility])), 1.0, None)

        # Run both algorithms
        lin_buy, lin_sell, lin_prof = max_profit_linear(prices)
        dc_buy, dc_sell, dc_prof = solve_divide_and_conquer(prices)

        # Assert equivalence
        error_msg = (
            f"\n[Iteration {iteration + 1}] Asset: {mock_company} ({mock_ticker})\n"
            f"Dataset Size: {n_days} days\n"
            f"Linear Profit: {lin_prof:.4f} | D&C Profit: {dc_prof:.4f}\n"
        )
        assert pytest.approx(lin_prof, rel=1e-4) == dc_prof, error_msg