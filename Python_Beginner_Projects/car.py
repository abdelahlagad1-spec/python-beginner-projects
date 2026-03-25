class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"{self.year} {self.make} {self.model} engine started")

    def stop_engine(self):
        print(f"{self.year} {self.make} {self.model} engine stopped")

car = Car("Toyota", "Camry", 2020)
car.start_engine()
car.stop_engine()
