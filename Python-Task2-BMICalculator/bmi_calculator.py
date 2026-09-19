"""Interactive BMI calculator."""


def read_positive_number(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if value <= 0:
            print("Please enter a valid positive number.")
            continue
        return value

def calculate_bmi(weight: float, height: float) -> tuple[float, str]:
    bmi = round(weight / (height**2), 2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category


def main() -> None:
    while True:
        weight = read_positive_number("Enter your weight in kg: ")
        height = read_positive_number("Enter your height in meters: ")
        bmi, category = calculate_bmi(weight, height)

        print("\n------------------------------")
        print("        BMI CALCULATOR")
        print("------------------------------")
        print("Your BMI:", bmi)
        print("Category:", category)
        print("------------------------------")

        again = input("Do you want to calculate again? (yes/no): ").strip().lower()
        if again not in {"yes", "y"}:
            print("Thank you for using the BMI calculator.")
            break


if __name__ == "__main__":
    main()