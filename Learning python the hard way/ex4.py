cars = 100 # value of the total amount of cars
space_in_a_car = 4.0 # value of space or seats in a car 
drivers = 30 # value of amount of drivers
passengers = 90 # value of passengers from the day
cars_not_driven = cars - drivers # value of cars that werent used, its cars minus drivers
cars_driven = drivers # value of cars diven is the AMOUNT of drivers
carpool_capacity = cars_driven * space_in_a_car # capacity is cars_driven times space_in_a_car
average_passengers_per_car = passengers / cars_driven # value of the average passenger, passenegers divided by cars_driven

# print the text and add the values to calculate the cars available
print("There are", cars, "cars available.")
# refer above except for drivers, you're basically plugging in the values and variables
print("There are only", drivers, "drivers available.")

print("There will be", cars_not_driven, "empty cars today.")

print("We can transport", carpool_capacity, "people today.")

print("We have", passengers, "to carpool today.")

print("We need to put about", average_passengers_per_car, "in each car.")
