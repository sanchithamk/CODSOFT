import random
import string

def generate_password(length):
    if length <= 0:
        return "Password length must be a positive integer."

    # Define the character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the password includes at least one character from each set
    if length < 4:
        return "Password length must be at least 4 to include all character types."

    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Add random characters to reach the desired length
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")

    try:
        # Get user input for the password length
        length = int(input("Enter the desired length of the password: "))
        
        # Generate and display the password
        password = generate_password(length)
        print(f"Generated Password: {password}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
