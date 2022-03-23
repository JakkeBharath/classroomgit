

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Chrome")


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "Chrome":
        driver = webdriver.Chrome(executable_path="C:\Browser\chromedriver.exe")
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
    elif browser_name == "edge":
        driver = webdriver.Edge(executable_path="C:\Browser\msedgedriver.exe")
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\Browser\geckodriver.exe")
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()