# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome("./chromedriver")
# driver.get("file:///C:/Users/karni/Downloads/demo.html")
# sleep(3)
# driver.maximize_window()
# list_box = driver.find_element_by_id("standard_cars")
# # select = Select(list_box)
# # select.select_by_index(4)
# # sleep(2)
# # select.select_by_index(6)
# # all_selected_options=select.options
# # for item in all_selected_options:
# #     print(item.text)
# # #
# # #
# # select = Select(list_box)
# # all = select.options
# # for item in all:
# #     print(item.text)
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome("./chromedriver")
# driver.get("file:///C:/Users/karni/Downloads/demo.html")
# driver.maximize_window()
# list_box = driver.find_element_by_id("standard_cars")
# select = Select(list_box)
# all_select = select.options
# for item in all_select:
#     print(item.text)
from pytest import fixture
@fixture
def greet():
    return "hello world"
def test_greet(greet):
    assert "hello world" == greet

