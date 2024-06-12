class CarPark:
    def __init__(self, location="Unknown", capacity=0, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates if plates is not None else []
        self.sensors = sensors if sensors is not None else []
        self.displays = displays if displays is not None else []

    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays."

car_park = CarPark("123 Example Street", 100)
print(car_park)
