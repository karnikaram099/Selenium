"""print entire sum and internal sum of list"""

# list_=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# entire_sum = 0
# for item in list_:
#     internal_sum = 0
#     for i in item:
#         entire_sum+=i
#         internal_sum+=i
#     print(internal_sum)
# print(entire_sum)

"""print entire sum of list"""
# evens = [item for item in list_ if isinstance(item, int) if (item)%2 == 0]
# # print(evens)
# evens = [item for item in list_ if isinstance(item, int) if (item)%2 != 0]
# # print(odds)
#
#
# """ if even store as it is else reverse and store it """
# l = ["python", "Node JS", "selenium", "Java", "c++"]
# l1 = []
# for item in l:
#     if isinstance(item ,str):
#         if len(item)%2 ==0:
#             l1.append(item)
#         else:
#             l1.append(item[::-1])
#
# # print(l1)
# # l=[[1, 2, 3], [4, 5, 6], [7, 8, 9], 5]
# # sum=0
# # for item in l:
# #     if not isinstance(item, int):
# #         for i in item:
# #             sum+=i
# #     else:
# #         sum+=item
# # # print(sum)
# #
# # """reverse the list"""
# # l = ["hi", "hello", "python"]
# # # print(l[::-1])
# #
# # l = ["hi", "hello", "python"]
# # res = []
# #
# # for item in l[::-1]:
# #     res.append(item[::-1])
# #
# # # print(res)
# # """ remove all the duplicate elements """
# # l = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
# # s = (set(l))
# # # print(list(s))
# #
# # """ WAP to create a list of squares for the elements in the below list"""
# # list_=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "hai", "hello"]
# # res = [i*i for i in list_ if isinstance(i, int)]
# # # print(res)
# # res2=[]
# # for item in list_:
# #     if isinstance(item, int):
# #         res2.append(item * item)
# # # print(res2)
# #
# # """ create list of tuples of index and its corresponding item in the list """
# # list_=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "hai", "hello"]
# # l=[]
# # for item in enumerate(list_):
# #     l.append(item)
# # # print(l)
# #
# #
# # res = [item for item in enumerate (list_)]
# # # print(res)
# #
# # """ list of even numbers """
# # list_=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "hai", "hello"]
# # l1=[]
# # for item in list_:
# #     if isinstance(item, int):
# #         if item%2==0:
# #             l1.append(item)
# # # print(l1)
# # res = [item for item in list_ if isinstance(item, int) if (item)%2 == 0]
# # # print(res)
# #
# # """ list of even and odd """
# # list_=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "hai", "hello"]
# # evens = []
# # odds = []
# # for item in list_:
# #     if isinstance(item, int):
# #         if item%2 == 0:
# #             evens.append(item)
# #         else:
# #             if isinstance(item, int):
# #                 if(item)%2!=0:
# #                     odds.append(item)
# #
# # # print(evens)
# # # print(odds)
#
# res = [item if len(item) % 2 == 0 else item[::-1] for item in l]
# # print(res)
#
#
# """ reverse if it is a string else keep it as it is """
# list_ = ["Java", "Python", 10, True, 1.4, "c++", "ruby"]
#
#
# res2 = [item[::-1] if isinstance(item, str) else item for item in list_]
# # print(res2)
# l1 = []
# for item in list_:
#     if isinstance(item, str):
#         l1.append(item[::-1])
#     else:
#         l1.append(item)
# # print(l1)
#
# """ list of words starting with vowel """
# files = ["Amazon", "flipkart", "walmart", "gmail", "yahoo"]
# res3 = [item for item in files if item[0].lower() in "aeiou"]
# # print(res3)
# l1=[]
# for item in files:
#     if item[0].lower() in "aeiou":
#         l1.append(item)
#         print(item)
#
#
# """print entire sum and internal sum of list"""
# list1 = [[1, 2, 3,], [4, 5, 6], [7, 8, 9], 99]
# sum = 0
# for item in list1:
#     if not isinstance(item, int):
#         for i in item:
#             sum+=i
#     else:
#         sum+=item
# # print(sum)
#
#
# """ set of tuples with index and item """
# list_ = ["Java", "Python", 10, True, 1.4, "c++", "ruby"]
# res4 = {(index, item) for index, item in enumerate(list_)}
# # print(res4)
#
#
# """ WAP to create a dictionary with item and its index pair"""
#
#
# """fibonaciii"""
# # def fibo(num):
# #     a = 0
# #     b = 1
# #     while a<=num:
# #         print(a)
# #         c = a+b
# #         a = b
# #         b = c
# # fibo(14)
#
# # def fibonacii(num):
# #     a = 0
# #     b = 1
# #     i = 0
# #     while i <= num:
# #         print(a)
# #         c = a+b
# #         a = b
# #         b = c
# #         i += 1
# # fibonacii(14)
# #"""fibonacii"""
#
#
# # def fibonacii(num):
# #     first = 0
# #     second = 1
# #     i = 0
# #     while i <= num:
# #         # print(first, end = '  ')
# #         sum = first+second
# #         first = second
# #         second = sum
# #         i += 1
# # fibonacii(15)
#
# """Series of fibonacii"""
# def fibonacii(number):
#     first = 0
#     second = 1
#     while first <= number:
#         # print(first, end = "   ")
#         sum = first+second
#         first=second
#         second=sum
# fibonacii(21)
# #
# # from turtle import *
# # speed(2)
# # bgcolor()
# # penup()
# # goto(-50, 60)
# # pendown()
# # color("#00adef")
# # begin_fill()
# # goto(100, 100)
# # goto(100, -100)
# # goto(-50, -60)
# # goto(-50, 60)
# # end_fill()
# # color("black")
# # goto(15, 100)
# # color("black")
# # width(10)
# # goto(15, -75)
# # penup()
# # goto(100, 0)
# # pendown()
# # goto(-100, 0)
# # done()
#
#
# # # for row in range(1, 5):
# # #     print(f'{"* "* row:^8}')
# # def sam():
# #     for i in range(1, 10):
# #         yield i
# # a = sam()
# #
# # # print((list(a)))
# #
# #
# # # a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # # s = iter(a)
# # # print(s)
# # # c = next(s)
# # # print(c)
# # # d = next(s)
# # # print(d)
# #
# #
# # n=[1,2,3]
# # s=iter(n)
# # print(s)
# # b=next(s)
# # print(b)
# #
# # def Armstrong_num(num):
# #     temp = str(num)
# #     power = len(temp)
# #     total = 0
# #     for item in temp:
# #         total+= int(item)**power
# #
# #     if total == num:
# #         print(f'{num} is armstrong')
# #     else:
# #         print(f'{num} is not armstrong')
# # Armstrong_num(159)
# #
# #
# # def fibonacii(num):
# #     first = 0
# #     second = 1
# #     i = 0
# #     while first<num:
# #         print(first)
# #         sum = first+second
# #         first = second
# #         second = sum
# #         # i+=1
# #
# # fibonacii(12)
#
# # num = 12356
# # sum = 0
# # for i in range(num):
# #     last = num%10
# #     sum+=last
# #     num = num//10
# # # print(sum)
# # # add = lambda a, b:a+b
# # # print(add(2,7))
# # a = 20
# # def spam():
# #     global a
# #     a = a+10
# #     print(a)
# # spam()
# # class Circle:
# #     def __init__(self, radius):
# #         self.radius = radius
# #     @property
# #     def radius(self):
# #         return self._radius
# #     @radius.setter
# #     def radius(self, value):
# #         if not isinstance(value, int):
# #             raise TypeError()
# #         self._radius=value
# #     def Circumference(self):
# #         return self._radius * 3.14*2
# #
# #
# # print(Circle.Circumference())
#
# with open("demo.html", "r") as file_read, open("demo1.docx", "w") as file_write:
#     for line in file_read:
#         file_write.write(line)












