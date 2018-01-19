from selenium import webdriver
from time import sleep
dr= webdriver.Chrome()
dr.get('https://login.anjuke.com/login/form')
dr.maximize_window()
sleep(3)
dr.switch_to.frame('iframeLoginIfm')
dr.find_element_by_name("phone").send_keys("17768609406")
dr.find_element_by_name("sms_code").send_keys("8888")
dr.find_element_by_id("smsSubmitBtn").click()