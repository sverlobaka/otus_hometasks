"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):
    cargo = None
    max_cargo = None


    def __init__(self, max_cargo, weight=0, fuel=0, fuel_consumption=0):
        super().__init__(weight=weight, fuel=fuel, fuel_consumption=fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, add_cargo):
        new_cargo = self.cargo + add_cargo
        if new_cargo > self.max_cargo:
            raise CargoOverload('перегруз')
        else:
            self.cargo = new_cargo