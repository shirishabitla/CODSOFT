import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4 characters."

    # Use letters, digits, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Program Start
print("=== Password Generator ===")

try:
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    print("\nGenerated Password:", password)
except ValueError:
    print("Invalid input! Please enter a number.")