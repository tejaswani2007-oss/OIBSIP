# OIBSIP Submission Checklist

## Before Submission

- [ ] Use clear task-based project names such as `Python-Task1-VoiceAssistant`.
- [ ] Keep one README file in every submitted project folder.
- [ ] Add the GitHub repository link to the official submission form.
- [ ] Add a live demo link only if the project has one.
- [ ] Test each project from a clean terminal.
- [ ] Remove `__pycache__`, `.pyc` files, passwords, API keys, and personal data.
- [ ] Submit through the official submission form only.

## Project Naming Template

Use these name-free project folders:

```text
Python-Task1-VoiceAssistant
Python-Task2-BMICalculator
Python-Task3-PasswordGenerator
```

Use the exact task numbers assigned by your internship instructions. Voice Assistant is currently organized as Task 1.

## Submission Details

Fill these values into the official form:

```text
Name: YOUR FULL NAME
GitHub repository: https://github.com/YOUR_USERNAME/YOUR_REPOSITORY
Live demo: Not applicable (local Python CLI project)
```

The live demo is normally not applicable because these are local command-line Python programs. Do not invent a live URL. Use the GitHub repository link and describe the run commands in each README.

## Run Commands

```powershell
python "Python-Task2-BMICalculator\bmi_calculator.py"
python "Python-Task3-PasswordGenerator\password_generator.py"
python "Python-Task1-VoiceAssistant\voice_assistant.py"
```

## GitHub Upload

From the repository root, after renaming the folders:

```powershell
git init
git add .
git commit -m "Complete OIBSIP Python internship tasks"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
git push -u origin main
```

Create the GitHub repository first, keep it public if the internship requires public access, and replace the placeholder remote URL with your real repository URL.
