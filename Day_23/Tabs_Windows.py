from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service(r"F:\Python & Selenium by pavan sir\Drivers\chromedriver.exe")
ops=webdriver.ChromeOptions()
ops.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj, options=ops)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://demo.nopcommerce.com/")
newTab=(Keys.CONTROL+Keys.ENTER)
driver.find_element(By.CSS_SELECTOR,".ico-register").send_keys(newTab)

##New Tab - Selenium4 :  Opens a new tab and switches to new tab
driver.get("https://www.opencart.com/")
driver.switch_to.new_window("tab")
driver.get("https://www.orangehrm.com/")

##New Tab - Selenium4 :  Opens a new tab and switches to new tab
driver.get("https://www.opencart.com/")
driver.switch_to.new_window("window")
driver.get("https://www.orangehrm.com/")