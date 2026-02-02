import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        ops = webdriver.ChromeOptions()
        ops.add_experimental_option("detach", True)
        # ops.add_argument("--headless=new")
        driver = webdriver.Chrome(options=ops)
    elif browser == "edge":
        ops = webdriver.EdgeOptions()
        ops.add_experimental_option("detach", True)
        # ops.add_argument("--headless=new")
        driver = webdriver.Edge(options=ops)
    elif browser == "firefox":
        ops = webdriver.FirefoxOptions()
        # ops.add_argument("--headless=new")
        driver = webdriver.Firefox(options=ops)
    return driver

# --------To invoke browser from comand line for browser
# 1)This will get the value from CLI
def pytest_addoption(parser):
    parser.addoption("--browser")


# 2)--------These Below fixture will take it from from top-----------
@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


#
