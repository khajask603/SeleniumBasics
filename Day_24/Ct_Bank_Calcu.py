import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from Day_24 import XLUTils

serv_obj=Service(r"F:\Python & Selenium by pavan sir\Drivers\chromedriver.exe")
ops=webdriver.ChromeOptions()
ops.add_experimental_option("detach",True)
driver=webdriver.Chrome(service=serv_obj, options=ops)
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://www.cit.com/cit-bank/resources/calculators/certificate-of-deposit-calculator/")
driver.maximize_window()

inideposit = driver.find_element(By.XPATH,"//input[@id='mat-input-0']")
length = driver.find_element(By.XPATH,"//input[@id='mat-input-1']")
apr = driver.find_element(By.XPATH,"//input[@id='mat-input-2']")
calbutton = driver.find_element(By.XPATH,"//button[@id='CIT-chart-submit']")

path = r"C:\Users\SHAIK KHAJA MOHIDDIN\Downloads\Solution\Solution\caldata2.xlsx"
rows = XLUTils.getRowCount(path, "Sheet1")
print("row count is : " , rows)

for r in range(2,rows+1):
    inidepo = XLUTils.readData(path, "Sheet1", r, 1)
    interestrate = XLUTils.readData(path, "Sheet1", r, 2)
    monthlength = XLUTils.readData(path, "Sheet1", r, 3)
    compoundingmonths = XLUTils.readData(path, "Sheet1", r, 4)
    exptotal = XLUTils.readData(path, "Sheet1", r, 5)

    inideposit.clear()
    length.clear()
    apr.clear()
    time.sleep(3)

    inideposit.send_keys(inidepo)
    length.send_keys(monthlength)
    apr.send_keys(interestrate)

    #Dropdown (Boostrap) - Not having Select Tag
    compoundrp = driver.find_element(By.XPATH,"//mat-select[@id='mat-select-0']")
    compoundrp.click()
    options = driver.find_elements(By.XPATH,"//div[@id='mat-select-0-panel']//mat-option")

    for option in options:
        if(option.text==compoundingmonths):
            option.click()

    calbutton.click()
    acttotal = driver.find_element(By.XPATH,"//span[@id='displayTotalValue']").text

    print("exp total is from excel: ", exptotal)
    print("act total is from app: ", acttotal)

    if(exptotal==acttotal):
        XLUTils.writeData(path, "Sheet1" ,r, 7 ,"Passed")
        XLUTils.fillGreenColor(path, "Sheet1" ,r, 7)
    else:
        XLUTils.writeData(path, "Sheet1" ,r, 7 ,"Failed")
        XLUTils.fillRedColor(path, "Sheet1" ,r, 7)

print("calculation has been completed")
driver.close()
