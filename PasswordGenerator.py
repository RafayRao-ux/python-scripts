import random
import string

def generate_password(length, use_digits, use_symbols):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += "!@#$%&*><+="
    return ''.join(random.choice(chars) for _ in range(length))

length = int(input("Password length: "))
digits = input("Include numbers? (y/n): ") == 'y'
symbols = input("Include symbols? (y/n): ") == 'y'
label = input("What is this password for? (e.g. Gmail, Facebook, Google, Instagram ): ")

password = generate_password(length, digits, symbols)
print(f"\nYour password: {password}")

with open("passwords.txt", "a") as f:
    f.write(f"{label}: {password}\n")

print("Saved to passwords.txt")