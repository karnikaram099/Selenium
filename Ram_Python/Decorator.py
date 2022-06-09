# # def sample(func):
# #     def wrapper (*args, **kwargs):
# #         res = func(*args, **kwargs)
# #         return abs(res)
# #     return wrapper
#
#
# a = (10, 20)
# def sam(func):
#     def wrapper(*args,**kwargs):
#         res = func(*args, **kwargs)
#         return abs(res)
#     return wrapper
#
# @sam
# def add(a, b):
#     return a+b
#
# print(add(10,-20))
#
# def demo(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         if isinstance(res, str):
#             return res[::-1]
#     return wrapper
#
# @demo
# def demo1(string):
#     return string
#
# print(demo1("HAi"))


def sam(func):                   #------------> 1st
    def wrapper(*args, **kwargs):#------------>4th
        print("Deco func  is Executing")# ------->7th One
        return func(*args, **kwargs) #8th
    return wrapper#--------->5th(return wrapper is having the address of add function)

@sam#----------->2nd       ###add = sam(add)###3
def add(a, b):
    return a+b #9th
print(add(1, 6))#-------------->6th calling add function









