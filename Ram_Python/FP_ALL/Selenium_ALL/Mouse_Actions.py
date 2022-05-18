from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("./chromedriver")
driver.get("https://www.ajio.com/")
driver.maximize_window()
sleep(2)
actions =ActionChains(driver)
ope1= driver.find_element_by_xpath("//a[text()='MEN']")
sleep(8)
# driver.switch_to_alert().accept()
actions.move_to_element(ope1).perform()
sleep(3)
ope2 = driver.find_element_by_xpath("(//a[text()='Jackets & Coats'])[1]")
ope2.click()
sleep(4)
# driver.get_screenshot_as_file("Sony.png")
actions.send_keys(Keys.ARROW_DOWN).perform()
sleep(2)
driver.find_element_by_xpath("//span[text()='fabric']").click()
