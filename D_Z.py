class Car:
    price = 1000000

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return "Марка {} модель {}, цена {}".format(self.__class__.__name__, self.model, self.price)

    def horse_powers(self):
        print("500 - HP")

class Nissan(Car):
    price = 1200000

    def horse_powers(self):
        print("500 - HP")

class Kia(Car):
    price = 900000

    def horse_powers(self):
        print("500 - HP")

nissan = Nissan(model = "GTR")
kia = Kia(model = "K5")
print(nissan)
nissan.horse_powers()
print(kia)
kia.horse_powers()


