"""Iterator is noting but the process of iterating through each and every value or element in collection
and the function used to perform the operation is called iterator
1.iter()
2.next()
iter is used to get the intial address of varible
next is used to collect the current element and comtroll will move to next element"""
a = (1,2,3,4)
i = iter(a)
print(i)
s=next(i)
print(s)
d=next(i)
print(d)