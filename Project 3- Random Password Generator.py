import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
all_characters = letters + numbers
print("===================================")
print("      Random Password Generator    ")
print("====================================")
try:
    length_input = input("Enter the wanted password length: ")
    password_length = int(length_input)
    password = ""

    for i in range(password_length):
        random_char = random.choice(all_characters)
        password = password + random_char

    print("\n====================================-")
    print(f"Your generated password: {password}")
    print("======================================")

except ValueError:
        print("Please enter a valid number.")

