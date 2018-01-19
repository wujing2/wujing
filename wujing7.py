from selenium import webdriver
from selenium.webdriver.common.alert import Alert
import time
dr=webdriver.Chrome()
dr.get("file:///C:/Users/win7/Desktop/Alter.HTML")
dr.maximize_window()
dr.find_element_by_xpath("/html/body/button").click()
time.sleep(3)
Alert(dr).accept()









