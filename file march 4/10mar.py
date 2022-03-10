+from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.color import Color
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("./chromedriver")


driver.get("http://demowebshop.tricentis.com/")
class _visibility_of_element_located(visibility_of_element_located):
    def __call__(self,driver):
        result =super().__call__(driver)
        if isinstance(result,WebElement):
            return result.is_enabled()
        else:
            return False


def wait(func):
    def wrapper(*args,**kwargs):
        locator = args[0]
        wait = WebDriverWait(driver,20)
        v =_visibility_of_element_located(locator)
        wait.until(v)
        return func(*args,**kwargs)
    return wrapper


@wait
def click_element(locator):
    driver.find_element(*locator).click()


@wait
def enter_text(locator,value):
    driver.find_element(*locator).clear()
    driver.find_element(*locator).send_keys(value)

click_element((By.LINK_TEXT,"Register"))
click_element((By.ID,"gender-male"))
enter_text((By.NAME,"FirstName"), "hai")
enter_text((By.NAME,"LastName"), "helloo")
enter_text((By.ID,"Email"), "priya@gmail.com")
enter_text((By.ID,"Password"), "pass123456")
enter_text((By.ID,"ConfirmPassword"), "pass123456")
click_element((By.ID,"register-button"))










