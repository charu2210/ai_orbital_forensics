# AI Orbital Forensics

Classifies space debris fragments back to their parent satellite using real orbital data from CelesTrak.

## What it does

Given the Keplerian orbital elements of an unidentified debris fragment, the model predicts which historical breakup event it originated from — across five major LEO debris-generating events:

| ID | Event |
|----|-------|
| 0 | Cosmos-1408 — Russian ASAT test (2021) |
| 1 | Fengyun-1C — Chinese ASAT test (2007) |
| 2 | Iridium-33 — Iridium/Cosmos collision (2009) |
| 3 | Cosmos-2251 — Iridium/Cosmos collision (2009) |
| 4 | Breeze-M — Proton-M explosion (2012) |

## How it works

1. **Data** — Live TLE (Two-Line Element) sets fetched directly from [CelesTrak](https://celestrak.org). No synthetic data.
2. **Features** — Six Keplerian elements extracted from each TLE: semi-major axis, eccentricity, inclination, RAAN, argument of perigee, mean motion.
3. **Models** — Random Forest, SVM, KNN, and XGBoost individually tuned, then combined into a soft-voting ensemble.
4. **Output** — Per-class confidence scores for any input fragment, plus a real-time simulation over held-out test fragments.

## Setup

```bash
pip install numpy pandas scikit-learn xgboost matplotlib seaborn requests
```

Or in Colab, uncomment the `!pip install xgboost` line at the top of the notebook.

## Usage

Run all cells in order. The notebook will:
- Fetch live debris TLEs from CelesTrak
- Train and tune all models
- Print classification report + confusion matrix
- Simulate attribution on 5 random test fragments
- Attribute a custom unknown debris object (edit Section 12 to use your own orbital elements)

To attribute your own debris fragment, edit the `unknown` dict in Section 12:

```python
unknown = pd.DataFrame([{
    "a": R_EARTH + <altitude_km>,
    "e": <eccentricity>,
    "i": <inclination_deg>,
    "raan": <RAAN_deg>,
    "argp": <arg_perigee_deg>,
    "n": np.sqrt(MU / (R_EARTH + <altitude_km>)**3)
}])
```

## Data source

All orbital data is fetched live from [CelesTrak](https://celestrak.org) via their GP elements API. If a fetch fails, download the TLE file manually from CelesTrak and load it with `parse_tle(open("file.tle").read())`.

## Tech stack

Python · Scikit-learn · XGBoost · Pandas · Matplotlib · Seaborn · CelesTrak API
