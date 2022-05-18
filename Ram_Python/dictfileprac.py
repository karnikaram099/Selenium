d = {"a": 1, "b": 2}
d1 = {}
for k, v in d.items():
    d1[v] = k
print(d1)

list_= [1,2,3,4, 3, 3, 4]
b = list_.sort()
print(b)
print(sorted(list_))
class Ram:
    a = 10

self = Ram
print(self.a)


a = [10, 10, 20, 830, 50]
e = 30
for item, index in enumerate(a):
    if item == e:
        print(index)