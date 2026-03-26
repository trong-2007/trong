#Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters. The elevator has methods go_to_floor, floor_up and floor_down. A new elevator is always at the bottom floor. If you make elevator h for example the method call h.go_to_floor(5), the method calls either the floor_up or floor_down methods as many times as it needs to get to the fifth floor. The methods run the elevator one floor up or down and tell what floor the elevator is after each move. Test the class by creating an elevator in the main program, tell it to move to a floor of your choice and then back to the bottom floor.
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor  # Elevator starts at bottom floor
        print(f"Elevator initialized at floor {self.current_floor}")

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Moved up to floor {self.current_floor}")
        else:
            print("Already at the top floor, cannot go up.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Moved down to floor {self.current_floor}")
        else:
            print("Already at the bottom floor, cannot go down.")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print(f"Target floor {target_floor} is out of range.")
            return

        print(f"Moving from floor {self.current_floor} to {target_floor}")
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
        print(f"Arrived at floor {self.current_floor}")

# Test the Elevator class
if __name__ == "__main__":
    # Create an elevator with floors 0 to 10
    elevator = Elevator(0, 10)

    # Move to floor 7
    elevator.go_to_floor(7)

    # Move back to bottom floor
    elevator.go_to_floor(elevator.bottom_floor)
#Extend the previous program by creating a Building class. The initializer parameters for the class are the numbers of the bottom and top floors and the number of elevators in the building. When a building is created, the building creates the required number of elevators. The list of elevators is stored as a property of the building. Write a method called run_elevator that accepts the number of the elevator and the destination floor as its parameters. In the main program, write the statements for creating a new building and running the elevators of the building.
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor  # Elevator starts at bottom floor
        print(f"Elevator initialized at floor {self.current_floor}")

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Moved up to floor {self.current_floor}")
        else:
            print("Already at the top floor, cannot go up.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Moved down to floor {self.current_floor}")
        else:
            print("Already at the bottom floor, cannot go down.")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print(f"Target floor {target_floor} is out of range.")
            return

        print(f"Moving from floor {self.current_floor} to {target_floor}")
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
        print(f"Arrived at floor {self.current_floor}")

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]
        print(f"Building created with {num_elevators} elevators.")

    def run_elevator(self, elevator_number, destination_floor):
        if elevator_number < 0 or elevator_number >= len(self.elevators):
            print("Invalid elevator number.")
            return
        elevator = self.elevators[elevator_number]
        print(f"\nRunning elevator {elevator_number} to floor {destination_floor}")
        elevator.go_to_floor(destination_floor)

# Main program
if __name__ == "__main__":
    # Create a building with floors 0 to 10 and 3 elevators
    building = Building(0, 10, 3)

    # Run elevator 0 to floor 5
    building.run_elevator(0, 5)

    # Run elevator 2 to top floor
    building.run_elevator(2, 10)

    # Run elevator 1 back to bottom floor
    building.run_elevator(1, 0)
#Extend the program again by adding a method fire_alarm that does not receive any parameters and moves all elevators to the bottom floor. Continue the main program by causing a fire alarm in your building.
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor  # Elevator starts at bottom floor
        print(f"Elevator initialized at floor {self.current_floor}")

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Moved up to floor {self.current_floor}")
        else:
            print("Already at the top floor, cannot go up.")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Moved down to floor {self.current_floor}")
        else:
            print("Already at the bottom floor, cannot go down.")

    def go_to_floor(self, target_floor):
        if target_floor < self.bottom_floor or target_floor > self.top_floor:
            print(f"Target floor {target_floor} is out of range.")
            return

        print(f"Moving from floor {self.current_floor} to {target_floor}")
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
        print(f"Arrived at floor {self.current_floor}")

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for _ in range(num_elevators)]
        print(f"Building created with {num_elevators} elevators.")

    def run_elevator(self, elevator_number, destination_floor):
        if elevator_number < 0 or elevator_number >= len(self.elevators):
            print("Invalid elevator number.")
            return
        elevator = self.elevators[elevator_number]
        print(f"\nRunning elevator {elevator_number} to floor {destination_floor}")
        elevator.go_to_floor(destination_floor)

    def fire_alarm(self):
        print("\nFIRE ALARM! Moving all elevators to the bottom floor.")
        for idx, elevator in enumerate(self.elevators):
            print(f"\nMoving elevator {idx} to bottom floor")
            elevator.go_to_floor(self.bottom_floor)

# Main program
if __name__ == "__main__":
    # Create a building with floors 0 to 10 and 3 elevators
    building = Building(0, 10, 3)

    # Run some elevators to different floors
    building.run_elevator(0, 5)
    building.run_elevator(2, 10)
    building.run_elevator(1, 0)

    # Now, simulate a fire alarm
    building.fire_alarm()
#Write a main program that creates an 8000-kilometer race called Grand Demolition Derby. The new race is given a list of ten cars similarly to the earlier exercise. The main program simulates the progressing of the race by calling the hour_passes in a loop, after which it uses the race_finished method to check if the race has finished. The current status is printed out using the print_status method every ten hours and then once more at the end of the race.
import random

class Race:
    def __init__(self, name, kilometers, cars):
        self.name = name
        self.kilometers = kilometers
        self.cars = cars  # list of Car objects

    def hour_passes(self):
        for car in self.cars:
            # Generate a random change in speed: e.g., -10 to +10 km/h
            speed_change = random.randint(-10, 10)
            car.adjust_speed(speed_change)
            car.drive()  # move the car based on its current speed

    def print_status(self):
        print(f"\nStatus of the race: {self.name}")
        print(f"{'Car Name':<15} {'Speed (km/h)':<15} {'Distance Covered (km)':<25}")
        for car in self.cars:
            print(f"{car.name:<15} {car.speed:<15} {car.distance_covered:<25}")

    def race_finished(self):
        for car in self.cars:
            if car.distance_covered >= self.kilometers:
                return True
        return False

# Example Car class for completeness
class Car:
    def __init__(self, name):
        self.name = name
        self.speed = 0  # current speed in km/h
        self.distance_covered = 0

    def adjust_speed(self, change):
        self.speed += change
        if self.speed < 0:
            self.speed = 0

    def drive(self):
        # Move the car forward based on current speed
        self.distance_covered += self.speed

# Main program
if __name__ == "__main__":
    # Create a list of 10 cars
    car_names = [f"Car {i+1}" for i in range(10)]
    cars = [Car(name) for name in car_names]

    # Create the race
    race = Race("Grand Demolition Derby", 8000, cars)

    hours = 0
    # Run the race until finished
    while not race.race_finished():
        hours += 1
        race.hour_passes()

        # Print status every 10 hours
        if hours % 10 == 0:
            print(f"\n--- Status after {hours} hours ---")
            race.print_status()

    # Final status after race ends
    print(f"\nRace finished after {hours} hours!")
    race.print_status()