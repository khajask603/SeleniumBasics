import time
import autoit

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service(r"F:\Python & Selenium by pavan sir\Drivers\chromedriver.exe")
ops = webdriver.ChromeOptions()
ops.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=serv_obj, options=ops)

# Navigate to the desired webpage
driver.get("https://resume.naukri.com/resume-quality-score")
driver.maximize_window()

# Find the file input element
file_input = driver.find_element(By.XPATH, "//span[@class='browse']")

# Click the file input element to open the file dialog
file_input.click()

# Wait for the file dialog to appear (adjust the sleep time if needed)
time.sleep(1)

# Use AutoIt to handle the file dialog and select the file
autoit.win_active("Open")
autoit.control_send("Open", "Edit1", "F:\\Python & Selenium by pavan sir\\UDEMY DOCUMENTS\\Locators-seleium-python.pdf")
autoit.control_send("Open", "Edit1", "{ENTER}")

# Optionally, you can click a button to submit the form
# submit_button = driver.find_element_by_xpath("//button[@type='submit']")
# submit_button.click()

# Close the browser window
# driver.quit()



