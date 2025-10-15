import string

def check_password_strength(password):
    score = 0
    suggestions = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Make it at least 8 characters long.")

    # Check for lowercase letters
    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    # Check for uppercase letters
    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    # Check for digits
    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("Add a number.")

    # Check for special characters
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        suggestions.append("Add a special character (e.g., @, #, !).")

    # Determine password strength based on score
    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestions

# Main program
if __name__ == "__main__":
    # Get password input from the user
    pwd = input("Enter password: ")
    
    # Calculate strength and get suggestions
    strength, suggestions = check_password_strength(pwd)

    # Display results
    print(f"\nPassword strength: {strength}\n")
    if suggestions:
        print("Suggestions to improve your password:")
        for s in suggestions:
            print(" -", s)
