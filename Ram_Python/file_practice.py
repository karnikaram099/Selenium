# import os
# path = (r"C:\Users\karni\PycharmProjects\Alpha_3\file Handling\sample.txt")
# print(os.getcwd())
# #print(os.mkdir(r"C:\Users\karni\PycharmProjects\Alpha_3\file Handling\sample.txt"))
# print(os.listdir())
#

# from selenium import webdriver
# driver = webdriver.Chrome(r"C:\Users\karni\PycharmProjects\Selenium\chromedriver.exe")
# # driver.get("http://demowebshop.tricentis.com/").click()
# # driver.find_element_by_link_text("//a[text() = 'Twitter']").click()
#
# from selenium import webdriver
# driver = webdriver.Chrome("./chromedriver")


"""for printing right angled triangle"""

# for i in range(5):
#     print('* '*i)
#
# for _ in range(4):
#     print('* '*3)

# a = "hai hello how are you"
# c = ''
# for i in a:
#     if a.count(i) > 1:
#         # c+=1
#         print(i)
# s = "hai how are you"
# char = "a"
# for i in s:
#     if char ==i:
#         print(s.count(i))
#         break



d = {"a":1, "b":2}
d1 = {}
for key, value in d.items():
    d1[value]=key
print(d1)

a = 10
b = 20
a, b = b, a
print(a, b)

# print(b)
#
#
# with open("sample3.txt", 'w') as file:
#     file.write("Mechanical Engineering")
#
#

# d ={"a":1, "b":2, "a":4}
# # s = d.update(a=10)
# print(d["a"])

list_=[1, 2, 4, 5, 6, 7, 8, 9, 20, 30]
l1 = []
for item in list_:
    if item%3==0:
        (l1.append(33))
    else:
        l1.append(item)
print(l1)



# import keyword
# keyword.kwlist





