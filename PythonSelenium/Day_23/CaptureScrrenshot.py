from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PIL import Image
import os

from selenium.webdriver.common.by import By

serv_obj=Service(r"F:\Python & Selenium by pavan sir\Drivers\chromedriver.exe")
ops=webdriver.ChromeOptions()
ops.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj, options=ops)
driver.maximize_window()
driver.implicitly_wait(5)
# driver.get("https://demo.nopcommerce.com/")

#------1) Taking ScreenShot
driver.save_screenshot(r"F:\Python & Selenium by pavan sir\SeleniumTraining\pythonProject\Day_23\Scren1.png")
Image=driver.save_screenshot(os.getcwd()+"Scren2.png")

# 2))---Open the saved screenshot using Pillow========================================================
# Save screenshot to a file
screenshot_path = os.path.join(os.getcwd(), "Scren3.png")
driver.save_screenshot(screenshot_path)

# Open the saved screenshot using Pillow
screenshot = Image.open(screenshot_path)
screenshot.show()


# 3)-----For Specific Element screenshot===========================================================

# from PIL import Image  -----These need to be impported or downloaded near selenium packages
#Run These Command as well with above step --> pip install selenium pillow

# Navigate to the URL
driver.get("https://demo.nopcommerce.com/")

# Find the element by its XPath
element = driver.find_element(By.XPATH, "(//div[@class='item-grid'])[2]")

# Get the screenshot of the element as binary data
screenshot_data = element.screenshot_as_png

# Save the screenshot data to a file
with open("element_screenshot.png", "wb") as file:
    file.write(screenshot_data)

# Open the saved screenshot using Pillow
screenshot = Image.open("element_screenshot.png")
screenshot.show()