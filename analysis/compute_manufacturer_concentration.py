"""Compute manufacturer concentration of FDA AI/ML device authorizations.

Reproduces Figure 4 of:
Golshani P, Joseph M. Three Decades of FDA Authorizations of AI/ML-Enabled
Medical Devices (1995-2025). Cureus 2026.
"""
import pandas as pd
from pathlib import Path

CSV = Path(__file__).parent.parent / "data" / "fda_aiml_devices_1995_2025.csv"

def tier(n):
    if n == 1:
        return "1 device (single-product firms)"
    if n <= 4:
        return "2-4 devices"
    if n <= 9:
        return "5-9 devices"
    return ">=10 devices (repeat authorizers)"

def main():
    df = pd.read_csv(CSV)
    counts = df.groupby("Company").size()
    n_companies = len(counts)
    n_devices = len(df)
    print(f"Total companies: {n_companies}")
    print(f"Total devices: {n_devices}\n")

    # bin
    tiers = ["1 device (single-product firms)",
             "2-4 devices",
             "5-9 devices",
             ">=10 devices (repeat authorizers)"]
    companies = {t: 0 for t in tiers}
    devices = {t: 0 for t in tiers}
    for company, n in counts.items():
        t = tier(n)
        companies[t] += 1
        devices[t] += n

    print(f"{'Tier':40s}  {'Companies':>10s}  {'Devices':>10s}")
    print("-" * 70)
    for t in tiers:
        c = companies[t]
        d = devices[t]
        c_pct = 100 * c / n_companies
        d_pct = 100 * d / n_devices
        print(f"{t:40s}  {c:5d} ({c_pct:4.1f}%)  {d:5d} ({d_pct:4.1f}%)")

    # top-10 and top-25 manufacturer counts
    top10 = counts.nlargest(10).sum()
    top25 = counts.nlargest(25).sum()
    print(f"\nTop 10 manufacturers: {top10} authorizations ({100*top10/n_devices:.1f}%)")
    print(f"Top 25 manufacturers: {top25} authorizations ({100*top25/n_devices:.1f}%)")
    print(f"Single largest manufacturer: {counts.max()} authorizations")

if __name__ == "__main__":
    main()
