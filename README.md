# Signal Denoising with Median Filtering

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](python/median_filter_signal_denoising.py)
[![DSP](https://img.shields.io/badge/Domain-Digital%20Signal%20Processing-6f42c1)](#method)

> A reproducible Python experiment that reduces Gaussian noise in a composite time-domain signal using median filtering.

![Clean signal compared with filtered result](docs/assets/signal-denoising-comparison.png)

## What it demonstrates

- Generates a composite 5 Hz and 20 Hz sinusoidal signal.
- Adds deterministic Gaussian noise for reproducible experiments.
- Applies an odd-length median-filter window to reduce noise.
- Produces four plots and evaluates the result with Mean Squared Error (MSE).

## Method

```text
Clean composite signal -> Gaussian noise -> Median filter -> MSE evaluation
```

The default experiment uses a 1 kHz sampling rate, seed `42`, and an 11-sample window.

## Run

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
python python/median_filter_signal_denoising.py --save-dir outputs
```

The validated default run reports an MSE of approximately `0.021386` and writes plots to `outputs/`.

## Context

Academic Digital Signal Processing laboratory project by Yahya Al Afifi, Islamic University of Gaza.

