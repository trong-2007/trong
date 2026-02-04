#Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.
number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1
#Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.
while True:
    inches = float(input("Enter inches (negative to quit): "))
    if inches < 0:
        break
    centimeters = inches * 2.54
    print(f"{inches} inches is equal to {centimeters} centimeters.")
#Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally, the program prints out the smallest and largest number from the numbers it received.
numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == "":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if numbers:
    smallest = min(numbers)
    largest = max(numbers)
    print(f"Smallest number: {smallest}")
    print(f"Largest number: {largest}")
else:
    print("No numbers were entered.")
#Write a program that asks the user for a username and password. If either or both are incorrect, the program ask the user to enter the username and password again. This continues until the login information is correct or wrong credentials have been entered five times. If the information is correct, the program prints out Welcome. After five failed attempts the program prints out Access denied. The correct username is python and password rules.
correct_username = "python"
correct_password = "rules"
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    else:
        attempts += 1
        print("Incorrect username or password. Please try again.")
else:
    print("Access denied")
#Write a function that extracts the middle character of a given string. If the string length is even, extract the middle two characters.
def get_middle(s):
    length = len(s)
    mid = length // 2
    if length % 2 == 0:
        # Even length: return the middle two characters
        return s[mid - 1:mid + 1]
    else:
        # Odd length: return the middle character
        return s[mid]
#Write a function that takes a phrase and returns an acronym using the first letter of each word, capitalized. For example:
def generate_acronym(phrase):
    words = phrase.split()
    acronym = ''.join(word[0].upper() for word in words)
    return acronym