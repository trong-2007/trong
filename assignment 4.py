#Write a program that asks the user to enter numbers until they input an empty string to quit. At the end, the program prints out the five greatest numbers sorted in descending order. Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.
# Initialize an empty list to store the numbers
numbers = []

while True:
    user_input = input("Enter a number (or press Enter to finish): ")
    if user_input == "":
        break
    try:
        # Convert input to float to handle decimal numbers
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Check if there are at least 5 numbers
if len(numbers) < 5:
    print("You entered fewer than 5 numbers.")
    # Optionally, display all entered numbers sorted
    sorted_numbers = sorted(numbers, reverse=True)
    print("Numbers in descending order:", sorted_numbers)
else:
    # Sort the list in descending order
    sorted_numbers = sorted(numbers, reverse=True)
    # Get the top 5 numbers
    top_five = sorted_numbers[:5]
    print("The five greatest numbers in descending order:", top_five)
#Write a program that asks the user for an integer and tells if the number is a prime number. Prime numbers are number that are only divisible by one or the number itself.
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Check odd divisors up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Ask the user for an integer
try:
    number = int(input("Enter an integer: "))
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
#Write a program that asks the user to enter the names of five cities one by one (use a for loop for reading the names) and stores them into a list structure. Finally, the program prints out the names of the cities one by one, one city per line, in the same order they were read as input. Use a for loop for asking the names and a for/in loop to iterate through the list.
# Initialize an empty list to store city names
cities = []

# Use a for loop to read five city names
for i in range(5):
    city_name = input(f"Enter the name of city {i+1}: ")
    cities.append(city_name)

# Use a for/in loop to print each city name
print("\nThe cities you entered are:")
for city in cities:
    print(city)
#Write a function that gets a list of integers as a parameter. The function returns the sum of all the numbers in the list. For testing, write a main program where you create a list, call the function, and print out the value it returned.
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Create a list of integers for testing
numbers_list = [3, 7, 2, 9, 5]

# Call the function and store the result
sum_result = sum_of_list(numbers_list)

# Print the result
print(f"The sum of the list is: {sum_result}")
#Write a function that gets a list of integers as a parameter. The function returns a second list that is otherwise the same as the original list except that all uneven numbers have been removed. For testing, write a main program where you create a list, call the function, and then print out both the original as well as the cut-down list.
def remove_uneven_numbers(numbers):
    # Create a new list with only even numbers
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

# Create a list of integers for testing
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Call the function
filtered_list = remove_uneven_numbers(original_list)

# Print both lists
print("Original list:", original_list)
print("Filtered list (only even numbers):", filtered_list)