import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="options: chrome, firefox, safari")


# @pytest.fixture
# def cmdopt(request):
#     return request.config.getoption("--cmdopt")


@pytest.fixture()
def setup(request):
    browser_name = request.config.getoption("--browser_name")

    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(
            executable_path="/Users/teoliver/Documents/Web_Projects_Docs/Selenium_Drivers/chromedriver",
            options=chrome_options)

    elif browser_name == "firefox":
        # firefox invocation (Gecko Driver)
        firefox_options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(
            executable_path="/Users/teoliver/Documents/Web_Projects_Docs/Selenium_Drivers/geckodriver",
            options=firefox_options)

    elif browser_name == "safari":
        # safati invocation
        pass

    else:
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(
            executable_path="/Users/teoliver/Documents/Web_Projects_Docs/Selenium_Drivers/chromedriver",
            options=chrome_options)

    action = ActionChains(driver)
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.action = action
    yield

    driver.close()
    driver.quit()
