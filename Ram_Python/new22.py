from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.amazon.com")
driver.maximize_window()
driver.find_element_by_xpath("(//input[@class='nav-input nav-progressive-attribute'])[1]").send_keys("Books",Keys.ENTER)
sleep(3)
driver.find_element_by_xpath("(//input[@class='nav-input nav-progressive-attribute'])[1]").send_keys("Children books", Keys.ENTER)
# driver.get("https://www.redbus.in/")
# driver.find_element_by_xpath("//input[@data-message='Please enter a source city']").send_keys("Kurnool")
# sleep(2)
# driver.find_element_by_xpath("//input[@data-message='Please enter a destination city']").send_keys("Hydrabad")
# sleep(2)
# driver.find_element_by_xpath("//span[@class='fl icon-calendar_icon-new icon-onward-calendar icon']").click()
# driver.find_element_by_xpath("//td[@class='wd day']").click()
# driver.find_element_by_xpath("//button[text()='Search Buses']").click()