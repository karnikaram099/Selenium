from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.jntua.ac.in/")
sleep(3)
actions = ActionChains\
    (driver)
actions.send_keys(Keys.PAGE_DOWN).perform()
ope1 = driver.find_element_by_xpath("//a[text()=' MECH']").click()
