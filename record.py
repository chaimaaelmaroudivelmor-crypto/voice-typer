"""
Record audio from the microphone and save it as a .wav file.

Usage:
    python record.py
"""

import os

import sounddevice as sd
import soundfile as sf

SAMPLE_RATE = 16000


def record(seconds):
    print(f"Recording for {seconds} seconds...")
    audio = sd.rec(int(seconds * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype="float32")
    sd.wait()
    print("Done.")
    return audio


def save(audio, filename):
    os.makedirs("recordings", exist_ok=True)
    path = os.path.join("recordings", filename)
    sf.write(path, audio, SAMPLE_RATE)
    print(f"Saved to {path}")


if __name__ == "__main__":
    audio = record(5)
    save(audio, "test.wav")
