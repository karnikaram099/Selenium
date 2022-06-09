# class Parent:
#     def yahoo(self):
#         print("printing Parent class")
#
#
# class Child1(Parent):
#     def twitter(self):
#         print("printing child class")
#         super().yahoo()
#
#
# class Child2:
#     def Google(self):
#         print("Google is printing")
#
#
#
# class Child3(Child2, Child1):
#     def email(self):
#         print("email is printing")
#         super().Google()
#

# c = Child2()
# c.Google()

#
#
# """Encapsulation"""
# class Samantha:
#     s = 30
#     _d = 40
#     __f = 50
#
#
# obj = Samantha()
# print(obj.s)
# print(obj._d)
# print(dir(obj))
# print(obj._Samantha__f)


# from abc import ABC, abstractmethod
#
# class Car(ABC):
#     @abstractmethod
#     def speed(self):
#         print("car speed is 100km/hr")
#
#
# class Kia(Car):
#     def speed(self):
#         print("car speed is 150km/hr")
#
#
#
# class Tesla(Car):
#     def speed(self):
#         print("car speed is 300km/hr")
#
#
# obj = Tesla()
# obj.speed()
# obj1 = Kia()
# obj1.speed()
# obj2 = Car()
# obj2.speed()



class School:
    school_name = "Brindavan"

    def college(self, sname, srollnum):

        self.sname = sname
        self.srollnum = srollnum


# a= School()
# print(a.college())


class Student1(School):
    def fee(self, balance_fees):
        self.balance_fees = balance_fees
        #print(self.balance_fees)
        super().college(self)


class Student2(Student1):
    def fee(self, balance_fee):
        self.balance_fee= balance_fee
        super().fee(self)

obj = Student2()
obj.fee(5000)
print(School.school_name)


print(obj.__dict__)


