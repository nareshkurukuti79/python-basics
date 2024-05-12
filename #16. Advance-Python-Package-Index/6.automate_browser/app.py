######################## Automating The Browser ###########################

from selenium import webdriver
import time

# opening the browser
browser = webdriver.Firefox()
browser.get("https://gmail.com")

# username
username_filed = browser.find_element_by_id("identifierId")
username_filed = browser.send_keys("python36@gmail.com")

# clicking the next button
next_btn = browser.find_element_by_class_name("VfPpkd-vQzf8d")
next_btn.click()


time.sleep(5)


password_filed = browser.find_element_by_xpath("/html/body/div[1]")

password_filed.send_keys("hey21000there")
