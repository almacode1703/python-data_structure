class Car:

    # class attribute
    category = "vehicle"

    # instance attribute
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year


# instantiate the Car class
mercedes = Car("Mercedes", 2022)
toyota = Car("Toyota", 2020)

# access the class attributes
print("Mercedes is a {}".format(mercedes.category))
print("Toyota is also a {}".format(toyota.category))

# access the instance attributes
print("{} was manufactured in {}".format(mercedes.brand, mercedes.year))
print("{} was manufactured in {}".format(toyota.brand, toyota.year))