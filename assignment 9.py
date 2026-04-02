#Write a function that will open a text file and count the total number of lines of text in that file. Blank lines will be ignored and does not add to the total count.
def count_non_blank_lines(file_path):
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Check if line is not blank
                count += 1
    return count
#Write a function that takes a text file and a specific keyword as its parameters. The function should return a list of line numbers (1-based index) where that keyword appears.
def find_keyword_lines(file_path, keyword):
    line_numbers = []
    with open(file_path, 'r') as file:
        for i, line in enumerate(file, start=1):
            if keyword in line:
                line_numbers.append(i)
    return line_numbers
#You have a text file where each line contains a name and a score separated by a comma (e.g., Alice,85). Write a program that calculates the average score of all students in the given file.
def calculate_average_score(file_path):
    total_score = 0
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            # Remove any leading/trailing whitespace and skip blank lines
            line = line.strip()
            if not line:
                continue
            # Split the line into name and score
            parts = line.split(',')
            if len(parts) != 2:
                continue  # Ignore malformed lines
            name, score_str = parts
            try:
                score = float(score_str)
                total_score += score
                count += 1
            except ValueError:
                continue  # Ignore lines with invalid score format
    if count == 0:
        return 0  # Avoid division by zero
    return total_score / count
#Write a function that implements the Caesar cipher technique. In particular:
def caesar_cipher(file_name, shift, direction):
    # Determine shift direction
    if direction.lower() == 'right':
        shift_amount = shift
    elif direction.lower() == 'left':
        shift_amount = -shift
    else:
        raise ValueError("Direction must be 'left' or 'right'.")

    # Read the original file
    with open(file_name, 'r') as file:
        content = file.read()

    result_chars = []

    for char in content:
        # Skip numbers
        if char.isdigit():
            result_chars.append(char)
            continue

        # Shift uppercase letters
        if char.isupper():
            original_ord = ord(char)
            # 'A' to 'Z' -> 65 to 90
            new_ord = (original_ord - 65 + shift_amount) % 26 + 65
            result_chars.append(chr(new_ord))
        # Shift lowercase letters
        elif char.islower():
            original_ord = ord(char)
            # 'a' to 'z' -> 97 to 122
            new_ord = (original_ord - 97 + shift_amount) % 26 + 97
            result_chars.append(chr(new_ord))
        else:
            # Non-alphabetic characters are unchanged
            result_chars.append(char)

    # Save the encrypted content to a new file
    output_file = 'ciphertext.txt'
    with open(output_file, 'w') as file:
        file.write(''.join(result_chars))

    print(f"Encrypted content saved to {output_file}")
