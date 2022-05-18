from selenium import webdriver
from time import sleep
# driver = webdriver.Chrome(r"C:\Users\karni\PycharmProjects\Selenium\driver\chromedriver.exe")
# driver.implicitly_wait(5)
# driver.get("https://www.monsterindia.com/")
#
# driver.find_element_by_id("SE_home_autocomplete").send_keys("python in skills")
# driver.find_element_by_xpath("//input[@value='Search']").click()
# id = driver.window_handles
# print(id)
# driver.find_element_by_xpath("//a[@title ='Click to upload your resume']").click()
# driver.find_element_by_xpath("(//input[@id='file-upload'])[1]").send_keys()

"""opening watsapp"""
# driver = webdriver.Chrome(r"C:\Users\karni\PycharmProjects\Selenium\driver\chromedriver.exe")
# driver.get("https://www.whatsapp.com/")
# driver.find_element_by_xpath("//h5[text()='WHATSAPP WEB']").click()
"""opening facebook"""
driver = webdriver.Chrome((r"C:\Users\karni\PycharmProjects\Selenium\driver\chromedriver.exe"))
driver.get("https://www.facebook.com/")
driver.find_element_by_xpath("//input[@class='inputtext _55r1 _6luy']").send_keys("ram")
sleep(2)
driver.find_element_by_xpath("//input[@id='pass']").send_keys("ram123456")
sleep(3)
driver.find_element_by_xpath("//button[@name = 'login']").click()
#driver_id = driver.window_handles
#print(driver_id)
# driver.switch_to.window(driver_id[1])
driver.implicitly_wait(30)
sleep(15)
driver.find_element_by_xpath("//input[@type='text']").send_keys("karnikaram.2000@gmail.com")
sleep(3)
driver.find_element_by_xpath("//input[@type='password']").send_keys("9642095340")
sleep(2)
driver.find_element_by_xpath("//button[@value='1']").click()
sleep(15)
driver.find_element_by_xpath("//input[@class='inputtext mrm']]").send_keys("6281308839")


