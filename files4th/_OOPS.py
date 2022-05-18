# """Inheritence"""
#
# """
# It is a phenomenon of deriving the properties of one class to another class .in this process the property
#  which we inherit the proprty is called parent class or super class or basic class
#  and which we inherit the property is called child class.
#
#
#    or
#  it is a phenomenon of inhereting the properties of one class to another class..
#
#    """
#
#
# class Bank:
#     Bank_name = "SBI"
#     Bank_loc = "Bangalore"
#     Bank_IFSC = "SBIN00012907"
#     def __init__(self, name, phno, address):
#         self.name = name
#         self.address = address
#         self.phno = phno
# # a = Bank.Bank_IFSC
# # print(a)
# #c1 = Bank("Ram", 6281308839, "bangalore")
# # c2 = Bank("Madhuri", 7386543222, "Bangalore")
# # c3 = Bank("Priya", 9642095340, "Bangalore")
# # print(c1.name)
# # print(c3.address)
# #print(c1.__dict__)
#
# class Bank2(Bank):
#     def __init__(self, name, phno, address, Acno):
#         super().__init__(name, address, phno)
#         self.Acno = Acno
# #c4 = Bank2("Diwa,", "Kurnool", 8919467201, 33622609998)
# # # c5 = Bank2("Ramesh", "Gadekal", 9182391523, 3362260999999998)
# #print(c4.__dict__)
#
#
# class Bank3(Bank2):
#     def __init__(self, name, adress, phno, Acno, Loans, ATM):
#         super().__init__(name, adress, phno, Acno)
#         self.Loans = Loans
#         self.ATM = ATM
# c6 = Bank3("Diwa,", "Kurnool", 8919467201, 33622609998, 3.5, 5525)
# #print(c6.__dict__)
# # c7 = Bank
# # print(c7.__dict__)
#
# class Bank4(Bank3):
#     def __init__(self, name, address, phno, Acno, Loans, ATM, Insurence, Intrests):
#         super().__init__(name, address, phno, Acno, Loans, ATM)
#         self.Insurence = Insurence
#         self.Intrests = Intrests
#
# c8 = Bank4("THARUN", "Bangalore", 35345256,65568656,4686,584, 250, "Vehicle")
# #print(c8.__dict__)
#
#
# class Bank5(Bank, Bank2, Bank3):
#     def __init__(self,name, address, phno, Acno, Loans, ATM, Insurence, Intrests):
#         super().__init__(Bank, Bank2, Bank3)
# c9 = Bank5("THARUN", "Bangalore", 35345256,65568656,4686,584, 250, "Vehicle")
# #print(c9.__dict__)



"""Encapsulation"""
# class Tharun:
#     _a=10
#     _b=20
#     _c=30
#     def __init__(self, name, course):
#         self._name=name
#         self._course = course
#
# A=Tharun._a
# b =Tharun._b
# c = Tharun("Manoj", "Mech")
# print(c.__dict__)
#
# #print(c)
# print(b)

class Arun:
    __a=10
    __b=20
    def __init__(self, Name, Age, Branch):
        self.__name=Name
        self.__age=Age
        self.__branch=Branch
f = Arun("Anuj",27, "Mech")
print(f._Arun__age)
"""for accesing each and evry object in protected we need mention variable name._clsname__value name"""
print(f.__dict__)   #{'_Arun__name': 'Anuj', '_Arun__age': 27, '_Arun__branch': 'Mech'}










