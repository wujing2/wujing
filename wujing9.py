from selenium import webdriver
import time
dr=webdriver.Chrome()
dr.get("https://www.baidu.com/")
dr.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
dr.maximize_window()
time.sleep(2)
dr.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()
dr.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("雨下的愿望")
dr.find_element_by_id("TANGRAM__PSP_10__password").send_keys("Wj07139865")
time.sleep(4)
dr.find_element_by_id("TANGRAM__PSP_10__submit").click()