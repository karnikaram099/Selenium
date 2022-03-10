from selenium import webdriver
from time import sleep
driver=webdriver.Chrome("./chromedriver")
# # driver.get("https://www.irctc.co.in/nget/train-search")
# # driver.implicitly_wait(20)
# # driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
# # sleep(2)
#
#
#
# # # driver.find_element_by_xpath("//span[@class='ui-state-default ui-state-disabled ng-tns-c59-10 ng-star-inserted']").click()
# # driver.get("http://demowebshop.tricentis.com/")
# # driver.find_element_by_xpath("//a[contains(text(),'Books')]").click()
# # driver.find_element_by_xpath("//a[text()='Computing and Internet']")
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
#class _visibility_of_element_located():
    def wait(func):
        def wrapper(*args, **kwargs):
            locator=args[0]
            wait = WebDriverWait(driver, 20)
            v = _visibility_of_element_located(locator)
            wait.until(v)
            return wrapper

@wait
def click_element(locator):
    driver.find_element(*locator).click()


@wait
def enter_text(loctype, locvalue):
    driver.find_element(loctype, locvalue).clear()
    driver.find_element().send_keys()
