class Display:
    def __init__(self, id, message="", is_on=False, car_park=None):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        status = "on" if self.is_on else "off"
        return f"Display {self.id}: {self.message} - {status}"

display = Display(1, "Welcome to the car park", True)
print(display)
