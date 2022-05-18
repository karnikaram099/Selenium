# """5. Covert the string "Hello welcome to Python" to a comma separated string."""
# # string = "hello welcome to python"
# # a = string.split()
# # c = ','.join(a)
# # print(c)
#
#
# """6. Write a program to print alternate characters in a string."""
# # string = "hello world"
# # print(string[::2])
#
# """7. Write a Program to print ascii values of the characters present in a string."""
# # string= "Avengers"
# # for i in string:
# #     print(ord(i))
#
# """8. Write program to convert upper case to lower case and vice-versa without using inbuilt method."""
# # st = "HaI EveRY One"
# # for i in st:
# #     if "a"<=i<="z":
# #         print(chr(ord(i)-32))
# #     elif "A"<=i<="Z":
# #         print(chr(ord(i)+32))
#
# """by using swapcase"""
# # st = "HaI EveRY One"
# # res = st.swapcase()
# # print(res)
# #
#
# """9. Write program to swap two numbers without using 3rd variable."""
# st = "HaI EveRY One"
# # res = st.swapcase()
# # print(res)
#
#
# """10. Write program to merge two different lists."""
# # a = [1,2,3]
# # b = [4,5,6]
# # #print(a+b)
# # c=[*a,*b]
# # print(c)
#
# """11. Write program to read a random line in a file. (ex. 50, 65, 78th line)"""
# path = r"C:\Users\karni\PycharmProjects\Alpha_3\file Handling\sample.txt"
# from itertools import islice
# n = 4
# with open(path) as f:
#     for index, item in enumerate(f):
#         if index==n:
#             print(index, item)


"""12. Write program to read a random lines in a file. (ex. I want read all lines 10th to 15th line)"""
#path = r"C:\Users\karni\PycharmProjects\Alpha_3\file Handling\sample.txt"
#
# """13 Program to print last "N" lines of a file."""
# from collections import deque
# path = r"C:\Users\karni\PycharmProjects\Alpha_3\file Handling\sample.txt"
# n = 3
# def demo(n):
#     with open(path) as file:
#         #for line in file:
#         s = deque(file, n)
#         return s
# last_10_lines = demo(5)
# for line in last_10_lines:
#     print(line)
"""14. Write a program to check if the given string is Palindrome or not without using reversed method."""
# st = "mom"
# res = ""
# for i in st:
#     res = res + i
# if res == st:
#     print("poli")
#
# else:
#     print("not a poli")


"""15 Write a program to search for a character in a given string and return the corresponding index.
"""
# string = "hai hello how are u"
# sub_string = "h"
# for index, item in enumerate(string):
#    if item == sub_string:
#        print(index, item)

"""16 Write a program to get the below output

sentence = "hello world welcome to python programming hi there"

d = {'h': ['hello', 'hi'], 'w': ['world', 'welcome'], 't': ['to', 'there'], 'p': ['python', 'programming'] }"""
# sentence = "hello world welcome to python programming hi there"
# from collections import defaultdict
# d = defaultdict(list)
# words = sentence.split()
# for word in words:
#     d[word[0]].append(word)
# print(d)

"""17 Write a program  to replace all the characters with - if the character occurs more than once in a string"""
string = "hello hai everyone"
# res = ""
# for item in string:
#     if item not in res:
#         print(item)
#     else:
#         print("-")
# new_string = ''.join(['-' if string.count(c) > 1 else c for c in string])
# print(new_string)
"""18 write a decorator that returns only positive values of subtraction"""
# def demo(func):
#     def wrapper(*args, **kwargs):
#         res = (func(*args, **kwargs))
#         return(abs(res))
#     return wrapper
# @demo
# def add(a, b):
#     return a+b
# print(add(3, -6))

"""19 How to get the count of number of instances of a class that is being created."""
# class login:
#     login_count=0
#     def __init__ (self):
#         login.login_count+=1
#
# u1 = login()
# login.login_count
# print(u1)
"""20 Write a function which takes a list of strings and integers.If the item is a string it should print as is and if the item is integer of float it should reverse it.
"""
# def rev_int(list_):
#     for item in list_:
#         if isinstance(item, str):
#             print(item)
#         else:
#             if isinstance(item, (int,float)):
#                 print (str(item[::-1]))
# (rev_int(["hai", "hello", 1, 2, 3, 4.3]))
#




"""21 Write a class named Simple and it should have iteration capability."""



"""22 Write a Custom class which can access the values of dictionaries using d['a'] and d.a"""



"""23 Write a python program to get the below output"""
"""sentence = "Hi How are you" 
o/p should be "iH woH era uoy"""
# sentence = "Hi How are you"
# for item in reversed(sentence[::-1]):
#     print(item, end="")

"""24 Write a python program to get the below output"""
"""sentence = "Hi How are you" 
o/p should be "ouy era woH iH"
"""
# sentence = "Hi How are you"
# for item in reversed(sentence):
#     print(item, end="")

"""25 Write a lambda function to add two numbers (a, b)"""
a=10
b = 20
res = lambda a, b:a+b
print((res(a, b)))

"""26 What is the output of the following"""

a = [1, 2, 3]
b = [4, 5, 6]
print([a, b])              #list(list)
print((a, b))              #(tuple(list))

"""27 How to remove duplicates from the list without using inbuilt functions
"""
items = [1, 2, 3, 4, 1, 2, 3, 4, 5]
set_ = set(items)
print(list(set_))
"""28 Find the longest word in the sentence
sentence = "Hello world. Welcome to Python"
"""
# sentence = "Hello world. Welcome to Python"
# s = sentence.split()
# d = {word: len(word) for word in s}
# res = max(d.items(), key = lambda item: item[-1])
# print(res)
#
# sentence = "hello world welcome to python"
# word = sentence.split()
# max_len = 0
# min_word=""
# for item in word:
#
# s= 1234
# sum = 0
# for i in range(s):
#     last = s%10
#     sum +=last
#     s=s//10
# print(sum)



# num = 1234530
# sum=0
# for i in range(num):
#     last_=num%10
#     sum+=last_
#     num = num//10
# print(sum)


#
# a  = (1, 2, 3, 4,5)
# c = 0
# for i in a:
#     c=c+1
#     print(c)


















