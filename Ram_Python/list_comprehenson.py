# """list comperehension is an elgant way to define and create list..... Based on existing lists"""
# """    syntax  =  expression for item in list    """
# """wap to ctreate a list of even numbers from the below list"""
# list_=[10, 2, 45, 67, 78, 9, 8, 65]
# res = [item for item in list_ if item%2==0]
# print(res)
#
# """wap to create 2 lists evens and odds"""
# list1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = [item for item in list1 if item%2==0]
# odds=[item for item in list1 if item%2!=0]
# print(evens)
# print(odds)
# """wap to craete a list using the following list of the word is of even length store the word
# asitis else reverse the word and store"""
# list2=["python", "java", "c++", "jango"]
# res = [str(item) if len(item)%2==0 else str(item[::-1]) for item in list2]
# print(res)
# # for i in list2:
# #     if len(i)%2==0:
# #         print(i)
# #     else:
# #         print(i[::-1])
#
#
# # l =[i if len(i1`)%2==0 else i[::-1] for i in list2]
# # print(l)
#
#
# """print entire sum and internal sum of list"""
#
# # list_=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # entire_sum = 0
# # for item in list_:
# #     internal_sum = 0
# #     for i in item:
# #         entire_sum+=i
# #         internal_sum+=i
# #     print(internal_sum)
# # print(entire_sum)
#
# """print entire sum of list"""
# l=[[1, 2, 3], [4, 5, 6], [7, 8, 9], 5]
# sum=0
# for item in l:
#     if not isinstance(item, int):
#         for i in item:
#             sum+=i
#     else:
#         sum+=item
# # print(sum)
#
# """reverse the list"""
# l = ["hi", "hello", "python"]
# # print(l[::-1])
#
# l = ["hi", "hello", "python"]
# res = []
#
# for item in l[::-1]:
#     res.append(item[::-1])
#
# # print(res)
# """ remove all the duplicate elements """
# l = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
# s = (set(l))
# # print(list(s))
#
# """ WAP to create a list of squares for the elements in the below list"""
# list_=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "hai", "hello"]
# res = [i*i for i in list_ if isinstance(i, int)]
# # print(res)
# res2=[]
# for item in list_:
#     if isinstance(item, int):
#         res2.append(item * item)
# # print(res2)
#
# """ create list of tuples of index and its corresponding item in the list """
# list_=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "hai", "hello"]
# l=[]
# for item in enumerate(list_):
#     l.append(item)
# # print(l)
#
#
# res = [item for item in enumerate (list_)]
# # print(res)
#
# """ list of even numbers """
# list_=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "hai", "hello"]
# l1=[]
# for item in list_:
#     if isinstance(item, int):
#         if item%2==0:
#             l1.append(item)
# # print(l1)
# res = [item for item in list_ if isinstance(item, int) if (item)%2 == 0]
# # print(res)
#
# """ list of even and odd """
# list_=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "hai", "hello"]
# evens = []
# odds = []
# for item in list_:
#     if isinstance(item, int):
#         if item%2 == 0:
#             evens.append(item)
#         else:
#             if isinstance(item, int):
#                 if(item)%2!=0:
#                     odds.append(item)
#
# # print(evens)
# # print(odds)
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
# print(sum)
#
#
# """ set of tuples with index and item """
# list_ = ["Java", "Python", 10, True, 1.4, "c++", "ruby"]
# res4 = {(index, item) for index, item in enumerate(list_)}
# print(res4)
#

# list1 = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]
# entire_sum = 0
# for item in list1:
#     # if not isinstance(list_, int):
#         internal_sum = 0
#         for i in item:
#             entire_sum+=i
#             internal_sum+=i
#         print(internal_sum)
# print(entire_sum)
#
#
# s  = 1234
# a = str(s)
# out = ""
# for item in a:
#     out = (item)+out
# print(out)

# for item in reversed(a):
#     print(item, end ="")

# print(1234%10)
# import sys

# n = 0
# for item in range(s):
#     last = s % 10
#     out+= str(last)
#     s = s//10
#     n+=1
#     if n == len(s):
#
# print(out)
# print(s%10)


# print("%%")

# s = "HB123&Hb&&67887&&92"
# for item in s:
#     try:
#        if isinstance(int(item), int):
#            print(item, end='')
#     except (TypeError, ValueError):
#         pass

# s = "HB123&Hb&&67887&&92"

# for item in s:
#     if "0" <= item <= "9":
#         print(item, end="-")


# import re
# res = re.findall(r"\d", s)
# print(res)

# for i in s:
#     if i.isdigit():
#         print(i,end ="")


""" WAP to create a list of squares for the elements in the below list"""
# l = [1,2,3,4]
# l1 = [i**2 for i in l ]
# print(l1)


""" create list of tuples of index and its corresponding item in the list """


# l = [90,30,40,20]
# l2 =[(index,item) for index,item in enumerate(l)]
# print(l2)


""" list of even numbers """
# l = [3,1,4,6]
# l1 = [i for i in l if i%2==0]
# print(l1)

li = [1, 2, 3, 45, 65, 99, 3, 4, 5, 67]
a = (sorted(li))
# print(a(sum[-3]))

def samantha():
    print()