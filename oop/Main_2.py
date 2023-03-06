from Main import Vehicle

vehicle_one = Vehicle("Toyota", "white", "sheila","4", "1KZ")
vehicle_two = Vehicle("BMW", "blue", "wendy","4", "1KZ")
vehicle_three = Vehicle("Jeep", "red", "wafula","4", "1KZ")

print(vehicle_one.owner, vehicle_one.engine, vehicle_one.wheels)
print(vehicle_two.owner, vehicle_two.make, vehicle_two.color)
print(vehicle_three.owner, vehicle_three.color, vehicle_three.engine)