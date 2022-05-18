from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("./chromedriver")
driver.get("http://demowebshop.tricentis.com/")
driver.maximize_window()
sleep(2)
actions = ActionChains(driver)
actions.send_keys(Keys.PAGE_DOWN).perform()
ope1=driver.find_element_by_xpath("//a[text()='Twitter']")
sleep(2)
ope1.click()
sleep(4)
# driver.find_element_by_xpath("//input[@aria-label='Search query']").send_keys("Nani")
sleep(5)
handles = driver.window_handles
driver.switch_to.window(handles[0])


