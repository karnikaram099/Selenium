import re

mail = re.findall("^[a-zA-Z0-9_.-]+@[a-zA-Z0-9.-]+$", "karnikaram.2000@gmail.com")
print(mail)

# mail2 = re.findall/''("^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$ ")


# my_mail="kalyanjb143@gmail.com"
# # mail2=re.findall("^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$", my_mail)
# # print(mail2)
#
# email1=re.findall("\S+@\S+", my_mail)
# print(email1)
#
file = r"C:\Users\karni\OneDrive\Desktop\Sample\sample.txt"

with open(file) as f:
    c = 0
    for i in f:
        c += 1
        print(c)


