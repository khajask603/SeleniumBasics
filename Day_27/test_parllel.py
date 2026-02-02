import pytest
from selenium.webdriver.common.by import By

class Test_Login:
    # -----------------------Chrome---------------------
    def test_login_chrome2(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By

        ops = webdriver.ChromeOptions()
        ops.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=ops)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "// input[ @ placeholder = 'Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        title = self.driver.title
        print(title)
        assert title in "OrangeHRM"
        self.driver.quit()

    # -----------------------EDGE---------------------
    # =--------Edge using Service class---------
    def test_login_edge(self):
        from selenium import webdriver
        from selenium.webdriver.edge.service import Service

        serv_Obj = Service(r"F:\Python & Selenium by pavan sir\Drivers\msedgedriver.exe")
        ops = webdriver.EdgeOptions()
        ops.add_experimental_option("detach", True)
        self.driver = webdriver.Edge(options=ops, service=serv_Obj)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "// input[ @ placeholder = 'Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        title = self.driver.title
        print(title)
        assert title in "OrangeHRM"
        self.driver.quit()

    # -----------------------FireFox---------------------
    def teste_login_firefox(self):
        from selenium import webdriver

        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "// input[ @ placeholder = 'Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        title = self.driver.title
        print(title)
        assert title in "OrangeHRM"
        self.driver.quit()
