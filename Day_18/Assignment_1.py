import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.XPATH,"//button[text()='Confirm Box']").click()
alerts=driver.switch_to.alert
print(alerts.text)
alerts.accept()

#---Wikipedia

sB=driver.find_element(By.CSS_SELECTOR,"#Wikipedia1_wikipedia-search-input")
sB.send_keys("Selenium")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
SearchResults=driver.find_elements(By.XPATH,"//div[@id='Wikipedia1_wikipedia-search-results']//div/a")
print("Numberof Links:-",len(SearchResults))

for link in SearchResults:
    print(link.text)
    link.click()
    time.sleep(2)

windowIds=driver.window_handles
for winid in windowIds:
    driver.switch_to.window(winid)
    print(driver.title)

driver.quit()

# Press a button!
# Numberof Links:- 5
# Selenium
# Selenium in biology
# Selenium (software)
# Selenium disulfide
# Selenium dioxide
# Automation Testing Practice
# Selenium dioxide - Wikipedia
# Selenium disulfide - Wikipedia
# Selenium (software) - Wikipedia
# Selenium in biology - Wikipedia
# Selenium - Wikipedia