

class Car:
     def __init__(self,brand):
      self.brand =brand

     def Start(self):
         print(f"{self.brand} is starting")

my_car= Car("Toyota")
print(f"my_car.brand")
my_car.Start()