"""print 1 to 10 using for   loop"""
# n = 10
# for i in range(1, n+1):
#     print(i)
import re

"""print 10 to 1 using for loop"""
# n = 10
# for i in range(10, 0, -1):
#     print(i)


"""print -10 to -1 using for loop"""
# n = -10
# for i in range(-1, -10-1, -1):
#     print(i)

"""print even numbers using for loop"""
# n = 30
# for i in range(n):
#     if i%2 == 0:
#         print(i)


"""travers through string using for loop"""
# a = "hello world"
# res = ""
# for char in a:
#     res+=char
# print(res)

"""traverse through list using for loop"""
# list_=["hai", "hello", "python"]
# for item in (list_):
#     print(item, len(item))

"""To print index and charecter in a string"""
# st = "hello hai everyone"
# for index, item in enumerate(st):
#     print(item, index)

"""traversing a string in reversed order"""
# st = "hello world"
# res = ""
# for char in st:
#     res=char+res
# print(res)


# """second method"""
# st = "hello world"
# for char in st[::-1]:
#     print(char, end = "")


"""third method"""
# st = "hello world"
# for char in reversed(st):
#     print(char, end = "")


"""count the number of charecters in a string"""
# st = "hello world"
# c = 0
# for char in st:
#     c+=1
# print(c)

"""print even charecters in a string"""
# st = "hai python"
# for index, char in enumerate(st):
#     if index%2==0:
#         print(index, char)

"""to print the digits in a string using inbuilt method"""
# st = "hello 123"
# for i in st:
#     if i.isdigit():
#         print(i)

"""Without using inbuilt method"""
# # st = "hello143"
import re
# #s = "hai123$@hello"
# a = re.findall(r"\d+", "hai123$@hello")
# print((a))


#a = re.findall(r"am*b", "abmmmammmmb")
b = re.findall(r"an+", "an")
print(b)



c = "HAI HEL HEL LO HOW are you STRING"
res = re.findall(r"\b[A-Z]{4}",c)
print(res)

