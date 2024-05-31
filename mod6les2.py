class Vehicle:
    vehicle_type = "none"

class Car:
    price = 1000000

    def horse_powers(self):
        self.horse_powers = horse_powers


class Nissan (Car, Vehicle):
    def __init__(self, price, vehicle_type):
        Car.price = price
        Vehicle.vehicle_type = vehicle_type

    def horse_powers(self):
        super().horse_powers()

    def __str__(self):
        return '{} Тип ТС: {} цена: {} л/с: {}'.format(
            self.__class__, self.vehicle_type, self.price, self.horse_powers)


bibi1 = Nissan(2500000, 'pickups')
bibi1.horse_powers = 150
print(bibi1)

bibi2 = Nissan(1800000, 'sedans')
bibi2.horse_powers = 90
print(bibi2)




