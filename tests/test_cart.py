import os

from selene import browser
from selene import be, have, query

from luma_UI_test_framework.pages.authorization_page import Authorization
from luma_UI_test_framework.pages.cart_page import Cart
from luma_UI_test_framework.pages.search_page import SearchItem
from tests.conftest import base_url
import allure
import pytest

login = os.getenv("login_luma")
password = os.getenv("password_luma")

authorization = Authorization()
cart = Cart()
product = SearchItem()

@pytest.mark.cart
@allure.tag("web")
@allure.label("owner", "Kostromin")
@allure.feature("Корзина")
@allure.story("Добавление товара в корзину")
@allure.link(base_url)
@allure.severity('critical')
def test_add_item_to_cart():
    # GIVEN
    with allure.step(f'Открыть главную страницу {base_url}'):
        cart.open_main_page()

    with allure.step("Вводим данные для авторизации"):
        authorization.user_login(login, password)

    with allure.step("Ищем товар"):
        product.search("Erika Running Short")

    # WHEN
    with allure.step("Добавляем товар в корзину"):
        cart.add_item_to_cart()

    # THEN
    with allure.step("Проверяем, что товар добавился"):
        cart.name_item.should(have.text("Erika Running Short")).should(be.visible)
        cart.counter_items.should(be.visible).should(have.text("1"))

@pytest.mark.cart
@allure.tag("web")
@allure.label("owner", "Kostromin")
@allure.feature("Корзина")
@allure.story("Удаление товара из корзины")
@allure.link(base_url)
@allure.severity('critical')
def test_delet_item_to_cart():
    # GIVEN
    with allure.step(f'Открыть главную страницу {base_url}'):
        cart.open_main_page()

    with allure.step("Вводим данные для авторизации"):
        authorization.user_login(login, password)

    # WHEN
    with allure.step("Удалить товар из корзины"):
        cart.delet_item_to_cart()

    # THEN
    with allure.step("Проверяем, что корзина пустая"):
        cart.empty_cart.should(be.visible).should(have.text("You have no items in your shopping cart."))