class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Details of Car: {self.year} {self.model}")

car1 = Car("Mclaren", 2022)
car2 = Car("Ferrari", 2012)
car1.display_details()
car2.display_details()
