"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):

    def __init__(self, weight=1500, fuel=50, fuel_consumption=10, max_cargo=0):
        super(Plane, self).__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, cargo):
            if self.cargo + cargo <= self.max_cargo:
                self.cargo += cargo
            else:
                raise CargoOverload("Load capacity exceeded")

    def remove_all_cargo(self):
        n = self.cargo
        self.cargo = 0
        return n
