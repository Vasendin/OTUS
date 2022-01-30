from abc import ABC
from homework_02.exceptions import NotEnoughFuel, LowFuelError


class Vehicle(ABC):
    def __init__(self,
                 weight=1500,
                 fuel=50,
                 fuel_consumption=10
                 ):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
                print("start")
            else:
                raise LowFuelError("No fuel")

    def move(self, distance):
        if self.fuel >= self.fuel_consumption*distance:
            self.fuel -= self.fuel_consumption*distance
        else:
            raise NotEnoughFuel("NotEnoughFuel")
