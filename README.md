# Car-Park-System

This project will implement a simplified car park system using Object-Oriented Programming (OOP) concepts in Python. The system will consist of a car park, sensors, and displays to track the cars entering and exiting and the availability of parking bays.


**CarPark Class**

*Attributes*:

location: String representing the location of the car park.
capacity: Integer indicating the total number of parking bays available.
plates: List of strings holding the license plates of cars currently parked.
sensors: List holding instances of Sensor objects associated with this car park.
displays: List holding instances of Display objects for showing car park information.

*Methods*:

add_car(plate): Adds a car's license plate to the plates list and updates displays.
remove_car(plate): Removes a car's license plate from the plates list and updates displays.
register(component): Registers a Sensor or Display to the car park.
update_displays(): Updates all displays with the current status of the car park.

**Sensor Class**

*Attributes*:

id: Unique identifier for the sensor.
is_active: Boolean indicating whether the sensor is active.
car_park: Reference to the CarPark object this sensor is associated with.

*Methods*:

detect_vehicle(): Detects a vehicle and processes its entry or exit.
activate(): Activates the sensor.
deactivate(): Deactivates the sensor.

**Display Class**

*Attributes*:

id: Unique identifier for the display.
message: String message currently shown on the display.
is_on: Boolean indicating whether the display is turned on.
car_park: Reference to the CarPark object this display is associated with.

*Methods*:

update(data): Updates the display with new data.
turn_on(): Turns on the display.
turn_off(): Turns off the display.