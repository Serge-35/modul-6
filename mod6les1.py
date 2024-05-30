class Car:
    price = 1000000

    def horse_powers(self):
        self.horse_powers = horse_powers

    def __str__(self):
        return '{} цена: {} л/с: {}'.format(
            self.__class__, self.price, self.horse_powers)

bibi = Car()
bibi.horse_powers = 70

print(bibi)

class Nissan(Car):
    price = 1500000
    horse_powers = 120

bibi2 = Nissan()

class Kia(Car):
    price = 1750000
    def __init__(self, horse_powers):
        self.horse_powers = horse_powers

bibi3 = Kia(105)

print(bibi2)
print(bibi3)
