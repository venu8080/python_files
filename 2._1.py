class car:
    """Class to repersent a car"""
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price

        #method to display car details
        def show_details(self):
            print(f"Car Brand: {self.brand}")
            print(f"Car Model: {self.model}")
            print(f"Car price: {self.price}")
            #Create object of car
            my_car = Car("tesla","Model X",90000000)
            my_car = Car("swift","Model Y",300000)
            car3=Car("nano","Model Z",10000000)

            
            my_car.show_details()
            my_car.show_details()
            car3.show_details()
            
            

