"""
STEP 5 - Meeting mode

Goal:
    Start recording, stop when you press Enter, then save a transcript
    with timestamps to transcripts/<date-time>.txt

Plan:
    1. Start recording (same InputStream idea as dictate.py).
    2. Stop when the user presses Enter (look up input()).
    3. Transcribe. Each segment has .start, .end and .text
    4. Write lines like:  [00:01:23] text...  into a .txt file.

Hints:
    - Use the datetime module to name the file with today's date and time.
    - Convert seconds to hh:mm:ss yourself (good practice with // and %).

Important:
    - Ask people's permission before recording a meeting.
    - Never upload recordings or transcripts to GitHub
      (the .gitignore already blocks the folders).

Bonus (advanced, later):
    - This version records your microphone only. Recording the other
      people's voices from Teams needs "loopback" recording of the
      computer's sound. Research the "soundcard" library when you are ready.
"""


def main():
    # TODO
    pass


if __name__ == "__main__":
    main()
