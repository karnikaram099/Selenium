# from threading import *
# def display():
#     print("executing by:", current_thread().name)
#     for _ in range(5):
#         print("ram")
#
#
# t = Thread(target=display)
# t.start()
# print("executing by:", current_thread().name)
# for _ in range(5):
#     print("Karnika")


from threading import *


def display():
    print("1st pro", current_thread().name)
    for _ in range(5):
        print("Multi", end="")


t = Thread(target=display)
t.start()
print("2nd pro", current_thread().name)
for _ in range(5):
    print("Star", end="")

