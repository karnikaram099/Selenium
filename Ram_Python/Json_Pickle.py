# import json
# path = r"C:\Users\karni\OneDrive\Desktop\Sample\sample.txt"
# # with open(path) as file:
# # for item in file:
# #     item.strip()
# #     print(item)
# with open(path) as file:
#     json.load(file)

# with open("sample2", "w") as file_read, open(path_)
#     for line in file:
#         file.writelines(line)

from time import sleep
from selenium.webdriver.support.wait import WebDriverWait


class _wait:
    def wait(func):
        def wrapper(implicit_wait=None, *args, **kwargs):
            res = func(*args, **kwargs)
            implicit_wait(10)
            return res
        return wrapper

