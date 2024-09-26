# defining class
class Smartphone:
    # constructor
    def __init__(self, device, brand, price):
        self.device = device
        self.brand = brand
        self.price = price

    # method of the class
    def description(self):
        return f"{self.device} of {self.brand} supports Android 14"


# creating object of the class
phoneObj = Smartphone("Smartphone", "Samsung", 57000)
print(phoneObj.description())

