from selenium import webdriver

def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    service_obj = Service(r"F:\Python & Selenium by pavan sir\Drivers\chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # options.add_argument("--headless")
    options.add_argument("--headless=new")
    driver_obj = webdriver.Chrome(service=service_obj, options=options)
    return driver_obj

def headless_Edge():
    from selenium.webdriver.edge.service import Service
    driverpath=r"F:\Python & Selenium by pavan sir\Drivers\msedgedriver.exe"
    serv_Obj = Service(driverpath)
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("detach", True)
    ops.add_argument("--headless=new")
    driver = webdriver.Edge(options=ops,service=serv_Obj)
    return driver

def headless_Ff():
    from webdriver_manager.firefox import GeckoDriverManager
    from selenium.webdriver.firefox.service import Service as FirefoxService
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get("https://www.monsterindia.com/")
    driver.maximize_window()
    return driver


# driver = headless_chrome()
# driver= headless_Edge()
driver= headless_Ff()


driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
