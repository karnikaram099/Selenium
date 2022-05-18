"""The process of hiding the data from the end user"""

from abc import ABC, abstractmethod
# class name(ABC):
#     @abstractmethod
#     def fname(self):
#         pass

# a2=name()

# class sam(name):
#     def fname(self):
# #         print("hai")
# a1 = sam()
# # print(a1.fname())
#
# class Car(ABC):
#     @abstractmethod
#     def speed(self):
#         pass
#
# class Tesla(Car):
#     def speed(self):
#         print("speed is 200Km per hour")
#
# class Renault(Car):
#     def speed(self):
#         print("Speed is 150km/hr")
#
#
# t = Tesla().speed()
# r = Renault().speed()
#

# class Car(ABC):
#     @abstractmethod
#     def Speed(self):
#         pass
#
#
# class Tesla(Car):
#     def Speed(self):
#         print("The car maximum speed is 250km/hr")
#
# class Renault(Car):
#     def Speed(self):
#         print("The car speed is 100km/hr")
#
# t = Tesla().Speed()
# r = Renault.Speed()


"""Abstraction method"""
from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def Speed(self):
        print("Car is a mechanical Machine")

class Tesla(Car):
    def Speed(self):
        print("car speed is 230km/hr")

class Skoda(Car):
    def Speed(self):
        print("Car speed is 90km/hr")


a = Tesla().Speed()
b = Skoda().Speed()
c = Car().Speed()
print(a)
print(b)
print(c)
















