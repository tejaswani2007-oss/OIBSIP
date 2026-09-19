# BMI Calculator

A command-line BMI calculator for the OIBSIP Python Programming internship, Task 2.

## Requirements Covered

- Prompts for weight in kilograms and height in meters
- Calculates BMI using `weight / (height ** 2)`
- Displays BMI rounded to two decimal places
- Classifies results as Underweight, Normal weight, Overweight, or Obese
- Rejects non-numeric, zero, and negative values with helpful messages
- Allows repeated calculations until the user chooses to stop

## Run

From the `OIBSIP` folder:

```powershell
python "Python-Task2-BMICalculator\bmi_calculator.py"
```

## Demonstration Inputs

Normal range example:

```text
Weight: 70
Height: 1.75
```

Also demonstrate an invalid value such as `abc` or `-5` and show the validation message.
