# OIBSIP Python Internship Tasks

This workspace contains the completed Python internship projects.

## Official Submission

Submit projects through the official submission form only. The form should include:

- Your public GitHub repository link
- A live demo link only when applicable
- The project name using the required naming format

These are local Python command-line projects, so a live demo is not applicable unless you deploy them separately. Do not invent a live URL; provide the GitHub link and the documented run commands instead.

## Task 2: BMI Calculator

Location: `Python-Task2-BMICalculator/bmi_calculator.py`

Features:

- Validates positive numeric weight and height
- Calculates BMI and category
- Repeats until the user chooses to stop

Run:

```powershell
python "Python-Task2-BMICalculator\bmi_calculator.py"
```

## Task 3: Password Generator

Location: `Python-Task3-PasswordGenerator/password_generator.py`

Features:

- Uses Python's secure `secrets` module
- Configurable length and character types
- Includes selected character categories
- Avoids ambiguous characters
- Reports password strength

Run:

```powershell
python "Python-Task3-PasswordGenerator\password_generator.py"
```

## Voice Assistant

Location: `Python-Task1-VoiceAssistant/voice_assistant.py`

Features:

- Voice input with typed fallback
- Greetings, time, date, search, weather, reminders, and knowledge answers
- YouTube song lookup
- Graceful microphone and keyboard-interrupt handling

Run from the `OIBSIP` directory:

```powershell
python "Python-Task1-VoiceAssistant\voice_assistant.py"
```

Install voice-assistant dependencies:

```powershell
pip install SpeechRecognition pyttsx3 PyAudio pywhatkit requests
```

## Submission Checklist

- Run each program successfully.
- Include the source files and README files.
- Do not include `__pycache__` folders or generated `.pyc` files.
- Demonstrate normal input and invalid-input handling.
- Keep generated passwords private and store them in a password manager.
- Keep the submitted folders named `Python-Task1-VoiceAssistant`, `Python-Task2-BMICalculator`, and `Python-Task3-PasswordGenerator`.
- Complete [SUBMISSION_CHECKLIST.md](SUBMISSION_CHECKLIST.md) before using the official form.
