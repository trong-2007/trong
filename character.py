#Write a program that asks your name and then greets you by your name
from tarfile import LinkOutsideDestinationError
name = input('What is your name? ')
print(f'Hello {name}')
#Write a program that asks the user for the radius of a circle and the prints out the circumference of the circle.
import math
radius = float(input('Enter the radius of the circle: '))
circumference = math.pi * radius**2
print(f'The circumference of the circle is {circumference}')
#Write a program that asks the user for the length and width of a rectangle. The program then prints out the perimeter and area of the rectangle. The perimeter of a rectangle is the sum of the lengths of each four sides
length = float(input('What is the length of the rectangle? '))
width = float(input('What is the width of the rectangle? '))
area = length * width
perimeter = 2 * (length + width)
print(f'The area of the circle is {area}')
print(f'The perimeter of the rectangle is {perimeter}')
#Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers.
a = float(input('first number'))
b = float(input('second number'))
c = float(input('third number'))
sum = a + b + c
product = a * b * c
average = sum / 3
print(f'The average area of the circle is {average}')
print(f'The product of the circle is {product}')
print(f'The sum of the circle is {sum}')
#Write a program that asks the user to enter a mass in medieval units: talents, pounds, and lots. The program converts the input to full kilograms and grams and outputs the result to the user:
POUNDS_PER_TALENT = 20
LOTS_PER_POUND = 32
GRAMS_PER_LOT = 13.3
talents = float(input('How many talents would you like? '))
pounds = float(input('How many pounds would you like? '))
lots = float(input('How many lots would you like? '))
total_lots = talents *  POUNDS_PER_TALENT * LOTS_PER_POUND + pounds * LOTS_PER_POUND + lots
total_grams = total_lots * GRAMS_PER_LOT
kilograms = float(total_grams // 1000)
grams = total_grams % 1000
print(f"\nThe mass is {kilograms} kilograms and {grams:.2f} grams.")
#Write a program that draws two random combinations of numbers for a combination lock:
#a 3-digit code where each number is between 0 and 9.
#a 4-digit code where each number is between 1 and 6.
import random
code_3_digit = [random.randint(0,9) for _ in range(3)]
code_4_digit = [random.randint(1,6) for _ in range(4)]
print("3-digit combination (0-9)", code_3_digit)
print("4-digit combination (1-6)", code_4_digit)