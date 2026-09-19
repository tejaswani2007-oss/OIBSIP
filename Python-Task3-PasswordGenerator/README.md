# Password Generator

A secure command-line password generator for the OIBSIP Python task.

## Features

- Uses Python's `secrets` module for secure random values
- Requires a minimum password length of 8 characters
- Optional uppercase letters, lowercase letters, numbers, and symbols
- Requires at least two selected character types
- Ensures every selected character type appears at least once
- Avoids ambiguous characters such as `I`, `l`, `1`, `O`, and `0`
- Displays a simple strength estimate
- Allows another password to be generated without restarting

## Run

From the `OIBSIP` folder:

```powershell
python "Python-Task3-PasswordGenerator\password_generator.py"
```

Enter a length and answer the character-type prompts. Press Enter to accept the default `yes` answer.

Generated passwords are shown only in the terminal. Store them in a trusted password manager and never share them in chat or source code.
