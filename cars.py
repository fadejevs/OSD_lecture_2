class Car:
    def __init__(self, name, license_plate, color, fuel_type):
        self.name = name
        self.license_plate = license_plate
        self.color = color
        self.fuel_type = fuel_type

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"License Plate: {self.license_plate}")
        print(f"Color: {self.color}")
        print(f"Fuel Type: {self.fuel_type}")
        print()


cars = [
    Car("Fiat", "DEJ112", "White", "Diesel"),
    Car("Honda", "XYZ226", "Red", "Diesel"),
    Car("Ferrari", "EMPTYBNK", "Gray", "Petrol"),
]

for car in cars:
    car.display_info()
