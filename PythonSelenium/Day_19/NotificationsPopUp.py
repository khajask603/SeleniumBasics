from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))



options.add_argument("--disable-notifications")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.airindia.com/in/en/book/search-flights.html")
