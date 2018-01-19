from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
from time import sleep
dr= webdriver.Chrome()
dr.get('http://mail.163.com/')
dr.maximize_window()
dr.switch_to.frame('x-URS-iframe')
dr.find_element_by_name("email").send_keys("17768609406")
dr.find_element_by_name("password").send_keys("Wj07139865")
dr.find_element_by_id("dologin").click()
