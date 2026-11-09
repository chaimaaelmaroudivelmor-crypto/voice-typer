"""
Turn audio into text with faster-whisper (runs offline on the CPU).

Usage:
    python transcribe.py                      -> transcribes recordings/test.wav
    python transcribe.py path/to/file.wav fr  -> force a language (en, fr, ar)
"""

import sys

from faster_whisper import WhisperModel

MODEL_SIZE = "small"  # "base" = faster, "small" = balanced, "medium" = more accurate


def load_model():
    print(f"Loading model '{MODEL_SIZE}'...")
    return WhisperModel(MODEL_SIZE, device="cpu", compute_type="int8")


def transcribe(model, audio, language=None):
    """audio can be a file path or a numpy array (16 kHz, mono, float32)."""
    segments, info = model.transcribe(audio, language=language, vad_filter=True)
    text = " ".join(segment.text.strip() for segment in segments).strip()
    return text, info.language


def transcribe_segments(model, audio, language=None):
    """Same as transcribe(), but returns a list of (start, end, text) for timestamps."""
    segments, info = model.transcribe(audio, language=language, vad_filter=True)
    return [(s.start, s.end, s.text.strip()) for s in segments], info.language


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "recordings/test.wav"
    language = sys.argv[2] if len(sys.argv) > 2 else None

    model = load_model()
    text, detected = transcribe(model, path, language)
    print(f"[{detected}] {text}")
