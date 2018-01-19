import time
from selenium import webdriver
driver=webdriver.Ie()
driver.get("http://10.135.78.4:8080/adminLogin.jsp")
driver.find_element_by_id("loginUser").send_keys("BOMUSER")
driver.find_element_by_id("password").send_keys("PASS1234")
driver.find_element_by_id("btnLogin").click()



