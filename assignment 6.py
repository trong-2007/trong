#Write a program that asks the user to enter numbers until they input an empty string to quit. At the end, the program prints out the five greatest numbers sorted in descending order. Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.
# Initialize an empty list to store the numbers
numbers = []

while True:
    # Prompt the user for input
    user_input = input("Enter a number (or press Enter to finish): ")
    # Check if the input is empty
    if user_input == "":
        break
    try:
        # Convert input to float and add to the list
        num = float(user_input)
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Check if we have at least five numbers
if len(numbers) < 5:
    print("You entered fewer than five numbers.")
else:
    # Sort the list in descending order
    sorted_numbers = sorted(numbers, reverse=True)
    # Get the top five numbers
    top_five = sorted_numbers[:5]
    print("The five greatest numbers are:", top_five)
#Write a program that asks the user for a number of a month and then prints out the corresponding season (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program. We can define each season to last three months, December being the first month of winter.
# Tuple of seasons
seasons = ("winter", "spring", "summer", "autumn")

# Prompt the user for a month number
month = int(input("Enter the month number (1-12): "))

# Determine the season
if month == 12 or month == 1 or month == 2:
    season = "winter"
elif 3 <= month <= 5:
    season = "spring"
elif 6 <= month <= 8:
    season = "summer"
elif 9 <= month <= 11:
    season = "autumn"
else:
    season = "Invalid month"

if season != "Invalid month":
    print(f"The month {month} is in {season}.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
#Write a program that asks the user to enter names until they enter an empty string. After each name is read, the program either prints out New name or Existing name depending on whether the name was entered for the first time. Finally, the program lists out the input names one by one, one below another in any order. Use the set data structure to store the names.
# Initialize an empty set to store names
names_set = set()

while True:
    name = input("Enter a name (or press Enter to finish): ")
    if name == "":
        break
    if name in names_set:
        print("Existing name")
    else:
        print("New name")
        names_set.add(name)

# List out the names one by one
print("\nList of names:")
for name in names_set:
    print(name)
#Write a function that will determine the frequency of a word (i.e. how many times does a word appears) in a given piece of text, then calculate the proportion of the 5 most common words relative to the piece of text. For example:
def word_frequencies(text):
    # Split the text into words (assuming words are separated by whitespace)
    words = text.lower().split()
    total_words = len(words)

    # Count the frequency of each word using a dictionary
    freq_dict = {}
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1

    # Sort the dictionary items by frequency in descending order
    sorted_freq = sorted(freq_dict.items(), key=lambda item: item[1], reverse=True)

    # Get the top 5 most common words
    top_5 = dict(sorted_freq[:5])

    # Calculate the total count of the top 5 words
    top_5_total = sum(top_5.values())

    # Calculate the proportion
    proportion = (top_5_total / total_words) * 100 if total_words > 0 else 0

    # Output the results
    print(f"Top 5: {top_5}")
    print(f"Total number of words: {total_words}")
    print(f"Proportion of 5 most common words: {top_5_total} / {total_words} = {proportion:.2f}%")
#Write a function that gets a list of integers as a parameter. The function returns a second list that is otherwise the same as the original list except that all odd numbers have been removed. For testing, write a main program where you create a list, call the function, and then print out both the original as well as the cut-down list.
def remove_odd_numbers(numbers):
    # Return a new list containing only even numbers
    return [num for num in numbers if num % 2 == 0]

# Main program for testing
def main():
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filtered_list = remove_odd_numbers(original_list)

    print("Original list:", original_list)
    print("Filtered list (no odd numbers):", filtered_list)

# Run the main function
if __name__ == "__main__":
    main()