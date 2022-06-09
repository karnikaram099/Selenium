# (add(7, 4))"""1. Write a program to find the length of the string without using inbuilt function (len)"""
# string = "hello world"
# # c = 0
# # for j in string:
# #     c+=1
# # print(c)
#
# """2. Write a program to reverse a string without using any inbuilt functions."""
# # string = "hello world"
# # rev = ""
# # for i in string:
# #     rev =i+rev
# # print(rev)
# # """with inbuilt method"""
# # for i in reversed(string):
# #     print(i, end = "")
# """3. Write a program to replace one string with another.
# e.g. "Hello World" replace "World" with "Universe"""
# st = "hai good morning evryone"
# a = st.replace("good", "Superr")
# #print(a)
#
# """4. How to convert a string to a list and vice-versa"""
# # st = "haihello how are you"
# # print(list(st))
# """Series of prime number"""
# num = 100
# for num in range(2, num):
#     for i in range(2, num):
#         if num % i ==0:
# #             #print(f"{num} is not a prime")
# #     else:
# # #        print(f"{num} is a prime num")
#
#
# """checking a number wether its prime or not"""
# num = 13
# for i in range(2, num):
#     if num%i ==0:
#         #print(f"{num} is not a prime")
#         break
#     else:
#         #print(f"{num} is prime")
#         break
# """febonicii """
# num = 5
# a = 0
# b = 1
# i = 0
# while i<num:
#     #print(a)
#     c = a+b
#     a=b
#     b = c
#
#
# """factorial number"""
# # def fact(num):
# #     if num==0 or num ==1:
# #         return 1
# #     else:
# #         return num* fact(num-1)
# # print(fact(4))
# #
# #
# #def fact(n):
# #     if n ==0 or n==1:
# #         return 1
# #     return n*fact(n-1)
# # print(fact(4))
# #
# # """wap to check wether a number is armstrong or not"""
# # num = int(input("enter the num "))
# # sum = 0
# # temp = num
# # while temp>0:
# #     digit = temp%10
# #     sum+=digit**3
# #     temp//=10
# #     if num == sum:
# #         print("num is armstrong")
# #     else:
# #         print("num is not a armstrong num")
# #
#
#
# s= 1234
# sum = 0
# for i in range(s):
#     last = s%10
#     sum +=last
#     s=s//10
# print(sum)
#
# a = [1, 2,3]
# b =delattr(a)
# print(b)
# data = "₹50000/-"
# # res = ""
# # b = 3000
# # for i in data:
# #     if "0"<=i<="9":
# #         res+=i
# #         c = int(res)
# # print(int(c)+int(b))
# string = "Test Yantra"
#
#
# for i  in data:
#     if '0' <= i <= '9':
#         print(int(i) + 20)

# row = 5
# # a = row - 1
# # b = 7
# # for i in range(0, row):
# #     for j in range(0, a):
# #
# #         print(" ", end=" ")
# #
# # for j in range(1, row):
# #     print(" " * j, "*" * b)
# #     b -= 2
#
# # rows = 5
# # k = 2 * rows - 2
# # for i in range(0, rows):
# #     for j in range(0, k):
# #         print(end=" ")
# #     k = k - 1
# #     for j in range(0, i + 1):
# #         print("* ", end="")
# # #     print("")
# # class Sample:
# #     def __init__(self, c, b):
# #         self.a= c
# #         self.b = b
#
# def Sampleeee(*args, **kwargs):
#     print(len(f'{Sampleeee.__name__}'))
# Sampleeee()
#
# st = "Sonyindia"
# a1 = (st[-5:len(st)])
# a2 = (st[-2:len(st)])
#
# st = "Automation test engineer"
# res = ""
# half = len(st)/2
# print(half)
#
# name = "sharath"
# print(name[3:-2])
#
#
# d = {"a":10, "b":{"h":"hello", "e":15, "d":[10, 20, 30]},"e":11}
# print(d["b"]["d"][2])
# """wap to create a dictionary with word and its count pair"""
# word = "Wee all are employees of testyantra and testyantra is a Software Company"
# d = {}
# s = word.split()
# # for item in s:
# #     if s.count(item)>1:
# #         d[item]=s.count(item)
# # print(d)
# from collections import defaultdict
# d1 = defaultdict(int)
# for item in s:
#     if s.count(item)>1:
#         d1[item] =s.count(item)
# print(d1)
#
# """wap to create a dictonary with word and its count pair only if the word is starting with vowel"""
# word = "Wee all are employees of testyantra and testyantra is a Software Company"
# d = {}
# s = word.split()
# for item in s:
#     if item[0].lower() in "aeiou":
#         d[item]=len(item)
# print((d))

