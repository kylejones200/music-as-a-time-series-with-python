# Description: Short example for Music as a Time Series with Python.

import logging

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import correlate


def main():
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )

    # Load an example trumpet audio file
    y, sr = librosa.load(librosa.example("trumpet"), sr=None)  # Use default sample rate
    # Create a time vector
    time = np.linspace(0, len(y) / sr, num=len(y))
    # Plot the waveform
    plt.figure(figsize=(10, 4))
    plt.plot(time, y, label="Waveform")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.title("Raw Audio Waveform")
    plt.legend()
    plt.savefig("waveform.png")
    plt.show()
    # Compute the spectrogram
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
    # Plot the spectrogram
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(D, sr=sr, x_axis="time", y_axis="log")
    plt.colorbar(format="%+2.0f dB")
    plt.title("Spectrogram")
    plt.savefig("spectrogram.png")
    plt.show()
    # Compute autocorrelation
    corr = correlate(y, y, mode="full")
    lags = np.arange(-len(y) + 1, len(y))
    # Plot the autocorrelation function
    plt.figure(figsize=(10, 4))
    plt.plot(lags / sr, corr)
    plt.xlabel("Lag (seconds)")
    plt.ylabel("Autocorrelation")
    plt.title("Autocorrelation of Audio Signal")
    plt.savefig("autocorrelation.png")
    plt.show()
    # Load an example trumpet audio file
    y, sr = librosa.load(librosa.example("trumpet"), sr=None)  # Use default sample rate
    # Detect tempo
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    # Convert beat frames to time
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    # Print detected tempo (extract scalar properly)
    logger.info(f"Estimated Tempo: {tempo.item():.2f} BPM")
    # Plot beats over waveform
    plt.figure(figsize=(10, 4))
    librosa.display.waveshow(y, sr=sr, alpha=0.5)
    plt.vlines(beat_times, -1, 1, color="r", alpha=0.75, linestyle="--", label="Beats")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.title("Detected Beats in Music")
    plt.legend()
    plt.savefig("beat_detection.png")
    plt.show()
    # Estimated Tempo: 184.57 BPM


if __name__ == "__main__":
    main()
