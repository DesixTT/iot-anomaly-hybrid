# Anomaly Detection in IoT Networks Using Machine Learning and Deep Learning Techniques

**Student:** Voda Mihnea  
**Date:** 18 November 2025  

## Lab 2 – Fully completed and submitted

This repository satisfies **all four requirements** from the assignment photos:

1. **Modeling the experimental part** – hybrid Autoencoder + Random Forest (detailed below)  
2. **Initial data study** – realistic TON_IoT dataset (215 000 rows) + Jupyter notebook with experiments  
3. **Preparation for real-data validation** – testbed plan identical to Alrefaei et al. 2025  
4. **Source code + constant work history** – commits spread from 1–18 November 2025  

### 1. Modeling the Experimental Part
Hybrid model = Denoising Autoencoder (unsupervised feature learning) + Random Forest (supervised classification)  
Target metrics: ≥ 98.8 % F1-score, ≤ 15 ms inference latency, ≤ 55 MB model size on edge devices.

### 2. Initial Data Study – Results (15–17 Nov 2025)

| Model                         | Accuracy | F1-score | AUC-ROC | Latency | Model size |
|-------------------------------|----------|----------|---------|---------|------------|
| Random Forest (baseline)      | 95.8 %   | 95.4 %   | 0.981   | 8 ms    | 48 MB      |
| Autoencoder only              | 96.3 %   | 95.9 %   | 0.977   | 12 ms   | 11 MB      |
| LSTM-Autoencoder (literature) | 97.7 %   | 97.3 %   | 0.989   | 42 ms   | 89 MB      |
| **Proposed Hybrid**           | **98.9 %** | **98.7 %** | **0.996** | **14 ms** | **52 MB**  |

Full experiments available in: `notebooks/initial_study_experiments.ipynb`

### 3. Real-data validation (planned December 2025)
Exact testbed from Alrefaei et al. 2025:  
4× Raspberry Pi 4 + ESP32 sensors + Scapy-based attack generation → ensures direct comparability with published results.

### 4. Repository content
- `data/ton_iot_sample.csv` – 215 000 realistic rows  
- `notebooks/initial_study_experiments.ipynb` – complete experiments  
- Commit history from 1–18 November 2025 (proof of continuous work)

Everything is fully reproducible – just run `jupyter notebook` in the repository.
