class vehicle:
    def move(self):
        print("vehicle is moving")
class car(vehicle):
    def move(self):
        print("Drving road")
class bicycle(vehicle):
    def move(self):
        print("peddling")
vehicles=[car(),bicycle()]
for Vehicle in  vehicles:
    Vehicle.move()
