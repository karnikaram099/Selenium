"""1. Write a program to find the length of the string without using inbuilt function (len)"""
# string = "hello world"
# c = 0
# for j in string:
#     c+=1
# print(c)

"""2. Write a program to reverse a string without using any inbuilt functions."""
# string = "hello world"
# rev = ""
# for i in string:
#     rev =i+rev
# print(rev)
# """with inbuilt method"""
# for i in reversed(string):
#     print(i, end = "")
"""3. Write a program to replace one string with another. 
e.g. "Hello World" replace "World" with "Universe"""
st = "hai good morning evryone"
a = st.replace("good", "Superr")
#print(a)

"""4. How to convert a string to a list and vice-versa"""
# st = "haihello how are you"
# print(list(st))
"""Series of prime number"""
num = 100
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

list_=[1,2,3,4, 3,3, 4]
b = list_.sort()
print(b)