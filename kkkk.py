hours = float(input('Enter Hours: '))
rate = float(input('Enter Rate: '))
x = 1.5
amount = float(input('Enter amount of above hours:'))
pay = hours * rate + amount * x * rate
print(f'Pay: {pay}')