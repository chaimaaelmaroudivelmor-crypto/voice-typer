"""
STEP 3 - Turn a recording into text

Goal:
    Load a speech model once, then transcribe a .wav file into text.

Write two functions:
    load_model()                         -> returns a model
    transcribe(model, audio, language)   -> returns (text, detected_language)

Hints:
    - Read the faster-whisper README "Usage" section.
    - Create the model with WhisperModel("small", device="cpu", compute_type="int8").
    - model.transcribe() returns two things: segments and info.
      Join the text of all segments into one string.
    - language can be None (auto-detect), "en", "fr" or "ar".
    - The first run downloads the model (needs internet once).

Test:
    Record 3 test files with record.py: one in English, one in French, one in Arabic.
    Transcribe each one. Note which language works best. Try Darija too.
    Write what you found in the README under "What I learned".
"""


def load_model():
    # TODO
    pass


def transcribe(model, audio, language=None):
    # TODO
    pass


if __name__ == "__main__":
    # TODO: load the model, transcribe recordings/test.wav, print the text
    pass
