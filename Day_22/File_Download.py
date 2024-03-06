from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

import os
location = os.getcwd()


def firefox_setup():
    from selenium.webdriver.firefox.service import Service as FirefoxService
    from webdriver_manager.firefox import GeckoDriverManager
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    return driver  # Return the initialized driver

# Call the setup function and assign the returned driver to the 'driver' variable
driver = firefox_setup()

# Continue with other automation steps
driver.get("https://filesampleshub.com/format/document/xls")

# 1)Hide Ads by Manipulating Elements
all_iframes = driver.find_elements(By.TAG_NAME,"iframe")
for iframe in all_iframes:
    driver.execute_script("arguments[0].style.visibility = 'hidden';", iframe)
driver.find_element(By.XPATH, "//a[contains(@href,'/xls/sample1.xls')]").click()
