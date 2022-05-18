""" WAP to create a dictionary with item and its index pair"""
l = ["python", "java", "Germany", "France"]
d1={}
for index, item in enumerate (l):
    d1[index] = item
# print(d1)

res = {index:item for index, item in enumerate(l)}
# print(res)

""" WAP to create a dictionary with word and its length pair"""
l = ["python", "java", "Germany", "France"]
res1 = {word:len(word)for word in l}
# print(res1)
d1 = {}
for word in res1:
    d1[word]=len(word)

# print(d1)

""" create a dictionary of character and its count"""
s = "hello world"

res2 = {char: s.count(char) for char in s}
# print(res2)
d1 = {}
for char in s:
    d1[char]=s.count(char)
# print(d1)

""" create a dictionary of word and its count"""
sentence = "python is a language, python programming is easy"
a = sentence.split()
res3 = {word:a.count(word) for word in a}
# print(res3)
d1 = {}

for word in a:
    d1[word]=a.count(word)
# print(d1)

""" dictionary with word and its count pair only if the word is of even length"""

sentence = "python is a language, python programming is easy"
a = sentence.split()
res4={word:a.count(word) for word in a if len(word)%2 == 0}
# print(res4)
d1 = {}
for word in a:
    if len(a)%2==0:
        d1[word]=a.count(word)

print(d1)
print(len("programming"))

""" dictionary with index and word pair if the word is of odd length reverse it,
else keep it as is"""

sentence = "python is a language, python programming is easy 1  2 3"
a = sentence.split()

res = {index : word if len(word) % 2 == 0 else word[::-1] for index, word in enumerate(a)}
# print(res)
d1 = {}
for i, w in enumerate(a):
    if len(w)%2 == 0:
        d1[i] = w
    elif len(w)%2!=0:
        d1[i]=w[::-1]
    else:
        d1[i]=w
print(d1)

""" flip keys and values in a dictionary """
dict_ = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}

res = {value:key for key, value in dict_.items()}
# print(res)
d1 = {}
for key, value in dict_.items():
    d1[value] = key

print(d1)


d = {"a": 1, "b" : 2}
d1 = {}
for k, v in d:

    d1[v] =k

print(d1)