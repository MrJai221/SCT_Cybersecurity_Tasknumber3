import re

def check_password_strength(password):
    score = 0
    length_criteria = len(password) >= 8
    upper_criteria = bool(re.search(r"[A-Z]", password))
    lower_criteria = bool(re.search(r"[a-z]", password))
    digit_criteria = bool(re.search(r"\d", password))
    special_criteria = bool(re.search(r"[!@#$%^&*()\-_=+{}[\]:;\"'<>,.?/~`|\\]", password))

    print("\nPassword Analysis:")
    print(f"- Length >= 8: {'✅' if length_criteria else '❌'}")
    print(f"- Contains uppercase: {'✅' if upper_criteria else '❌'}")
    print(f"- Contains lowercase: {'✅' if lower_criteria else '❌'}")
    print(f"- Contains digit: {'✅' if digit_criteria else '❌'}")
    print(f"- Contains special character: {'✅' if special_criteria else '❌'}")

    # Scoring
    criteria = [length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria]
    score = sum(criteria)

    # Determine strength
    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    print(f"\nPassword Strength: {strength} ({score}/5)")

def main():
    print("🔐 Password Strength Checker 🔐")
    password = input("Enter your password: ")
    check_password_strength(password)

if __name__ == "__main__":
    main()
