import os

import allure
import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from luma_UI_test_framework.utils import allure_attach

base_url = "https://magento.softwaretestingboard.com"

DEFAULT_BROWSER_VERSION = '100.0'


def pytest_addoption(parser):
   parser.addoption(
       "--browser_version",
       default="100.0",
   )
   parser.addoption(
       "--base_url",
       default="https://magento.softwaretestingboard.com"
   )
   parser.addoption(
       "--browserName",
       default="chrome",
       choices=['firefox', 'opera']
   )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def browser_config(request):
    browser_version = request.config.getoption("--browser_version")
    browser_version = browser_version if browser_version != '' else DEFAULT_BROWSER_VERSION
    browserName = request.config.getoption("--browserName")
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--incognito")
    selenoid_capabilities = {
        "browserName":browserName,
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    driver = webdriver.Remote(command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
                              options=options)
    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = base_url
    allure.dynamic.parameter("Window Width", str(browser.config.window_width))
    allure.dynamic.parameter("Window Height", str(browser.config.window_height))
    yield browser

    allure_attach.screenshot(browser)
    allure_attach.html(browser)
    allure_attach.video(browser)

    browser.quit()
