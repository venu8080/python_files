class Car:
    def display_details(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year 
        print("class method (after assigning instance variables):")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
my_car = Car()
my_car.display_details("Porsche", "Model 2", 2025)
print("\n from outside the class:")
print(f"Make: {my_car.make}")
print(f"Model: {my_car.model}")
print(f"Year: {my_car.year}")
