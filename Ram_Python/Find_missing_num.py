# # l = [1, 2, 3, 4, 5, 6, 9, 10]
# # for item in range(1, len(l)):
# #     if item in l:
# #         pass
# #     else:
# #         print(item)
#
#
s= 1234
sum = 0
for i in range(s):
    last = s%10
    sum +=last
    s=s//10
print(sum)
#
#
# from num2words import num2words
# print(num2words(3625))
#
# #
# # """prime num"""
# # for num in range(100):
# #     if num>1:
# #         for i in range(2, num):
# #             if num%i==0:
# #                 break
# #             else:
# #                 print(f"{'num is prime'}",num)
# #                 break
#
# """prime"""
# num = 12
# for i in range(2, num):
#     if num%i == 0:
#         print("not a prime")
#         break
#     else:
#         print(num)
#         break
#
#
# """perfect number or not"""
# num = 6
# i = 1
# sum = 0
# while i < num:
#     if num%i == 0:
#         sum = sum+i
#     i+=1
# if num == sum:
#     print(num, "is perfect ")
#
# else:
#     print("num is not perfect")
