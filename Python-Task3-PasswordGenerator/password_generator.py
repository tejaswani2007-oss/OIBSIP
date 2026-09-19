"""Secure command-line password generator."""

import secrets
import string


AMBIGUOUS_CHARACTERS = "Il1O0"


def build_alphabet(
    include_uppercase: bool,
    include_lowercase: bool,
    include_digits: bool,
    include_symbols: bool,
) -> str:
    """Return the selected character alphabet without ambiguous characters."""
    groups = []
    if include_uppercase:
        groups.append(string.ascii_uppercase)
    if include_lowercase:
        groups.append(string.ascii_lowercase)
    if include_digits:
        groups.append(string.digits)
    if include_symbols:
        groups.append("!@#$%^&*()-_=+[]{}?/")

    alphabet = "".join(groups)
    return "".join(character for character in alphabet if character not in AMBIGUOUS_CHARACTERS)


def generate_password(
    length: int,
    include_uppercase: bool = True,
    include_lowercase: bool = True,
    include_digits: bool = True,
    include_symbols: bool = True,
) -> str:
    """Generate a cryptographically secure password from the selected categories."""
    selected_groups = []
    if include_uppercase:
        selected_groups.append(string.ascii_uppercase)
    if include_lowercase:
        selected_groups.append(string.ascii_lowercase)
    if include_digits:
        selected_groups.append(string.digits)
    if include_symbols:
        selected_groups.append("!@#$%^&*()-_=+[]{}?/")

    if length < 8:
        raise ValueError("Password length must be at least 8.")
    if len(selected_groups) < 2:
        raise ValueError("Select at least two character types.")
    if length < len(selected_groups):
        raise ValueError("Length must cover every selected character type.")

    filtered_groups = [
        "".join(character for character in group if character not in AMBIGUOUS_CHARACTERS)
        for group in selected_groups
    ]
    password_characters = [secrets.choice(group) for group in filtered_groups]
    alphabet = "".join(filtered_groups)
    password_characters.extend(
        secrets.choice(alphabet) for _ in range(length - len(password_characters))
    )
    secrets.SystemRandom().shuffle(password_characters)
    return "".join(password_characters)


def password_strength(length: int, character_types: int) -> str:
    """Provide a simple user-facing strength label."""
    if length >= 16 and character_types >= 4:
        return "Very strong"
    if length >= 12 and character_types >= 3:
        return "Strong"
    if length >= 8 and character_types >= 2:
        return "Moderate"
    return "Weak"


def ask_yes_no(prompt: str, default: bool = True) -> bool:
    answer = input(prompt).strip().lower()
    if not answer:
        return default
    return answer in {"y", "yes"}


def main() -> None:
    print("\nSECURE PASSWORD GENERATOR")
    print("Use a password manager to store generated passwords.\n")

    while True:
        try:
            length = int(input("Password length (default 16): ").strip() or "16")
            use_uppercase = ask_yes_no("Include uppercase letters? (Y/n): ")
            use_lowercase = ask_yes_no("Include lowercase letters? (Y/n): ")
            use_digits = ask_yes_no("Include numbers? (Y/n): ")
            use_symbols = ask_yes_no("Include symbols? (Y/n): ")
            password = generate_password(
                length,
                use_uppercase,
                use_lowercase,
                use_digits,
                use_symbols,
            )
            selected_types = sum((use_uppercase, use_lowercase, use_digits, use_symbols))
            print(f"\nPassword: {password}")
            print(f"Strength: {password_strength(length, selected_types)}")
        except ValueError as error:
            print(f"Error: {error}")

        if not ask_yes_no("Generate another password? (y/N): ", default=False):
            break


if __name__ == "__main__":
    main()
