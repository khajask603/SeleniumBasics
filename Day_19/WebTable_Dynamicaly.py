from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
driver.find_element(By.LINK_TEXT, "Admin").click()

# ------total rows n a table
rows = len(driver.find_elements(By.XPATH, "//div[@class='oxd-table-body']//*[contains(@class,'oxd-table-row')]"))
# //div[@class='oxd-table-body']//*[contains(@class,'oxd-table-row')]
print("total number of rows in a table:", rows)

count = 0
for r in range(1, rows + 1):
    colStatus = driver.find_element(By.XPATH, "(//div[@class='oxd-table-body']"
                                              "//*[contains(@class,'oxd-table-row')])["+str(r)+"]"
                                              "//*[contains(@class,'oxd-table-cell')][5]").text
    if colStatus == "Enabled":
        count = count + 1

print("Total Number of users:", rows)
print("Number of enabled users:", count)
print("Number of disabled users:", (rows - count))
