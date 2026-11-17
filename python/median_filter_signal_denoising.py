"""Reproducible 1D signal-denoising experiment using a median filter."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import medfilt


def composite_signal(time: np.ndarray) -> np.ndarray:
    """Create a clean signal containing 5 Hz and 20 Hz components."""
    return 0.7 * np.sin(2 * np.pi * 5 * time) + 1.2 * np.sin(2 * np.pi * 20 * time)


def save_plot(path: Path, title: str, time: np.ndarray, series: list[tuple[np.ndarray, str, str]]) -> None:
    """Save one labelled experiment plot."""
    fig, axis = plt.subplots(figsize=(12, 5))
    for values, label, style in series:
        axis.plot(time, values, style, label=label, linewidth=1.5)
    axis.set(title=title, xlabel="Time [s]", ylabel="Amplitude")
    axis.grid(True, alpha=0.3)
    axis.legend()
    fig.tight_layout()
    fig.savefig(path, dpi=180)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description="Median-filter signal-denoising experiment")
    parser.add_argument("--save-dir", type=Path, default=Path("outputs/signal"))
    parser.add_argument("--window-size", type=int, default=11)
    parser.add_argument("--noise-std", type=float, default=0.3)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    if args.window_size < 3 or args.window_size % 2 == 0:
        raise ValueError("--window-size must be an odd integer of at least 3.")

    args.save_dir.mkdir(parents=True, exist_ok=True)
    sampling_rate = 1000
    time = np.arange(sampling_rate) / sampling_rate
    clean = composite_signal(time)
    noise = np.random.default_rng(args.seed).normal(0, args.noise_std, clean.shape)
    noisy = clean + noise
    denoised = medfilt(noisy, kernel_size=args.window_size)
    mse = np.mean((clean - denoised) ** 2)

    save_plot(args.save_dir / "01-clean-and-noise.png", "Clean Signal and Noise", time, [(clean, "Clean", "g-"), (noise, "Noise", "k-")])
    save_plot(args.save_dir / "02-noisy-signal.png", "Noisy Signal", time, [(noisy, "Noisy", "b-")])
    save_plot(args.save_dir / "03-denoised-signal.png", "Median-Filtered Signal", time, [(denoised, "Denoised", "r-")])
    save_plot(args.save_dir / "04-comparison.png", "Clean vs. Denoised", time, [(clean, "Clean", "g-"), (denoised, "Denoised", "r--")])
    print(f"Window size: {args.window_size}")
    print(f"MSE (clean vs. denoised): {mse:.6f}")


if __name__ == "__main__":
    main()
