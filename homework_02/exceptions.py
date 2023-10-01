"""
Объявите следующие исключения:
- LowFuelError - низки запас топлива
- NotEnoughFuel - недостаточно топлива
- CargoOverload - перегрузка
"""

class LowFuelError(Exception):
    pass


class NotEnoughFuel(Exception):
    pass

class CargoOverload(Exception):
    pass