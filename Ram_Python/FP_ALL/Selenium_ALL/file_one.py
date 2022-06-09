from selenium import webdriver
from time import sleep
from pytest import fixture
driver = webdriver.Chrome("./chromedriver")
driver.get("https://accounts.google.com/ServiceLogin")