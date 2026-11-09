"""
STEP 4 - Dictation mode

Goal:
    While you HOLD a key (for example F9), record. When you RELEASE it,
    transcribe and paste the text where the cursor is (email, Excel, anywhere).

Plan (write each part, test it, then go to the next):
    1. Wait until the hotkey is pressed.
    2. Record while the hotkey is held down.
    3. Transcribe the audio (reuse your function from transcribe.py).
    4. Paste the text at the cursor.

Hints:
    - keyboard.wait() and keyboard.is_pressed() from the keyboard library.
    - To record for an unknown length, sounddevice.rec() is not enough.
      Look up sounddevice.InputStream with a callback that collects chunks,
      then join the chunks with numpy.concatenate().
    - To paste: copy the text with pyperclip.copy(), then send ctrl+v
      with keyboard.send().
    - Load the model ONCE at the start, not every time you press the key.

Test:
    Run python dictate.py, open Notepad, hold F9, speak, release.
"""

HOTKEY = "f9"


def main():
    # TODO
    pass


if __name__ == "__main__":
    main()
