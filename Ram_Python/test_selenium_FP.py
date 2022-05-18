# # # from selenium import webdriver
# # # from time import sleep
# # # driver=webdriver.Chrome("./chromedriver")
# # # driver.get("https://www.monsterindia.com/")
# # # from selenium.webdriver.common.action_chains import ActionChains
# # # actions = ActionChains(driver)
# # # ele = driver.find_element_by_xpath("//a[text()='Job search']")
# # # actions.move_to_element(ele).perform()
# # #
# # # ele1 = driver.find_element_by_xpath("//a[text()='Jobs by Education']")
# # # actions.move_to_element(ele1).perform()
# # # sleep(10)
# # # ele2 = driver.find_element_by_xpath("//a[contains(text(),'B Tech Jobs')]")
# # # sleep(5)
# # # ele2.click()
# # # from selenium import webdriver
# # # from selenium.webdriver.common.action_chains import ActionChains
# # # from time import sleep
# # # from selenium.webdriver.common.keys import Keys
# # # driver = webdriver.Chrome("./chromedriver")
# # # sleep(4)
# # # driver.get("https://www.monsterindia.com/")
# # #
# # # driver.maximize_window()
# # # actions = ActionChains(driver)
# # # actions.send_keys(Keys.ARROW_DOWN).perform()
# # # sleep(6)
# # # driver.find_element_by_xpath("//span[contains(text(),'Customer Care ')]").click()
# # # #driver.get_screenshot_as_file("Screen shot 1.jpeg")
# # # driver.save_screenshot(r"C:\Users\karni\PycharmProjects\Selenium\files4th\Screen shot 2.png")
# # #
# # #
# # #
# # # from selenium import webdriver
# # # from time import sleep
# # # from selenium.webdriver.common.action_chains import ActionChains
# # # from selenium.webdriver.common.keys import Keys
# # # driver = webdriver.Chrome("./chromedriver")
# # # driver.get("https://www.ajio.com/")
# # # driver.maximize_window()
# # # driver.switch_to.alert().accept()
# # # driver.find_element_by_css_selector("")
# # #
# # # sleep(2)
# # # actions =ActionChains(driver)
# # # ope1= driver.find_element_by_xpath("//a[text()='MEN']")
# # # sleep(8)
# # # # driver.switch_to_alert().accept()
# # # actions.move_to_element(ope1).perform()
# # # sleep(3)
# # # ope2 = driver.find_element_by_xpath("(//a[text()='Jackets & Coats'])[1]")
# # # ope2.click()
# # # sleep(4)
# # # # driver.get_screenshot_as_file("Sony.png")
# # # actions.send_keys(Keys.ARROW_DOWN).perform()
# # # sleep(2)
# # # driver.find_element_by_xpath("//span[text()='fabric']").click()
# # #
# # #
# # #
# # # from selenium import webdriver
# # # from time import sleep
# # # from selenium.webdriver.common.action_chains import ActionChains
# # # from selenium.webdriver.common.keys import Keys
# # #
# # # driver = webdriver.Chrome("./chromedriver")
# # # driver.get("https://www.jntua.ac.in/")
# # # sleep(3)
# # # # actions = ActionChains(driver)
# # # # actions.send_keys(Keys.PAGE_DOWN).perform()
# # # # ope1 = driver.find_element_by_xpath("//a[text()=' MECH']").click()
# # # #
# #
# #
# # from selenium import webdriver
# # from time import sleep
# # from selenium.webdriver.common.action_chains import ActionChains
# # from selenium.webdriver.common.keys import Keys
# # driver = webdriver.Chrome("./chromedriver")
# # driver.get("http://google.com/")
# # driver.maximize_window()
# # actions = ActionChains(driver)
# # sleep(3)
# # driver.find_element_by_xpath("//input[@title='Search']").send_keys("python", Keys.ENTER)
# # sleep(2)
# # driver.find_element_by_xpath("//h3[text()='Welcome to Python.org']").click()
# # ope1 = driver.find_element_by_xpath("(//a[text()='About'])[1]")
# # actions.move_to_element(ope1).perform()
# # sleep(2)
# # ope2 = driver.find_element_by_xpath("(//a[text()='Quotes'])[1]").click()
# # # actions.move_to_element(ope2).perform()
# # driver.get_screenshot_as_file("Python Screnshot.png")
#
#
# from selenium import webdriver
# from time import sleep
# # from wait_Deco import wait
# import wait_Deco
# @wait_Deco.wait
# def wait_():
#     driver = webdriver.Chrome("./chromedriver")
#     driver.get("https://www.amazon.in/")
#     driver.maximize_window()
#     sleep(3)
#
#     driver.find_element_by_xpath("//select[@aria-describedby='searchDropdownDescription']").click()
#     driver.find_element_by_xpath("//option[text()='Electronics']").click()
#         # driver.find_element_by_xpath("//input[@type='submit']").click()
#         # driver.find_element_by_xpath("//span[text()='Computer accessories']").click()
#     driver.find_element_by_xpath("//input[@name='field-keywords']").send_keys("Computer Accessories")
#     driver.find_element_by_xpath("//input[@type='submit']").click()

    # from selenium.webdriver.support.select import Select
# wait_()



# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.keys import Keys
# driver=webdriver.Chrome("./chromedriver")
# driver.get("https://www.google.com/maps/@12.9311737,77.5504773,15z")
# driver.maximize_window()
# # driver.switch_to.alert().dismiss()
# driver.find_element_by_xpath("//input[@id='searchboxinput']").send_keys("Hydrabad-500001-nampally", Keys.ENTER)

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from time import sleep
# driver = webdriver.Chrome("./chromedriver")
# driver.get("https://www.google.com/")
# driver.find_element_by_xpath("//input[@class='gLFyf gsfi']").send_keys("Ram pothineni", Keys.ENTER)




#
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome("./chromedriver")
# # driver.get("file:///C:/Users/karni/Downloads/demo%20(1).html")
# # driver.maximize_window()
# # elements = driver.find_elements_by_name("download")
# # for element in elements:
# #     element.click()
# driver.get("http:myntra.com")
# driver.maximize_window()
# data = driver.find_element_by_xpath("//input[@placeholder='Search for products, brands and more']").send_keys("pepe Jeans", Keys.ENTER)
# brands = driver.find_elements_by_xpath("//h3[text()='Pepe Jeans']")
# for brand in brands:
#     if brand.text=="pepe Jeans".lower():
#         print(f'{brand.text} this is brandname')

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome("./chromedriver")
driver.get("http://demowebshop.tricentis.com/")
# sleep(2)
# reg_link = driver.find_element_by_xpath("//a[text()='Register']")
# actions = ActionChains(driver)
# actions.context_click(reg_link).perform()
gifts_link = driver.find_element_by_xpath("(//a[contains(text(),'Gift Cards')])[3]")
actions = ActionChains(driver)
actions.context_click(gifts_link).perform()




