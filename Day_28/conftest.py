import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver

@pytest.fixture()
def setup(browser):
        if browser == "chrome":
            ops = webdriver.ChromeOptions()
            ops.add_experimental_option("detach", True)
            ops.add_argument("--headless=new")
            driver = webdriver.Chrome(options=ops)
        elif browser == "edge":
            ops = webdriver.EdgeOptions()
            ops.add_experimental_option("detach", True)
            ops.add_argument("--headless=new")
            driver = webdriver.Edge(options=ops)
        elif browser == "firefox":
            ops = webdriver.FirefoxOptions()
            ops.add_argument("--headless=new")
            driver = webdriver.Firefox(options=ops)
        return driver

# -------------------Default Fixtures from PytestDocumentations--------------
# --------To invoke browser from comand line for browser
# 1)This will get the value from CLI
def pytest_addoption(parser):
    parser.addoption("--browser")


# 2)--------These Below fixture will take it from from top-----------
@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

# customizing reHTML Report---------------------------------------------
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "Orange HRM"
    config.stash[metadata_key]["Module Name"] = "Login Module"
    config.stash[metadata_key]["Tester Name"] = "Sk Khaja Mohiddin"


# Optional hook for modifying pre-existing metadata (if needed)
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)  # Remove if present
    metadata.pop("Plugins", None)   # Remove if present
#
