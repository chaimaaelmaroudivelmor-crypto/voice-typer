"""
Meeting mode: record until you press Enter, then save a transcript
with timestamps to transcripts/<date>_<time>.txt

Usage:
    python meeting.py

Note: records the microphone only. Ask participants before recording.
"""

import os
from datetime import datetime

import numpy as np
import sounddevice as sd

from record import SAMPLE_RATE
from transcribe import load_model, transcribe_segments

LANGUAGE = None  # None = auto-detect, or "en", "fr", "ar"


def format_time(seconds):
    seconds = int(seconds)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def record_until_enter():
    chunks = []

    def callback(indata, frames, time_info, status):
        chunks.append(indata.copy())

    with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype="float32", callback=callback):
        input("Recording... press Enter to stop.\n")

    if not chunks:
        return None
    return np.concatenate(chunks).flatten()


def save_transcript(segments, language, started_at):
    os.makedirs("transcripts", exist_ok=True)
    filename = started_at.strftime("%Y-%m-%d_%H-%M") + ".txt"
    path = os.path.join("transcripts", filename)

    with open(path, "w", encoding="utf-8") as file:
        file.write(f"Meeting - {started_at.strftime('%d/%m/%Y %H:%M')} - language: {language}\n\n")
        for start, end, text in segments:
            file.write(f"[{format_time(start)}] {text}\n")

    return path


def main():
    model = load_model()
    input("Press Enter to start recording.")

    started_at = datetime.now()
    audio = record_until_enter()
    if audio is None:
        print("Nothing was recorded.")
        return

    minutes = len(audio) / SAMPLE_RATE / 60
    print(f"Transcribing {minutes:.1f} minutes of audio, this can take a while...")
    segments, language = transcribe_segments(model, audio, LANGUAGE)

    path = save_transcript(segments, language, started_at)
    print(f"Transcript saved to {path}")


if __name__ == "__main__":
    main()
