class car:
    def __init__(self):
        self.contact=4
        self.seats=5
    def drive(self):
        print("driving a car.......")

mycar =car()
mycar.drive()


class car:
    def __init__(self):
        self.wheels=4
        self.seats=5
    def drive(self):
        print("driving a car")
class sportscar(car):
    def __init__(self):
        super().__init__()
        self.engine_power="1200"
        self.seats =2
    def drive(self):
        print("driving a sport car.....")
mysportscar = sportscar()
mysportscar.drive()


