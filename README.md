# Voice Typer

<!-- Write 2-3 sentences in your own words: what does this tool do, and why did you build it? -->

## Features

- [x] Record audio from the microphone
- [x] Transcribe audio to text (English, French, Arabic)
- [x] Dictation mode: hold a key, speak, text appears at the cursor
- [x] Meeting mode: record a meeting and save a written transcript

## Privacy

All speech recognition runs locally on your computer. No audio or text is sent to the internet.

## Requirements

- Windows 10/11
- Python 3.12

## Setup

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

Activate the environment first: `.venv\Scripts\activate`

| Command | What it does |
|---|---|
| `python record.py` | Records 5 seconds to `recordings/test.wav` |
| `python transcribe.py` | Transcribes `recordings/test.wav` |
| `python transcribe.py file.wav fr` | Transcribes a file in a given language (`en`, `fr`, `ar`) |
| `python dictate.py` | Dictation: hold **F9**, speak, release, the text is pasted at the cursor |
| `python meeting.py` | Records until Enter, saves a timestamped transcript in `transcripts/` |

Settings (hotkey, language, model size) are at the top of each file.

The first run downloads the speech model (internet needed once). After that everything works offline.

## What I learned

<!-- Optional but great for recruiters: a few lines on what you learned building this. -->

## Acknowledgements

- [faster-whisper](https://github.com/SYSTRAN/faster-whisper) for speech recognition
- Inspired by [Handy](https://github.com/cjpais/Handy) and [OpenWhispr](https://github.com/OpenWhispr/openwhispr)

## License

MIT
