import os

import allure
import pytest
from selene import have

from luma_UI_test_framework.pages.authorization_page import Authorization
from tests.conftest import base_url

login = os.getenv("login_luma")
password = os.getenv("password_luma")

authorization = Authorization()


@pytest.mark.authorization
@allure.tag("web")
@allure.label("owner", "Kostromin")
@allure.feature("Авторизация")
@allure.story("Авторизация существующего пользователя")
@allure.link(base_url)
@allure.severity('critical')
def test_login():
    # GIVEN
    with allure.step(f'Открыть главную страницу {base_url}'):
        authorization.open_main_page()

    # WHEN
    with allure.step("Вводим данные для авторизации"):
        authorization.user_login(login, password)

    # THEN
    with allure.step("Проверяем, что авторизация прошла успешно. Текст 'Welcome, Aleksei Kost!' отображается"):
        authorization.login.should(have.text("Welcome, Aleksei Kost!"))
