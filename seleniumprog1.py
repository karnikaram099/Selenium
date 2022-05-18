# import select
#
# import selenium.webdriver.ie.webdriver
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver import Chrome
#
#
#
#
#
#
# #driver =webdriver.Chrome(r"C:\Users\karni\PycharmProjects\Selenium\chromedriver.exe")
# #
# # driver.get("http://demowebshop.tricentis.com/")
# # driver.find_element_by_link_text("Register").click()
# # driver.find_element_by_id("gender-male").click()
# # sleep(2)
# # driver.find_element_by_id("FirstName").send_keys("ram")
# # sleep(2)
# # driver.find_element_by_id("LastName").send_keys("Karnika")
# # sleep(1)
# # driver.find_element_by_id("Email").send_keys("kariniiikaramm@gmail.com")
# # sleep(2)
# # driver.find_element_by_id("Password").send_keys("1234500")
# # sleep(1)
# # driver.find_element_by_id("ConfirmPassword").send_keys("1234500")
# # sleep(2)
# # driver.find_element_by_id("register-button").click()
# # dr iver.find_element_by_css_selector("input[class='button-1 register-continue-button']").click()
# # # driver.find_element_by_css_selector("a[class='account']").click()
# # # driver.find_element_by_css_selector("a[class='ico-logout']").click()
# # driver.find_element_by_css_selector("a[class='ico-login']").click()
# # driver.find_element_by_id("Email").send_keys("kariniiikaramm@gmail.com")
# # driver.find_element_by_id("Password").send_keys("1234500")
# # driver.find_element_by_id("RememberMe").click()
# # driver.find_element_by_css_selector("input[class='button-1 login-button']").click()
#
# #
# # driver.get("file:///C:/Users/karni/Downloads/demo.html")
# # #driver.find_element_by_id("//input[@type='checkbox']").click()
# # links = driver.find_elements_by_xpath("//a")
# # for item in links:
# #     print(item.text)
# #     sleep(1)
#
# #
# # driver.get("https://www.python.org/")
# # links = driver.find_elements_by_xpath("//a")
# # for item in links:
# #     print(len(item.text))
# #     sleep(0.2)
#
# #
# # driver.get("https://www.python.org/")
# # links = driver.find_elements_by_xpath("//a")
# # for item in links:
# #     link_text = item.text.strip()
# #     if "python"in link_text:
# #         print(link_text)
# #
#
# # driver.get("https://www.python.org/")
# # links = driver.find_elements_by_xpath("//a")
# # data = []
# # for item in links:
# #     link_text = item.text.strip()
# #     url = item.get_attribute("href")
# #     if "python" in link_text:
# # #         data.append((link_text, url))
# # #         # print(data)
# #
# #
# # images = driver.find_elements_by_xpath("//img")
# # for image in images:
# #     print(image.get_attribute("alt"))
# #     sleep(1)
# #
# #
# # driver.get("https://www.python.org/")
# # sleep(5)
# # # driver.find_elements_by_xpath("//a[text()='Python 3.10.2']").click()
# # # sleep(3)
#
#
# #
# # driver.get("https://www.selenium.dev/downloads/")
# # driver.find_elements_by_xpath("//p[contains(text(),'Latest stable version')]//a")
# # driver.find_elements_by_xpath("//a[text()='documentation']").click()
#
#
# #
# #
# # from selenium import webdriver
# #
#driver =webdriver.Chrome(r"C:\Users\karni\PycharmProjects\Selenium\chromedriver.exe")
# #
# # # driver.get("https://www.google.com/")
# # sleep(1)
# # driver.maximize_window()
# # sleep(1)
# # driver.refresh()
# # sleep(1)
# # driver.minimize_window()
# # print(driver.current_url)
# # print(driver.title)
#
#
# # from selenium import webdriver
# # driver = webdriver.Chrome(r"C:\Users\karni\PycharmProjects\Selenium\chromedriver.exe")
# # driver.get("https://www.google.com/")
# # #driver.quit()
# # driver.close()
#
#
# # from selenium import webdriver
# # driver = webdriver.Chrome(r"C:\Users\karni\PycharmProjects\Selenium\chromedriver.exe")
# # driver.get("file:///C:/Users/karni/Downloads/demo%20(1).html")
#
# # elements = driver.find_elements_by_name('download')
# # # for item in elements[2::]:
# # #     sleep(1)
# # #     item.click()
# # elements[0].click()
# # elements[3].click()
# # #
# from selenium import webdriver
# driver = webdriver.Chrome(r"C:\Users\karni\PycharmProjects\Selenium\chromedriver.exe")
# # driver.get("https://www.python.org/downloads/")
# # #driver.find_element_by_xpath("//a[text()='Python 3.10.2']/../..//a[text()='Release Notes']").click()
# # driver.find_element_by_xpath("//a[text()='Python 3.9.8']/../..//a[text()='Release Notes']").click()
# from selenium import webdriver
# driver = webdriver.Chrome(r"C:\Users\karni\PycharmProjects\Selenium\chromedriver.exe")
# driver.get("http://demowebshop.tricentis.com/books")
# driver.find_element_by_xpath("//input[@class = 'button-2 product-box-add-to-cart-button']").click()
# driver.find_element_by_xpath("//input[@class = 'button-2 product-box-add-to-cart-button']").click()
#

#.get("http://demowebshop.tricentis.com/")



# from selenium import webdriver
# from time import sleep
# driver = webdriver.Chrome("./chromedriver")
# driver.get("http://demowebshop.tricentis.com/")
# driver.maximize_window()
# sleep(2)
# driver.find_element_by_xpath("//a[text()='14.1-inch Laptop']/../../..//input[@value='Add to cart']").click()





