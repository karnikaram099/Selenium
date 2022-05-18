from selenium import webdriver
from time import sleep
import re
driver=webdriver.Chrome("./chromedriver")
driver.get("https://www.ajio.com/")
driver.maximize_window()
sleep(3)
driver.find_element_by_xpath("//input[@name='searchVal']").send_keys("shoes")
driver.find_element_by_xpath("//span[@class='ic-search']").click()
sheos_=driver.find_element_by_xpath("//div[@class='contentHolder']")
shoes_names =sheos_[:6]
for shoe in shoes_names:
    print(shoe.text)
original_price = [int("".join(re.findall(r"\d",item.text))) for item in driver.find_elements_by_xpath("//span[@class='orginal-price']")[:6]]
index = original_price.index(max(original_price))
shoes_names[index].click()
print("the highest original price shoe is")
print("________")
print(shoes_names[index].text)
