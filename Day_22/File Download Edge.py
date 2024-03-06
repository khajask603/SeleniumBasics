from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import os
location = os.getcwd()
# +++++++++++++++++++++++++++++++++++++++++++++++A)CHROME++++++++++++++++++++++++++++++++++++
def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    preferences = {"download.default_directory": location}
    options.add_experimental_option("prefs",preferences)
    driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    return driver
# +++++++++++++++++++++++++++++++++++++++++++++++b)Edge++++++++++++++++++++++++++++++++++++
def edge_setup():
    from selenium.webdriver.edge.service import Service
    serv_Obj=Service("F:\Python & Selenium by pavan sir\Drivers\msedgedriver.exe")
    preferences = {"download.default_directory": location}
    options=webdriver.EdgeOptions()
    options.add_experimental_option("prefs",preferences)
    options.add_experimental_option("detach",True)
    driver=webdriver.Edge(options=options, service=serv_Obj)
    return driver
# +++++++++++++++++++++++++++++++++++++++++++++++C)FireFox++++++++++++++++++++++++++++++++++++
def firefox_setup():
    from selenium.webdriver.firefox.service import Service as FirefoxService
    from webdriver_manager.firefox import GeckoDriverManager
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))
    options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword")
    options.set_preference("browser.download.manager.showWhenStarting", False)
    options.set_preference("browser.download.folderList", 2)                     # 0-desktop 1-downloads folder 2- Desired loc
    return driver

# driver=chrome_setup()
# driver=edge_setup()
driver=firefox_setup()

#--Automation Code
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")
driver.maximize_window()
driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()

