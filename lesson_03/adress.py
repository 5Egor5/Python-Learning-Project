class Address:
    def __init__(self, index, city, street, hause, flat):
        self.index = index
        self.city = city
        self.street = street
        self.hause = hause
        self.flat = flat

    def __str__(self):
        return f"{self.index}, " \
               f"{self.city}, " \
               f"{self.street}, " \
               f"{self.hause} - {self.flat}"
