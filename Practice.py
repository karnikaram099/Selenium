# """print 1 to 10 using for   loop"""
# # n = 10
# # for i in range(1, n+1):
# #     print(i)
# import re
#
# """print 10 to 1 using for loop"""
# # n = 10
# # for i in range(10, 0, -1):
# #     print(i)
#
#
# """print -10 to -1 using for loop"""
# # n = -10
# # for i in range(-1, -10-1, -1):
# #     print(i)
#
# """print even numbers using for loop"""
# # n = 30
# # for i in range(n):
# #     if i%2 == 0:
# #         print(i)
#
#
# """travers through string using for loop"""
# # a = "hello world"
# # res = ""
# # for char in a:
# #     res+=char
# # print(res)
#
# """traverse through list using for loop"""
# # list_=["hai", "hello", "python"]
# # for item in (list_):
# #     print(item, len(item))
#
# """To print index and charecter in a string"""
# # st = "hello hai everyone"
# # for index, item in enumerate(st):
# #     print(item, index)
#
# """traversing a string in reversed order"""
# # st = "hello world"
# # res = ""
# # for char in st:
# #     res=char+res
# # print(res)
#
#
# # """second method"""
# # st = "hello world"
# # for char in st[::-1]:
# #     print(char, end = "")
#
#
# """third method"""
# # st = "hello world"
# # for char in reversed(st):
# #     print(char, end = "")
#
#
# """count the number of charecters in a string"""
# # st = "hello world"
# # c = 0
# # for char in st:
# #     c+=1
# # print(c)
#
# """print even charecters in a string"""
# # st = "hai python"
# # for index, char in enumerate(st):
# #     if index%2==0:
# #         print(index, char)
#
# """to print the digits in a string using inbuilt method"""
# # st = "hello 123"
# # for i in st:
# #     if i.isdigit():
# #         print(i)
#
# """Without using inbuilt method"""
# # # st = "hello143"
# import re
# # #s = "hai123$@hello"
# # a = re.findall(r"\d+", "hai123$@hello")
# # print((a))
#
#
# #a = re.findall(r"am*b", "abmmmammmmb")
# b = re.findall(r"an+", "an")
# print(b)
#
#
#
# c = "HAI HEL HEL LO HOW are you STRING"
# # res = re.findall(r"\b[A-Z]{4}",c)
# # print(res)
# #
# # f_path = (r"C:\Users\karni\PycharmProjects\Alpha_3\files_directory\txt_log_files\access-log.txt")
# # with open(f_path) as file:
# #     l = []
# #     for line in file:
# #         if line.strip():
# #             list_=line.split()
# #             l.append(list_[0])
# #     print(l)
#
# """wap to get the only url of access-log text files"""
# # f_path=(r"C:\Users\karni\PycharmProjects\Alpha_3\files_directory\txt_log_files\access-log.txt")
# # with open(f_path)as file:
# #     l =[]
# #     for item in file:
# #         a= item.split()
# #         l.append(a[0])
# #         print(l)
# """create a dictionary ip address and its count"""
# f_path = (r"C:\Users\karni\PycharmProjects\Alpha_3\files_directory\txt_log_files\access-log.txt")
# # d = {}
# # with open(f_path)as file:
# #     for item in file:
# #         if item.strip():
# #             a = item.split()
# #             for i in a:
# #                 d[a[0]]= a.count(i)
# #     print(d)
# from collections import deque
# # n = 3
# # with open(f_path)as file:
# #     lines = deque(file, n)
# #     print(list(lines))
# import csv
# path = r"C:\Users\karni\PycharmProjects\Alpha_3\file handling 2\SAMMMM.txt"
# # with open(path, 'w')as file_write:
# # #         for line in file_write:
# # #             file_write.write(list(line))
# # with open(path,'w') as csv_file:
# #     csv_writer = csv.writer(csv_file)
# #     csv_writer.writerow(["hai helloo"])
# #
# #
# #
# # with open(path,'w') as csv_file:
# #     a = csv.DictWriter(csv_file, [w])
# #     a.writerow({"name":"Ram", "age": 22})
# import csv
# # path = r"C:\Users\karni\PycharmProjects\karnikaram099\File handling imp\FH-1"
# # with open(path,'w' )as csv_file:
# #     a = csv.writer(csv_file)
# #     a.writerow(["TheThe 29-year-old Mills, a T20 specialist who has represented England in 12 matches and has taken 11 wickets at a strike rate of 22.7, was bought for Rs 1.5 crore by the five-time champions as a replacement for Trent Boult. With Jofra Archer missing out, Mills is expected to play all the games for his team"])
# #
# #
#
#
#
#
#
# # num = 123
# # sum = 0
# # for i in range(num):
# #     last = num%10
# #     sum+=last
# #     num=num//10
# # print(sum)
# # def fact(n):
# #     if n ==0 or n==1:
# #         return 1
# #     return n*fact(n-1)
# # print(fact(4))
# # def sum(n):
# #     if n==1:
# #         return 1
# #     return n+sum(n-1)
# # print(sum(5))
# #
# #
# # string= "momaaa"
# # res = ""
# # for i in string:
# # #     res+=i
# # #     if res == string:
# # #         print("pali")
# # #         break
# # #     else:
# # #         print("not a poli")
# # #         break
# # #
# # #
# #
# # """for nth febo num"""
# # # def febo(n):
# # #     if n<0:
# # #         print("incorrect input")
# # #     elif n==0:
# # #         return 0
# # #     elif n == 1 or n == 2:
# # #         return 1
# # #     else:
# # #         return febo(n-1)+febo(n-2)
# # # print(febo(15))
# # #def fibo(n):
# # #     a = 0
# # #     b = 1
# # #     i = 0
# # #     while i<n:
# # #         print(a)
# # #         c = a+b
# # #         a=b
# # #         b = c
# # #         i+=1
# # # print(fibo(5))
# # """wap to check wether a num is armstrong or not"""
# # def arm_strong(num):
# #     temp = str(num)
# #     power = len(temp)
# #     total = 0
# #     for item in temp:
# #         total +=int(item)**power
# #     if total ==num:
# #         return(f"{num} is a armstrong")
# #     else:
# #         return(f"{num} is  not a armstrong num")
# # print(arm_strong(153))
# #
# # num = 153
# # temp = str(num)
# # power = len(temp)
# # total = 0
# # for item in temp:
# #     total +=int(item)**power
# #
# #
# #     if total ==num:
# #         print(f"{num} is a armstrong")
# #         break
# #     else:
# #         print(f"{num} is not a armstrong num")
# #         break
# #
# #
# #
# #
# #
# #
# #
# # s = "hai how are you"
# # ch ='h'
# # for i in range(len(s)):
# #     if i ==ch:
# #         print(s[i])
# #
# #
# #
# # """armstrong number"""
# # def armstrong(num):
# #     temp = str(num)
# #     power = len(temp)
# #     total = 0
# #     for item in temp:
# #         total +=int(item)**power
# #     if total==num:
# #         print(f'{num}, is an armstrong')
# #     else:
# #         print(f'{num}, is not an armstrong')
# # armstrong(153)
# #
# # s = "hai evryone"
# # print(s[:2])
# # print(s[2:])
# # from time import sleep
# # class __wait:
# # #     def wait(func):
# # #         def wrapper(*args, **kwargs):
# # #             res = func(*args, **kwargs)
# # #             sleep(5)
# # #             return res
# # #         return wrapper
# # #
# # class Praveen:
# #     def __init__(self, a= 10, b = 20):
# #         self.a = a
# #         self.b = b
# a = Praveen()
# # print(a.__dict__)
#
# def sam(num):
#     a = str(num)
#     for i in a:
#         return (int(i)**int(i))
#
#
# print((sam(56)))
#
# def sam(n):
#     s = " "
#     while n > 0:
#         n = n%10
#         s = str(n)+s
#         n//=10
#     print(int(s))
# sam(56)

