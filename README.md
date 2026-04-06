# 🛰️ AI-Based Orbital Forensics

> Identifying the Source of Space Debris Using Machine Learning  
> Charu Malik (2430010140) · Radhika Rongare (2430010147)

---

## Project Structure

```
orbital_forensics/
│
├── data/
│   ├── generate_dataset.py     ← Synthetic physics-based debris dataset
│   └── fetch_real_tles.py      ← Real data from Celestrak (for paper)
│
├── models/
│   └── train_models.py         ← Multi-model training + evaluation
│
├── utils/
│   ├── clustering.py           ← UMAP + HDBSCAN (novel contribution)
│   └── predict.py              ← Inference API for single fragments
│
├── dashboard/
│   └── dashboard.py            ← Full Streamlit dashboard
│
├── run_all.py                  ← One-command setup
└── requirements.txt
```

---

## Quick Start

```bash
pip install -r requirements.txt
python run_all.py
```

Open `http://localhost:8501` in your browser.

---

## Step by Step

```bash
# 1. Generate dataset
python data/generate_dataset.py

# 2. (Optional) Fetch real TLE data from Celestrak
python data/fetch_real_tles.py

# 3. Train all models
python models/train_models.py --data data/orbital_forensics_dataset.csv

# 4. Run UMAP clustering (unsupervised track)
python utils/clustering.py

# 5. Launch dashboard
streamlit run dashboard/dashboard.py
```

---

## What's Novel (for the paper)

1. **Richer features**: 14 orbital features vs. the standard 3 (inclination, e, a)
   - Added: B* drag, apogee/perigee altitude, angular momentum, Kozai mean motion

2. **Multi-model benchmark**: RF, XGBoost, SVM, MLP, KNN — not just one model

3. **Unsupervised track**: UMAP + HDBSCAN to cluster debris of *unknown* origin.
   This is the actual real-world problem and the key novel contribution.

4. **Real data pathway**: `fetch_real_tles.py` pulls real TLE catalogs from
   Celestrak for Fengyun-1C, Kosmos-2251, Iridium-33 debris.

---

## Dashboard Tabs

| Tab | Contents |
|-----|----------|
| 🌍 Overview | Dataset distribution, orbital element violin plots |
| 🏆 Model Arena | Multi-model accuracy table, radar chart, per-class metrics |
| 🗺️ Orbital Map | UMAP scatter (true labels vs discovered clusters) |
| 🔍 Predict | Live inference — enter orbital elements, get attribution |
| 📊 Feature Lab | Feature importance, correlation heatmap, 3D scatter |
| 🎯 Confusion Matrix | Regular + normalized CM for each model |

---

## To Make It Publishable

- [ ] Run `fetch_real_tles.py` and use real data (massive credibility boost)
- [ ] Add time-evolution features (how elements drift over months)
- [ ] Compare ARI/NMI of unsupervised clustering vs. prior work
- [ ] Add ablation study: remove features one by one, show accuracy drop
- [ ] Target: IEEE Access, Acta Astronautica, Advances in Space Research
