"""Compute counts and percentages of FDA AI/ML authorizations by lead review panel.

Reproduces the Results > Specialty distribution section of:
Golshani P, Joseph M. Three Decades of FDA Authorizations of AI/ML-Enabled
Medical Devices (1995-2025). Cureus 2026.
"""
import pandas as pd
from pathlib import Path

CSV = Path(__file__).parent.parent / "data" / "fda_aiml_devices_1995_2025.csv"

def main():
    df = pd.read_csv(CSV)
    total = len(df)
    print(f"Total authorizations: {total}\n")

    counts = df["Panel (Lead)"].value_counts()
    print("Authorizations by FDA lead review panel:")
    print("-" * 60)
    for panel, n in counts.items():
        pct = 100 * n / total
        print(f"  {panel:30s}  n = {n:5d}  ({pct:5.1f}%)")

    top3 = counts.head(3).sum()
    top5 = counts.head(5).sum()
    print(f"\nTop 3 panels combined: {top3} ({100*top3/total:.1f}%)")
    print(f"Top 5 panels combined: {top5} ({100*top5/total:.1f}%)")

    print("\nPanels with <= 10 authorizations:")
    for panel, n in counts.items():
        if n <= 10:
            print(f"  {panel:30s}  n = {n:3d}  ({100*n/total:.1f}%)")

if __name__ == "__main__":
    main()
