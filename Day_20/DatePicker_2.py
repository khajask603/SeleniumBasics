from select import select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.find_element(By.CSS_SELECTOR,"#dob").click()
month=Select(driver.find_element(By.CSS_SELECTOR,".ui-datepicker-month"))
month.select_by_visible_text("Sep")
Year=Select(driver.find_element(By.CSS_SELECTOR,".ui-datepicker-year"))
Year.select_by_visible_text("1996")

#--Dates
dates=driver.find_elements(By.XPATH,"//table [@class='ui-datepicker-calendar']//tr/td")
for date in dates:
    if date.text=="7":
        date.click()
        break
