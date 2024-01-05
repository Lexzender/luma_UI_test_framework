import allure
import pytest
from selene import browser

from luma_UI_test_framework.utils import allure_attach

base_url = "https://magento.softwaretestingboard.com"

@pytest.fixture(scope="function", autouse=True)
def browser_config():

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