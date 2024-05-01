from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://jqueryui.com/datepicker/")

# Find the iframe containing the datepicker
frame_element = driver.find_element(By.CSS_SELECTOR, "iframe.demo-frame")
# Switch to the iframe
driver.switch_to.frame(frame_element)
# Interact with the datepicker element
# driver.find_element(By.ID, "datepicker").send_keys('02/18/2023')
ipBox=driver.find_element(By.ID, "datepicker").click()

month="March"
year="2023"
date="7"
while True:
    mth=driver.find_element(By.CSS_SELECTOR,".ui-datepicker-month").text
    Year=driver.find_element(By.CSS_SELECTOR,".ui-datepicker-year").text
    if mth==month and Year==year :
        break
    else:
        driver.find_element(By.CSS_SELECTOR,".ui-datepicker-prev").click()
#Selecting Dates
dates=driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//a[@class='ui-state-default']")

for dat in dates:
    if dat.text==date:
        dat.click()
        break
driver.quit()


