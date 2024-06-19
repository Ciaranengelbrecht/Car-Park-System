class Sensor:
    def __init__(self, id, is_active=False, car_park=None):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        status = "active" if self.is_active else "inactive"
        return f"Sensor {self.id} is {status}"

class EntrySensor(Sensor):
    def detect_vehicle(self):
        print("Vehicle entering")

class ExitSensor(Sensor):
    def detect_vehicle(self):
        print("Vehicle exiting")
