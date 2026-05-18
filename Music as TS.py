"""Generated from Jupyter notebook: Music as TS

Magics and shell lines are commented out. Run with a normal Python interpreter."""

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import correlate


def load_an_example_trumpet_audio_file() -> None:
    y, sr = librosa.load(librosa.example("trumpet"), sr=None)
    time = np.linspace(0, len(y) / sr, num=len(y))
    plt.figure(figsize=(10, 4))
    plt.plot(time, y, label="Waveform")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.title("Raw Audio Waveform")
    plt.legend()
    plt.grid()
    plt.savefig("waveform.png")
    plt.show()
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
    plt.figure(figsize=(10, 4))
    librosa.display.specshow(D, sr=sr, x_axis="time", y_axis="log")
    plt.colorbar(format="%+2.0f dB")
    plt.title("Spectrogram")
    plt.savefig("spectrogram.png")
    plt.show()


def compute_autocorrelation() -> None:
    corr = correlate(y, y, mode="full")
    lags = np.arange(-len(y) + 1, len(y))
    plt.figure(figsize=(10, 4))
    plt.plot(lags / sr, corr)
    plt.xlabel("Lag (seconds)")
    plt.ylabel("Autocorrelation")
    plt.title("Autocorrelation of Audio Signal")
    plt.savefig("autocorrelation.png")
    plt.show()


def load_an_example_trumpet_audio_file_2() -> None:
    y, sr = librosa.load(librosa.example("trumpet"), sr=None)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    print(f"Estimated Tempo: {tempo.item():.2f} BPM")
    plt.figure(figsize=(10, 4))
    librosa.display.waveshow(y, sr=sr, alpha=0.5)
    plt.vlines(beat_times, -1, 1, color="r", alpha=0.75, linestyle="--", label="Beats")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")
    plt.title("Detected Beats in Music")
    plt.legend()
    plt.savefig("beat_detection.png")
    plt.show()


def main() -> None:
    load_an_example_trumpet_audio_file()
    compute_autocorrelation()
    load_an_example_trumpet_audio_file_2()


if __name__ == "__main__":
    main()
