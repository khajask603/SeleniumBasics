import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from LoginPageObject import loginPage

# from selenium.webdriver.chrome import webdriver
class Test_login:
    def test_login(self):
        ops = webdriver.ChromeOptions()
        ops.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=ops)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://admin-demo.nopcommerce.com/login")
    #Login Page Object creation----------------------
        self.lgn_pge_OB=loginPage(self.driver)
        self.lgn_pge_OB.setUserName("admin@yourstore.com")
        self.lgn_pge_OB.setUserPasword("admin")
        self.lgn_pge_OB.click_Login_Button()
        self_act_title=self.driver.title
        self.driver.close()
