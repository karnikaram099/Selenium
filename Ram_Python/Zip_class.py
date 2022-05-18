# a = [1, 2, 3, 4, 5, 6]
# b = [2, 3, 5, 6, 7, 8]
# # for item in zip(a, b):
    # print(item)

from itertools import zip_longest
a = [1, 2, 3, 4, 5, 6]
b = [2, 3, 5, 6, 7, 8, 6, 7, 8]
for item in zip_longest(a, b, fillvalue="not Present:"):
    print(item)

