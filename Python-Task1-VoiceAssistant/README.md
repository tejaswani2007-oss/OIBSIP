# Voice Assistant

A beginner-friendly Python voice assistant for the OIBSIP task. It supports microphone input when the optional speech packages are installed and automatically falls back to typed commands.

## Features

- Responds to greetings
- Tells the current time and date
- Searches Google in the default browser
- Opens the first YouTube result for a requested song
- Sets timed reminders while the program is running
- Retrieves weather updates and general-knowledge summaries
- Provides a help command
- Handles unavailable microphones, speech errors, `Ctrl+C`, and closed input cleanly

## Setup

From the `Python-Task2-BMICalculator` folder, install the optional voice dependencies:

```powershell
pip install -r "voice assistant\requirements.txt"
```

`PyAudio` may require an operating-system-specific wheel. The assistant still works with typed input if microphone dependencies cannot be installed.

## Run

```powershell
python "voice assistant\voice_assistant.py"
```

Try these commands:

```text
hello
time
date
search Python tutorials
weather in London
remind me in 1 minute to stretch
who is Ada Lovelace
help
exit
```

Speech recognition uses Google's online recognition service through the `SpeechRecognition` package. Do not use this example for sensitive information without reviewing the privacy implications of that service.