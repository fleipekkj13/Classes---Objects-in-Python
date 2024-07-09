"""

    Starting with Objects & Classes in Python.

"""

class Veicle:
    def __init__(self, color, wheels, windows, doors):
        self.color = color
        self.wheels = wheels
        self.windows = windows
        self.doors = doors
    def showSpecifications(self):
        print(f"Your veicle is: {self.color}, has: {self.wheels} Wheels, {self.windows} Windows and {self.doors} Doors.")

class Car(Veicle):
    def __init__(self, name, color, wheels, windows, doors, brand, model):
        self.name = name
        self.brand = brand
        self.model = model
        super().__init__(color, wheels, windows, doors) #Call the __init__ method of Veicle object.
    
    def showMyCar(self):
        print(
            f"""
            Car name: {self.name}
            Car brand: {self.brand}
            Car model: {self.model}

            ---------- CAR SPECIFICATIONS ----------

            WHEELS: {self.wheels}
            WINDOWS: {self.windows}
            DOORS: {self.doors}
            
            COLOR: {self.color}

            """
        )

class Truck(Veicle):
    def __init__(self, color, wheels, windows, doors, weight, charges):
        self.weight = weight
        self.charges = charges
        super().__init__(color, wheels, windows, doors)

    def showMyTruck(self):
        print(
            f"""
            My Veicle is a Truck. 

            ----------- TRUCK SPECIFICATIONS -----------

            COLOR: {self.color}
            WHEELS: {self.wheels}
            WINDOWS: {self.windows}
            DOORS: {self.doors}

            ----------- VEICLE WEIGHT -----------

            THE TRUCK HAS: {self.weight}
            OTHER CHARGES: {self.charges}

            """
        )

myCar = Car('Ferrari', 'red', 4, 4, 2, 'Ferrari', 'Spider -> 458')
myCar.showMyCar()

myTruck = Truck('Blue', 12, 3, 2, 20000, 4)
myTruck.showMyTruck()