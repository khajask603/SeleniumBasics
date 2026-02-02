import pytest
class Test_Class:
    @pytest.mark.parametrize('user,pswd',
                             [("Admin","admin123"),
                              ("Am", "admin123"),
                              ("Admin", "a23"),
                              ("Adm", "admi3")
                              ]
                             )
    def test_Login(self,user,pswd):
        from selenium import webdriver
        from selenium.webdriver.common.by import By

        ops=webdriver.ChromeOptions()
        ops.add_experimental_option("detach", True)
        ops.add_argument("--headless=new")
        self.driver=webdriver.Chrome(options=ops)
        # self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(user)
        self.driver.find_element(By.XPATH, "// input[ @ placeholder = 'Password']").send_keys(pswd)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        try:
            self.status=self.driver.find_element(By.XPATH,"//img[@alt='client brand banner']").is_displayed()
            self.driver.close()
            assert self.status==True
        except:
            self.driver.close()
            assert False