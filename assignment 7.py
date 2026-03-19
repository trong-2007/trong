#Write a Car class that has the following properties: registration number, maximum speed, current speed and travelled distance. Add a class initializer that sets the first two of the properties based on parameter values. The current speed and travelled distance of a new car must be automatically set to zero. Write a main program where you create a new car (registration number ABC-123, maximum speed 142 km/h). Finally, print out all the properties of the new car.
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0


# Main program
def main():
    # Create a new car with registration number ABC-123 and maximum speed 142 km/h
    my_car = Car("ABC-123", 142)

    # Print out all properties
    print("Car Properties:")
    print(f"Registration Number: {my_car.registration_number}")
    print(f"Maximum Speed: {my_car.max_speed} km/h")
    print(f"Current Speed: {my_car.current_speed} km/h")
    print(f"Travelled Distance: {my_car.travelled_distance} km")


# Run the main function
if __name__ == "__main__":
    main()


#Extend the program by adding an accelerate method into the new class. The method should receive the change of speed (km/h) as a parameter. If the change is negative, the car reduces speed. The method must change the value of the speed property of the object. The speed of the car must stay below the set maximum and cannot be less than zero. Extend the main program so that the speed of the car is first increased by +30 km/h, then +70 km/h and finally +50 km/h. Then print out the current speed of the car. Finally, use the emergency brake by forcing a -200 km/h change on the speed and then print out the final speed. The travelled distance does not have to be updated yet.
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        # Change the speed by the specified amount
        new_speed = self.current_speed + speed_change
        # Ensure the speed doesn't go below 0
        if new_speed < 0:
            new_speed = 0
        # Ensure the speed doesn't exceed the maximum speed
        elif new_speed > self.max_speed:
            new_speed = self.max_speed
        self.current_speed = new_speed


# Main program
def main():
    # Create a new car with registration number ABC-123 and maximum speed 142 km/h
    my_car = Car("ABC-123", 142)

    # Print initial properties
    print("Initial Car Properties:")
    print(f"Registration Number: {my_car.registration_number}")
    print(f"Maximum Speed: {my_car.max_speed} km/h")
    print(f"Current Speed: {my_car.current_speed} km/h")
    print(f"Travelled Distance: {my_car.travelled_distance} km\n")

    # Increase speed by +30 km/h
    my_car.accelerate(30)
    # Increase speed by +70 km/h
    my_car.accelerate(70)
    # Increase speed by +50 km/h
    my_car.accelerate(50)

    # Print current speed
    print(f"Speed after accelerations: {my_car.current_speed} km/h")

    # Use emergency brake by forcing -200 km/h change
    my_car.accelerate(-200)

    # Print final speed
    print(f"Final speed after emergency brake: {my_car.current_speed} km/h")


# Run the main function
if __name__ == "__main__":
    main()


#Again, extend the program by adding a new drive method that receives the number of hours as a parameter. The method increases the travelled distance by how much the car has travelled in constant speed in the given time. Example: The travelled distance of car object is 2000 km. The current speed is 60 km/h. Method call car.drive(1.5) increases the travelled distance to 2090 km.
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        # Change the speed by the specified amount
        new_speed = self.current_speed + speed_change
        # Ensure the speed doesn't go below 0
        if new_speed < 0:
            new_speed = 0
        # Ensure the speed doesn't exceed the maximum speed
        elif new_speed > self.max_speed:
            new_speed = self.max_speed
        self.current_speed = new_speed

    def drive(self, hours):
        # Increase travelled distance based on current speed and hours driven
        distance_travelled = self.current_speed * hours
        self.travelled_distance += distance_travelled


# Main program
def main():
    # Create a new car with registration number ABC-123 and maximum speed 142 km/h
    my_car = Car("ABC-123", 142)

    # Print initial properties
    print("Initial Car Properties:")
    print(f"Registration Number: {my_car.registration_number}")
    print(f"Maximum Speed: {my_car.max_speed} km/h")
    print(f"Current Speed: {my_car.current_speed} km/h")
    print(f"Travelled Distance: {my_car.travelled_distance} km\n")

    # Accelerate the car in steps
    my_car.accelerate(30)
    my_car.accelerate(70)
    my_car.accelerate(50)

    # Print current speed
    print(f"Speed after accelerations: {my_car.current_speed} km/h")

    # Use emergency brake
    my_car.accelerate(-200)
    print(f"Speed after emergency brake: {my_car.current_speed} km/h")

    # Drive the car for 1.5 hours
    my_car.drive(1.5)
    print(f"Travelled distance after driving for 1.5 hours: {my_car.travelled_distance} km")

    # For demonstration, let's drive again for 2 hours
    my_car.drive(2)
    print(f"Travelled distance after additional 2 hours: {my_car.travelled_distance} km")


# Run the main function
if __name__ == "__main__":
    main()
#Now we will program a car race. The travelled distance of a new car is initialized as zero. At the beginning of the main program, create a list that consists of 10 car objects created using a loop. The maximum speed of each new car is a random value between 150 km/h and 200 km/h. The registration numbers are created as follows: "ABC-1", "ABC-2" and so on. Now the race begins. One per every hour of the race, the following operations are performed:
import random


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        new_speed = self.current_speed + speed_change
        if new_speed < 0:
            new_speed = 0
        elif new_speed > self.max_speed:
            new_speed = self.max_speed
        self.current_speed = new_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


def print_race_standings(cars):
    print(f"{'Reg. Number':<12} {'Max Speed':<10} {'Speed':<10} {'Distance':<12}")
    print("-" * 44)
    for car in cars:
        print(
            f"{car.registration_number:<12} {car.max_speed:<10} {car.current_speed:<10} {car.travelled_distance:<12.2f}")


def main():
    # Create 10 cars with random max speeds between 150 and 200 km/h
    cars = []
    for i in range(1, 11):
        max_speed = random.randint(150, 200)
        registration_number = f"ABC-{i}"
        cars.append(Car(registration_number, max_speed))

    race_finished = False
    hour = 0

    # Run the race until one car reaches at least 10,000 km
    while not race_finished:
        hour += 1
        # For each car, change speed randomly between -10 and +15 km/h
        for car in cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)  # Drive for 1 hour

        # Check if any car has reached or exceeded 10,000 km
        for car in cars:
            if car.travelled_distance >= 10000:
                race_finished = True
                break

    # Print final standings
    print("\nRace finished! Final standings:")
    print_race_standings(cars)


if __name__ == "__main__":
    main()
#How much time did it take for you to work on this assignment? Please include your answer in a separate .txt file. (Make sure it's an actual numerical value is included)
import leap_second
with open("time_taken.txt", "w") as file:
    file.write(f"Time taken to complete the assignment: {elapsed_time:.2f} seconds.\n")


