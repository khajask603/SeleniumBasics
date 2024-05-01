import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://mypage.rediff.com/login/dologin")
driver.find_element(By.CSS_SELECTOR,"input[value='Login']").click()
alert=driver.switch_to.alert
print(alert.text)   #Please enter captcha
alert.accept()