# for i in range(5):
#     print("* " * i)
#
# # print()
# """
# * * * *
#   * * *
#     * *
#       *
# # """
# # for i in range(4, 0, -1):
# #     print(f'{"* "* i:>8}')
# #
# #
# # for i in range(5):
# #     print(f"{'* '*i :^8}")
# #
#
# # for i in range(4, 0, -1):
# #     print(f'{"* "*i:^8}')
#
#
# """
#      a
#     b c
#    d e f
#   g h i j
# """
#
# #
# # for row in range(ord("a"), ord("j")):
# #     for col in range(ord("a"), row+1):
# #         # print(chr(col), end = " ")
# #         print(f'{chr(col) * col:^8}')
# #
# #     print()
#
#
# # for row in range(5):
# #     for col in range(ord("a"), row+1):
# #         print(chr(col))
# #     print()
# #
#
# # def positive(func):
# #     def wrapper(*args, **kwargs):
# #         res = func(*args, **kwargs)
# #         if isinstance(res, (int, float)):
# #             return abs(res)
# #         return res
# #     return wrapper
# #
# #
# #
# # @positive
# # def add(a, b):
# #     return a+b
# # print(add(2, 5))
#
#
# """1 0 1 0 1
#    1 0 1 0 1
#    1 0 1 0 1
#    1 0 1 0 1"""
# for _ in range(4):
#     for i in range(1, 6):
#         print(i%2, ' ',end="")
#     print()
#
#
# def  armstrong_num(num):
#     temp=str(num)
#     power=len(temp)
#     total=0
#     for item in temp:
#         total+=int(item)**power
#     if total==num:
#         return "num is an armstrong"
#     return "num is not an armstrong"
# print(armstrong_num(421))
#
#
# """fibonacii series"""
# def fibo(num):
#     a = 0
#     b = 1
#     while a<=num:
#         print(a)
#         c=a+b
#         a=b
#         b=c
# (fibo(10))
#
#
#
# """wap to get fibonacii num upto number specified"""
# def fibo(num):
#     a=0
#     b=1
#     i=0
#     while i<num:
#         print(a)
#         c=a+b
#         a=b
#         b=c
#         i+=1
# fibo(15)
#
#
#
# """Converting number to binary"""
# # def DecimalToBinary(num):
# #    if num>1:
# #       DecimalToBinary(num//2)
# #       print(num%2,end="")
# # if __name__=='__main__':
# #    dec_val=5
# #    DecimalToBinary(dec_val)
#
#
#
# """Sum of Diagonal"""
# def daisum(mat, n):
#    principal = 0
#    secondary = 0
#    for i in range(0,n):
#       principal+=mat[i][i]
#       # secondary+=mat[i][n-i-1]
#    print("principal diagonal:",principal)
#    # print("secondary diagonal:",secondary)
# a=[[1, 2 ,3 ,4],
#    [5,6,7,8],
#    [1, 2, 3, 4],
#    [5, 6, 7, 8]]
# print(daisum(a,4))
#
#
#
#
# # a = "%#@234575846326%$#"
# # import re
# # s=re.findall("\d", a)
# # d = ((set(s)))
# # print(list(sorted(d)))
#
#
#
#
#
# # aa = "#$%^^%^65*&&5"
# # ss = re.findall("\d+",aa)
# #print(max(ss))
#
#
#
# #
# # def column_sum(arr) :
# #     sum = 0
# #     for i in range(m):
# #         for j in range(n):
# #             sum += arr[j][i]
# #             print("Sum of the column", i, "=", sum)
# #             sum = 0
# # if __name__ == "__main__" :
# #     arr = np.zeros((4, 4))
# #     x = 1
# #
# #     for i in range(m):
# # #         for j in range(n):
# # #             arr[i][j] = x
# # #
# # #             x += 1
# # #     row_sum(arr)
# # #     column_sum(arr)
# #
# # from threading import *
# # """perferct square"""
# # def perfect_square(num):
# #     for i in range(num):
# #         if i*i==num:
# #             return True
# #     return False
# # print(perfect_square(16))
# #
# # t = Thread(perfect_square(20))
# # t.start()
# # """perfect number """
# # n = 28
# # sum=0
# # for i in range(1,n):
# #     if n%i==0:
# #         sum+=i
# # if sum ==n:
# #     print("num is perfect")
# # else:
# #     print("num is not a perfect")
#

num = 28
sum = 0
for i in range(1, num):
    if num%i == 0:
        sum+=i
if sum == num:
    print("perfect")
else:
    print("not a perfect")









# #
# #
# # """series of prime numbers"""
# # num = 100
# # for num in range(num):
# #     if num>1:
# #         for i in range(2, num):
# #             if num%i==0:
# #                 print("not a prime")
# #                 break
# #             else:
# #                 print(f'{num} is prime')
# #                 break
# #
# #
# #
# #
# # """Decimal to binary"""
# #
# # def DecimalToBinary(num):
# #     if num>1:
# #         DecimalToBinary(num//2)
# #         print(num%2, end="")
# #
# # if __name__=='__main__':
# #     dec_val=345
# #     DecimalToBinary(dec_val)
# #
# #
# # """Sum of Diagonal"""
# # def sum_diagonal(mat, n):
# #     principal=0
# #     secondary = 0
# #     for i in range(0, n):
# #         principal+=mat[i][i]
# #         secondary+=mat[i][n-i-1]
# #     print(principal)
# #     print(secondary)
# # a =[[1, 2, 3, 4],
# #     [5, 6, 7, 8],
# #     [1, 2, 3, 4],
# #     [5, 6, 7, 8]]
# # print(sum_diagonal(a, 4))
# def armstrong(num):
#     temp = str(num)
#     power = len(temp)
#     total = 0
#     for item in temp:
#         total+=int(item)**power
#     if num==total:
#         return "Num is an armstrong num"
#     return "Num is not an armstrong num"
# print(armstrong(1634))

def fibonaci(num):
    first = 0
    second = 1

    while first<num:
        print(first)
        sum = first+second
        first = second
        second = sum

(fibonaci(13))

"""wap to get fibonacii num upto number specified"""
# def fibo(num):
#     a=0
#     b=1
#     i=0
#     while i<num:
#         # print(a)
#         c=a+b
#         a=b
#         b=c
#         i+=1
# fibo(15)

def factorial(num):
    if num == 1 or num ==0:
        return 1
    else:
        return num*(factorial(num-1))
print(factorial(3))

def prime_num(start, end):
    for num in range(start, end):
        if num>1:
            for i in range(2, num):
                if num%i==0:
                    print(f'{num} ---------------------------------->is not a prime')
                    break
            else:
                print(f'{num} -------------------------------------->is a prime')
prime_num(100, 200)


st = "tea"
s = "eat"
a = sorted(st)
b = sorted(s)
if a == b:
    print("its an anagram")
else:
    print("its not an anagram")


st = "DAD"
res = ""
for item in st:
    res=item+res
if res == st:
    print("it is a pali")
else:
    print("its not a pali")


