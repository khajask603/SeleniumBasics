from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/login?returnUrl=%2F")

ele1=driver.find_element(By.CSS_SELECTOR,".email")
ele1.clear()
ele1.send_keys("abc@gmail.com")
print(ele1.text)       ## printed nothing
print(ele1.get_attribute('value'))  ##abc@gmail.com

