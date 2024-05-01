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

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()

alert=driver.switch_to.alert
print(alert.text)           #I am a JS prompt
alert.send_keys("Welcome")
time.sleep(3)
alert.accept()
# alert.dismiss()
alertIpText=driver.find_element(By.CSS_SELECTOR,"#result").text
print(alertIpText)   #You entered: Welcome
                     #You entered: null
