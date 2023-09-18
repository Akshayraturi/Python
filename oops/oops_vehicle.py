class Vehicle:
        def __init__(self):
                self.driver=1
                self.engine=1
        def type(self,vehicle):
                     print("**The type of vehicle is ",vehicle,"**") 
        def car(self,tyre,category,brand,colour):
                print("**The car has:",tyre,"tyre")
                print("**The car is of: ",brand,"brand")
                print("**The car's colour is:",colour)
                print("**The car has:",category,"type")
        def cycle(self,tyre,category,brand,colour):
                print("**The cycle has:",tyre,"tyre")
                print("**The cycle is of: ",brand,"brand")
                print("**The cycle has:",category,"type")
                print("**The cycle's colour is:",colour)
        def boat(self,tyre,category,brand,colour):
                print("**The boat has:",tyre,"tyre")
                print("**The boat is of: ",brand,"brand")
                print("**The boat has:",category,"type")
                print("**The boat colour is:",colour)
        def aeroplane(self,tyre,category,brand,colour):
                print("**The aeroplane has:",tyre,"tyre")
                print("**The aeroplane  is of: ",brand,"brand")
                print("**The aeroplane  has:",category,"type")
                print("**The aeroplane  colour is:",colour)
                  
        def method(self):
                print("**The vehicle has ",self.driver,"driver**")
                print("**The vehicle has ",self.engine,"engine**")
     
                          
obj=Vehicle()
obj.type("car")
car=Vehicle()
car.car(4,"land",str(input("enter the brand of the car")),str(input("enter the colour of the car")))
obj.method()
cycle=Vehicle()
cycle.cycle(2,"land",str(input("enter the brand of the cycle")),str(input("enter the colour of the cycle")))
obj.method()
boat=Vehicle()
boat.boat(2,"water",str(input("enter the brand of the  boat")),str(input("enter the colour boat")))
obj.method()
aeroplane=Vehicle()
aeroplane.aeroplane(2,"air",str(input("enter the brand of aeroplane")),str(input("enter the colour aeroplane")))
obj.method()