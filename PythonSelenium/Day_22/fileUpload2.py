
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"F:\Python & Selenium by pavan sir\Drivers\chromedriver.exe")
ops = webdriver.ChromeOptions()
ops.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=serv_obj, options=ops)

# Navigate to the desired webpage
driver.get("https://ps.uci.edu/~franklin/doc/file_upload.html")
driver.maximize_window()
upload=driver.find_element(By.XPATH,"//input[@name='userfile']")
# upload.click()
upload.send_keys("F:\\Python & Selenium by pavan sir\\Pyhton Notes\\DemoFiles.txt")


#------------------2nd website---------
# Navigate to the webpage containing the file upload form
driver.get("https://cgi-lib.berkeley.edu/ex/fup.html")

# Find the file input element
file_input = driver.find_element(By.NAME, "upfile")

# Send the file path to the file input element
file_input.send_keys(r"F:\\Python & Selenium by pavan sir\\Pyhton Notes\\DemoFiles.txt")

text_input = driver.find_element(By.NAME, "note")
text_input.send_keys("Demo Notes")

# Submit the form
submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
submit_button.click()