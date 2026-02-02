import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Day_24 import XLUTils

serv_obj=Service(r"F:\Python & Selenium by pavan sir\Drivers\chromedriver.exe")
ops=webdriver.ChromeOptions()
ops.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj, options=ops)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-"
           "calculator-SBI-BSB001.html")
driver.maximize_window()
if driver.find_elements(By.CSS_SELECTOR, ".wzrk-alert"):
    # Popup exists, handle it
    popup = driver.find_element(By.CSS_SELECTOR, ".wzrk-alert")
    # Find the buttons
    allow_button = popup.find_element(By.ID, "wzrk-confirm")
    decline_button = popup.find_element(By.ID, "wzrk-cancel")
    # Click the decline button (No thanks)
    decline_button.click()

file=r"F:\Python & Selenium by pavan sir\SeleniumDDT Practise notes\caldata.xlsx"
Rows=XLUTils.getRowCount(file,"Sheet1")

for r in range(2,Rows+1):
#Reading data from excel
    princ=XLUTils.readData(file,"Sheet1",r,1)
    Roi=XLUTils.readData(file,"Sheet1",r,2)
    per1=XLUTils.readData(file,"Sheet1",r,3)
    per2 = XLUTils.readData(file, "Sheet1", r, 4)
    freq = XLUTils.readData(file, "Sheet1", r, 5)
    Exp_matv = XLUTils.readData(file, "Sheet1", r, 6)

    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(princ)
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(Roi)
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(per1)
    perioddrp=Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
    perioddrp.select_by_visible_text(per2)
    frq_Drop=Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
    frq_Drop.select_by_visible_text(freq)
    driver.find_element(By.XPATH,"//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']").click()
    Act_valu=driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text
    print(Exp_matv)
    print(Act_valu)
#Validation
    if float(Exp_matv)==float(Act_valu):
        print("Test Passed")
        XLUTils.writeData(file,"Sheet1",r,8,"Passed")
        XLUTils.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("Test Failed")
        XLUTils.writeData(file, "Sheet1", r, 8,"Failed")
        XLUTils.fillRedColor(file, "Sheet1", r, 8)
    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()
    time.sleep(2)
