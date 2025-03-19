"""
3. Write a class called Converter. The user will pass a length and a unit when declaring an 
object from the class—for example, c = Converter(9,'inches'). The possible units are inches
, feet, yards, miles, kilometers, meters, centimeters, and millimeters. For each of these 
units there should be a method that returns the length converted into those units. For 
example, using the Converter object created above, the user could call c.feet() and should
get 0.75 as the result.
"""

class Converter:
    conversion_rates = {
        'inches': 1,
        'feet': 1 / 12,
        'yards': 1 / 36,
        'miles': 1 / 63360,
        'kilometers': 1 / 39370,
        'meters': 1 / 39.37,
        'centimeters': 1 / 0.3937,
        'millimeters': 1 / 0.03937
    }

    def __init__(self, length, unit):
        if unit not in self.conversion_rates:
            raise ValueError("Invalid unit. Choose from inches, feet, yards, miles, kilometers, meters, centimeters, millimeters.")
        self.length = length
        self.unit = unit

    def convert_to(self, target_unit):
        if target_unit not in self.conversion_rates:
            raise ValueError("Invalid target unit.")
        base_length = self.length / self.conversion_rates[self.unit]
        return base_length * self.conversion_rates[target_unit]

    def display_conversions(self):
        print(f"{self.length} {self.unit} is equal to:")
        for unit in self.conversion_rates:
            if unit != self.unit:
                print(f"{self.convert_to(unit):.4f} {unit}")

def converter_menu():
    length = float(input("Enter the length: "))
    unit = input("Enter the unit (inches, feet, yards, miles, kilometers, meters, centimeters, millimeters): ").lower()
    try:
        converter = Converter(length, unit)
        converter.display_conversions()
    except ValueError as e:
        print(e)

converter_menu()
