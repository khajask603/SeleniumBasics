from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()
# 1)   myWait=WebDriverWait(driver,10) --> Explicity wait plain code decleration without exception & polling
#    mywait=WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,
#                                                                        ElementNotVisibleException,
#                                                                        ElementNotSelectableException,
#                                                                        Exception])   # -> Excweptions and poll frequency
#                                                                                         # long codeecleration
#3)
wait2=WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=Exception) #-> Simple Exceptions and poll frequency code
driver.get("https://www.google.co.in/")
search=driver.find_element(By.ID,"APjFqb")
search.send_keys("Selenium")
search.submit()
Sb=wait2.until(EC.visibility_of_element_located((By.XPATH,"//h3[text()='Selenium']")))
Sb.click()
driver.quit()