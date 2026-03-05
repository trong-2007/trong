#Your university uses course codes that consist of 2-3 uppercase letters, followed by 3 digits (e.g., "TEC001", "AU006"). Write a function that returns True if a given string matches this format and False otherwise.
import re

def is_valid_course_code(code: str) -> bool:
    pattern = r'^[A-Z]{2,3}\d{3}$'
    return bool(re.match(pattern, code))
#Web colors are often written in hexadecimal format: a # followed by exactly 6 characters (digits 0-9 or letters A-F, case insensitive). Write a function that checks if a given string is a valid hex color or not.
import re

def is_valid_hex_color(color: str) -> bool:
    pattern = r'^#([0-9A-Fa-f]{6})$'
    return bool(re.match(pattern, color))
#Write a function that will find all numbers in a given paragraph, then calculate the sum of all numbers you've found. For example:
import re

def sum_numbers_in_text(text: str) -> int:
    numbers = re.findall(r'\d+', text)
    total = sum(int(num) for num in numbers)
    return total
#For privacy reasons, you need to hide phone numbers in a document. Write a function that replaces any sequence of 10 digits or those that starts with "+84" with the string [REDACTED]. For example:
import random

def estimate_pi(num_points):
    inside_circle = 0
    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 < 1:
            inside_circle += 1
    return 4 * inside_circle / num_points

def main():
    num_points = int(input("Enter the number of random points to generate: "))
    pi_estimate = estimate_pi(num_points)
    print(f"Approximate value of pi: {pi_estimate}")

if __name__ == "__main__":
    main()