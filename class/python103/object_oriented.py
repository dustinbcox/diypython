"""This is a intro to creating a class with inheritance"""
from __future__ import print_function

class Car(object):
    """Base class"""
    ALL_CARS_HAVE_THIS = 'wheels'

    def __init__(self, color = 'unknown'):
        """Something here"""
        self.color = color

    def make(self):
        """Returns the make of the car"""
        return ""

    def drive(self):
        """Do the driving thing"""
        return "Driving"

    def what_do_all_cars_have(self):
        # return Car.ALL_CARS_HAVE_THIS
        return self.ALL_CARS_HAVE_THIS


class Ford(Car):
    """This handles Ford cars"""

    def make(self):
        return 'Ford'

    def drive(self):
        """Do special type of driving"""
        type_of_driving = super(Ford, self).drive() + "Fast"
        return type_of_driving
        
        



if __name__ == "__main__":
    parking_lot = []

    my_car = Car('red')
    parking_lot.append(my_car)

    another_car = Car('black')
    parking_lot.append(another_car)

    ford_car = Ford('yellow')
    parking_lot.append(ford_car)

    for that_car in parking_lot:
        print ("That car's color is:", that_car.color, "and it is a ", that_car.make())
        print ("What do all cars have:", that_car.what_do_all_cars_have())
        print ("Let's go for a drive:", that_car.drive())
        