#
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome("./chromedriver")
# driver.get("http://google.com/")
# driver.maximize_window()
# actions = ActionChains(driver)
# sleep(3)
# a1 = driver.find_element_by_xpath("//input[@title='Search']").send_keys("python")
# actions.double_click(a1)
# sleep(2)
# driver.find_element_by_xpath("//h3[text()='Welcome to Python.org']").click()
# ope1 = driver.find_element_by_xpath("(//a[text()='About'])[1]")
# actions.move_to_element(ope1).perform()
# sleep(2)
# ope2 = driver.find_element_by_xpath("(//a[text()='Quotes'])[1]").click()
# # actions.move_to_element(ope2).perform()
# driver.get_screenshot_as_file("Python Screnshot.png")
#
# abc = "Hai hello Evryone"
# for item in abc:
#     if "a"<=item<="z":
#         print(chr(ord(item)-32), end=" ")
#     else:
#         if "A"<=item<="Z":
#
#             print(chr(ord(item)+32), end="")
# a = 10
# b = 1
# c = 2
# if a>b and a>c:
#     print("a is greater")
# elif b>a and b>c:
#     print("b is greater")
# elif c>a and c>b:
#     print("c is greater")
"""print -10 to -1"""
#
# for i in range(-1, -11, -1):
#     print(i)
std =" hai hellooo @$123"
# c = len(std)
# for item in std:
#     if item.isdigit() or item.isalpha():
#         c-=1
# print(c, item)


string_ = r'kasi123@2332@&^%$'
count = len(string_)
for item in string_:
    if (item.isalpha()) or (item.isdigit()) :
            count -= 1
print(count)
