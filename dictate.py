"""
Dictation mode: hold the hotkey, speak, release.
The text is pasted where the cursor is (email, Excel, Teams...).

Usage:
    python dictate.py
"""

import time

import numpy as np
import sounddevice as sd
import keyboard
import pyperclip

from record import SAMPLE_RATE
from transcribe import load_model, transcribe

HOTKEY = "f9"     # key to hold while speaking
LANGUAGE = None   # None = auto-detect, or "en", "fr", "ar"


def beep(frequency):
    try:
        import winsound
        winsound.Beep(frequency, 80)
    except Exception:
        pass


def record_while_held():
    chunks = []

    def callback(indata, frames, time_info, status):
        chunks.append(indata.copy())

    with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype="float32", callback=callback):
        while keyboard.is_pressed(HOTKEY):
            time.sleep(0.02)

    if not chunks:
        return None
    return np.concatenate(chunks).flatten()


def paste(text):
    try:
        previous = pyperclip.paste()
    except Exception:
        previous = None

    pyperclip.copy(text)
    time.sleep(0.05)
    keyboard.send("ctrl+v")
    time.sleep(0.2)

    if previous is not None:
        pyperclip.copy(previous)


def main():
    model = load_model()
    print(f"Ready. Hold {HOTKEY.upper()} and speak, release to insert text. Close the window to stop.")

    while True:
        keyboard.wait(HOTKEY)
        beep(880)
        audio = record_while_held()
        beep(440)

        if audio is None or len(audio) < SAMPLE_RATE * 0.3:
            continue

        try:
            text, detected = transcribe(model, audio, LANGUAGE)
        except Exception as error:
            print("Error:", error)
            continue

        if text:
            print(f"[{detected}] {text}")
            paste(text + " ")


if __name__ == "__main__":
    main()
