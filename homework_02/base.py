from abc import ABC

from homework_02 import exceptions


class Vehicle(ABC):
    def __init__(self, weight=0, started=None, fuel=0, fuel_consumption=0):
        self.weight = weight
        self._started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    @property
    def started(self):
        return self._started()

    @started.setter
    def start(self, fuel):
        if self.fuel > 0:
            started = True
            return self._started
        else:
            raise LowFuelError('топлива недостаточна для запуска двигателя')

    @staticmethod
    def move(fuel, fuel_consumption):
        if fuel > fuel_consumption:
            fuel -= fuel_consumption
            return fuel
        else:
            raise NotEnoughFuel('топлива недостаточно для преодоления дистанции')