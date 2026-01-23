#Write a function that asks a fisher the length of a zander in centimeters. If the zander does not fulfill the size limit, the program instructs to release the fish back into the lake and notifies the user of how many centimeters below the size limit the caught fish was. A zander must be 42 centimeters or longer to meet the size limit.
def check_zander_size():
    length = float(input("Enter the length of the zander (cm): "))
    size_limit = 42

    if length < size_limit:
        difference = size_limit - length
        print(f"The zander is too small. Release it back into the lake.")
        print(f"It is {difference:.1f} cm below the size limit.")
    else:
        print("The zander meets the size limit. You can keep it.")
#Write a function that asks the user to enter the cabin class of a cruise ship and then prints out a written description according to the list below. You must use an if/elif/else structure in your solution.
def cabin_description():
    cabin = input("Enter the cabin class (LUX, A, B, C): ").upper()

    if cabin == "LUX":
        print("Upper-deck cabin with a balcony.")
    elif cabin == "A":
        print("Above the car deck, equipped with a window.")
    elif cabin == "B":
        print("Windowless cabin above the car deck.")
    elif cabin == "C":
        print("Windowless cabin below the car deck.")
    else:
        print("Invalid cabin class.")
#Write a function that asks for the user's biological sex and hemoglobin value (g/l). The program the notifies the user if the hemoglobin value is low, normal or high.
def hemoglobin_check():
    sex = input("Enter biological sex (male/female): ").lower()
    hb = float(input("Enter hemoglobin value (g/l): "))

    if sex == "female":
        if hb < 117:
            print("Hemoglobin level is low.")
        elif hb <= 155:
            print("Hemoglobin level is normal.")
        else:
            print("Hemoglobin level is high.")

    elif sex == "male":
        if hb < 134:
            print("Hemoglobin level is low.")
        elif hb <= 167:
            print("Hemoglobin
#Write a function that asks the user to enter a year and notifies the user whether the input year is a leap year. A year is a leap year if it is divisible by four. However, years divisible by 100 are leap years only if they are also divisible by 400.
def check_leap_year():
    year = int(input("Enter a year: "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("The year", year, "is a leap year.")
    else:
        print("The year", year, "is not a leap year.")
#Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of the pizza in USD. The function calculates and returns the unit price of the pizza per square meter. The main program asks the user to enter the diameter and price of two pizzas, and tells the user which pizza provides better value for money (which of them has a lower unit price). You must use the function you wrote for calculating the unit prices.
import math

def pizza_unit_price(diameter_cm, price_usd):
    radius_cm = diameter_cm / 2
    area_cm2 = math.pi * radius_cm ** 2
    area_m2 = area_cm2 / 10000   # convert cm² to m²
    return price_usd / area_m2
# Input for pizza 1
d1 = float(input("Enter the diameter of pizza 1 (cm): "))
p1 = float(input("Enter the price of pizza 1 (USD): "))

# Input for pizza 2
d2 = float(input("Enter the diameter of pizza 2 (cm): "))
p2 = float(input("Enter the price of pizza 2 (USD): "))

# Calculate unit prices using the function
unit_price1 = pizza_unit_price(d1, p1)
unit_price2 = pizza_unit_price(d2, p2)

# Compare and display result
if unit_price1 < unit_price2:
    print("Pizza 1 provides better value for money.")
elif unit_price2 < unit_price1:
    print("Pizza 2 provides better value for money.")
else:
    print("Both pizzas provide the same value for money.")
