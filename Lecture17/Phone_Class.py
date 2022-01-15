class Phone:
    def __init__(self,
                 model = "",
                 manufacturer = None,
                 price = None,
                 owner = None,
                 battery = None,
                 screen = None
                 ):
        self.model = model
        self.manufacturer = manufacturer
        self.price = price
        self.owner = owner
        self. battery = battery
        self.screen = screen

    def print_properties(self):
        return self.model, self.manufacturer

nokia1 = Phone("N95","Nokia",owner = "Mitko")
print(Phone.print_properties(nokia1))