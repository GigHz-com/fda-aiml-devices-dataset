"""Compute annual and cumulative FDA AI/ML device authorization counts.

Reproduces Figure 1 of:
Golshani P, Joseph M. Three Decades of FDA Authorizations of AI/ML-Enabled
Medical Devices (1995-2025). Cureus 2026.
"""
import pandas as pd
from pathlib import Path

CSV = Path(__file__).parent.parent / "data" / "fda_aiml_devices_1995_2025.csv"

def main():
    df = pd.read_csv(CSV)
    df["year"] = pd.to_datetime(df["Date of Final Decision"]).dt.year
    annual = df.groupby("year").size().sort_index()
    cumulative = annual.cumsum()

    total = len(df)
    print(f"Total authorizations: {total}\n")

    print(f"{'Year':>6s}  {'Annual':>8s}  {'Cumulative':>12s}")
    print("-" * 30)
    for year, n in annual.items():
        cum = cumulative[year]
        print(f"{year:>6d}  {n:>8d}  {cum:>12d}")

    # period means
    def period_mean(start, end):
        s = annual[(annual.index >= start) & (annual.index <= end)]
        return s.sum() / (end - start + 1), s.sum()

    print("\nPeriod averages:")
    for start, end, label in [(1995, 2014, "1995-2014"),
                              (2015, 2019, "2015-2019"),
                              (2020, 2022, "2020-2022"),
                              (2023, 2025, "2023-2025")]:
        m, tot = period_mean(start, end)
        print(f"  {label}: mean {m:.1f}/year (total {tot})")

    # milestone years
    print("\nCumulative milestones:")
    for threshold in [100, 500, 1000]:
        crossed = cumulative[cumulative >= threshold]
        if len(crossed):
            year = crossed.index[0]
            print(f"  Cumulative reached {threshold} in {year} ({100*threshold/total:.1f}% of all-time total)")
    print(f"  Single-year maximum: {annual.max()} in {annual.idxmax()} ({100*annual.max()/total:.1f}% of all-time total)")

if __name__ == "__main__":
    main()
