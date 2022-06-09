# from pytest import fixture
# @fixture(scope="session")
# def fix_session():
#     print("running Setup SESSION scope")
#     yield
#     print("running teardown SESSION scope")
# @fixture(scope="module")
# def fix_mod():
#     print("running Setup MODULE scope")
#     yield
#     print("running Teardown MODULE scope")
# @fixture(scope="class")
# def fix_class():
#     print("running Setup CLASS scope")
#     yield
#     print("running Teardown CLASS scope")
# @fixture()
# def fix_func():
#     print("running Setup FUNCTION scope")
#     yield
#     print("running TEARDOWN CLASS scope")
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome("./chromedriver")
from pytest import fixture
@fixture
def test_setup():
    url = r'https://opensource-demo.orangehrmlive.com/'
    driver.get(url)
    driver.maximize_window()
    print("executed setup")
    yield
    driver.close()
    print("Tear dowm Executed")


def test_login():
    driver.find_element(By.ID, "txtUsername").send_keys("Tharun Kumar")
    driver.find_element(By.ID, "txtPassword").send_keys("9347806034")
    driver.find_element(By.ID, "btnLogin").click()