# list_=["hello", "hai", "owh"]
# word = list_[0]
# for letter in word:
#     a = [letter in i for i in list_[1:]]
#     if all(a):
#         print(letter)
#
#
#
# data = {"fruit": ['appele', 'banana', 'orange'], 'subject':['phy', 'math', 'English']}
# print(len(data["fruit"]))
# data["subject"]+=["biology"]
# print(data["subject"])
# data["animal"] = ["dog", "cat"]
#
# print(data)
#
#
# country = ['India', 'Germany', 'Italy']
# dog = ['Labrodor' 'german', 'pug']
# age = [1, 5, 10]
#
#
# import xlrd
#
# wb = xlrd.open_workbook(r"C:\Users\karni\OneDrive\Desktop\Sample_Practice1.xlsx")
# ws = wb.sheet_by_name("Practice")

# l = [0, 0, 0]
# l1 = [1, 1, 1]
# l2 = []
#
# for i in range(len(l)):
#     l2.append(l[i])
# #     l2.append(l1[i])
# # print(l2)
# from collections import defaultdict
# st = "Sharath is an Information tchnology employee"
# s = st.split()
# # d1 = {key:len(value) for key,value in enumerate(s)}
# # print(d1)
# # d = defaultdict(int)
# # d1 = {}
# # for item in s:
# #     d1[item]= len(item)
# print(d1)
# d1 = {}
# for item in (s):
#     d1[item] = len(sorted(item))
# print(d1)
# """wap to create a dictionary with word and its count pair"""
# # st = "Sharath is an Information tchnology employee is an"
# # s = st.split()
# # d1 = {}
# # for word in s:
# #     if word not in d1:
# #         d1[word] = s.count(word)
# # print(d1)



#
# def sam(func):
#     def wrapper(*args, **kwargs):
#         print("Deco func  is Executing")
#         return func(*args, **kwargs)
#     return wrapper
#
# @sam
# def add(a, b):
#     return a+b
# print(add(1, 6))

# st = "Hai hello"
# # for item in range(len(st)-1, -3,-1):
# #     print(st[item], end="")
# for item in reversed(st):
#     print(item)
#
# def sam(num):
#     rev = ""
#     while num != last:
#         last = num%10
#         rev += last
#         num = num//10
#     print(rev)
# sam(69)
# s= 1234
# sum = 0
# for i in range(s):
#     last = s%10
#     sum =sum*10+last
#     s=s//10
# print(sum)
#
# from selenium import webdriver
# from time import sleep
# driver=webdriver.Chrome("./chromedriver")
# driver.get("https://www.monsterindia.com/")
# from selenium.webdriver.common.action_chains import ActionChains
# actions = ActionChains(driver)
# ele = driver.find_element_by_xpath("//a[text()='Job search']")
# actions.move_to_element(ele).perform()
#
# ele1 = driver.find_element_by_xpath("//a[text()='Jobs by Education']")
# actions.move_to_element(ele1).perform()
# sleep(10)
# ele2 = driver.find_element_by_xpath("//a[contains(text(),'B Tech Jobs')]")
# sleep(5)
# ele2.click()





