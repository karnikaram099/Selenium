# """wait decorator"""
# from time import sleep
# import time
# def sam(func):
#     def wrapper (*args, **kwargs):
#         start = time.time()
#         sleep(7)
#         func(*args, **kwargs)
#         end = time.time()
#         print (end-start)
#     return wrapper
# @sam
# def demo(a,b):
#     return (a*b)
# print(demo(2, -3))
#
# """Positive Decorator"""
#
#
# def positive(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         if isinstance(res,(int,float)):
#             return abs(res)
#         return res
#     return wrapper
#
#
# @positive
# def mul(a,b):
#     return a+b
# print(mul(2,-6))
#
#
from time import sleep

def wait(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        sleep(5)
        return res
    return wrapper


