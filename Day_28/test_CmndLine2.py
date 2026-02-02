from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test_Class:
    def test_Logo(self,setup):
        self.driver=setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        try:
            # Use explicit wait for the logo element
            logo_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='orangehrm-login-branding']/img"))
            )
            # Check if the logo element is displayed
            is_logo_displayed = logo_element.is_displayed()
            print("Is logo displayed:", is_logo_displayed)
            self.driver.close()

        except:
            self.driver.close()
            assert False

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