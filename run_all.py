#!/usr/bin/env python3
"""
run_all.py
-----------
One-command setup: generates dataset, trains all models, runs clustering,
then launches the Streamlit dashboard.

Usage:
    python run_all.py                  # Use synthetic data
    python run_all.py --real-data      # Try fetching real TLEs first
    python run_all.py --skip-train     # Skip training, just launch dashboard
"""

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent


def run(cmd, desc):
    print(f"\n{'='*60}")
    print(f"  {desc}")
    print(f"{'='*60}")
    result = subprocess.run(cmd, shell=True, cwd=ROOT)
    if result.returncode != 0:
        print(f"[!] Step failed: {desc}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--real-data',   action='store_true')
    parser.add_argument('--skip-train',  action='store_true')
    parser.add_argument('--skip-umap',   action='store_true')
    args = parser.parse_args()

    if not args.skip_train:
        if args.real_data:
            run(f"{sys.executable} data/fetch_real_tles.py",
                "Fetching real TLE data from Celestrak")
            data_file = "data/real_tles_dataset.csv"
        else:
            run(f"{sys.executable} data/generate_dataset.py",
                "Generating synthetic orbital debris dataset")
            data_file = "data/orbital_forensics_dataset.csv"

        run(f"{sys.executable} models/train_models.py --data {data_file}",
            "Training all ML models (RF, GBT, SVM, MLP, KNN, XGB)")

        if not args.skip_umap:
            run(f"{sys.executable} utils/clustering.py",
                "Running UMAP + HDBSCAN clustering")

    print(f"\n{'='*60}")
    print("  Launching Streamlit Dashboard")
    print(f"{'='*60}")
    subprocess.run(
        f"streamlit run dashboard/dashboard.py "
        f"--server.port 8501 "
        f"--theme.backgroundColor '#0d1117' "
        f"--theme.primaryColor '#58a6ff'",
        shell=True, cwd=ROOT
    )


if __name__ == "__main__":
    main()
