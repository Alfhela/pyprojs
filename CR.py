class Auto:
    def __init__(self, driver=False, fueled=True):
        self.has_driver = driver
        self.has_fuel = fueled
        self.turn = 'straight'

    def turned(self, side):
        if side in ('left', 'straight', 'right'):
            self.turn = side
        else:
            raise ValueError

    def get_driver(self):
        self.has_driver = True


class ElectricAuto(Auto):
    pass


class FuelAuto(Auto):

    def fuel(self):
        self.has_fuel = True


class TrafficLight:
    def __init__(self, color='red'):
        self.color = color
        self.can_work = True

    def getcolor(self):
        return self.color

    def setcolor(self, color):
        if color in ('red', 'yellow', 'green'):
            self.color = color
        else:
            raise  ValueError

    def setstatus(self, status: bool):
        self.can_work = status


class Driver:
    def __init__(self, name):
        self.name = name

        self.car = None

    def drive(self, car: Auto):
        self.car = car
        self.car.get_driver()

    def seecolor(self, light: TrafficLight):
        return light.getcolor()

    def fuel_car(self, car: FuelAuto):
        car.fuel()

    def turn_handlebar(self, side):
        if self.car:
            self.car.turned(side)


d1 = Driver("Peter")
d2 = Driver("Mike")
c1 = FuelAuto()
c2 = FuelAuto()
c3 = FuelAuto()
c4 = ElectricAuto()
c5 = ElectricAuto()

d1.drive(c1)
d2.drive(c2)

d1.turn_handlebar('left')
d2.turn_handlebar('right')
