from selenium.webdriver.common.by import By


class Test_Class:
    def test_Login(self, setup):

        self.driver=setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH, "// input[ @ placeholder = 'Password']").send_keys("admin123")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        try:
            self.status=self.driver.find_element(By.XPATH,"//img[@alt='client brand banner']").is_displayed()
            self.driver.close()
            assert self.status==True
        except:
            self.driver.close()
            assert False