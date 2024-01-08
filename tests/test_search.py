import allure
import pytest
from selene import be, have

from luma_UI_test_framework.pages.authorization_page import Authorization
from luma_UI_test_framework.pages.search_page import SearchItem
from tests.conftest import base_url

product = SearchItem()
authorization = Authorization()
login = "xichnek123@gmail.com"
password = "qwerty123Q"


@pytest.mark.search
@allure.label('layer', 'web')
@allure.label("owner", "Kostromin")
@allure.feature("Поиск")
@allure.story("Поиск товара")
@allure.link(base_url)
@allure.severity('Critical')
@pytest.mark.parametrize("item", ("short", 'tanks for women', 'Pants'))
def test_search(item):
    # GIVEN
    with allure.step(f'Открыть главную страницу {base_url}'):
        product.open_main_page()

    # WHEN
    with allure.step(f'Поиск товара: {item}'):
        product.search(item)

    # THEN
    with allure.step('Проверка выдачи результата'):
        product.result_search.should(have.text(f"Search results for: '{item}'"))


@pytest.mark.search
@allure.label('layer', 'web')
@allure.label("owner", "Kostromin")
@allure.feature("Поиск")
@allure.story("Сортировка товара по фильтру")
@allure.link(base_url)
@allure.severity('Major')
def test_search_coast_filter():
    # GIVEN
    with allure.step(f'Открыть главную страницу {base_url}'):
        product.open_main_page()

    with allure.step('Поиск товара'):
        product.search("short")

    with allure.step('Отсортировать товар по цене'):
        product.sort_by("Price")

    # THEN
    with allure.step('Убедиться, что товар отсортирован по цене'):
        assert product.price_item_first > product.price_item_last


@pytest.mark.search
@allure.label('layer', 'web')
@allure.label("owner", "Kostromin")
@allure.feature("Поиск")
@allure.story("Добавление товара в список 'желаний'")
@allure.link(base_url)
@allure.severity('Major')
def test_add_item_in_wish_list():
    # GIVEN
    with allure.step(f'Открыть главную страницу {base_url}'):
        product.open_main_page()

    with allure.step("Вводим данные для авторизации"):
        authorization.user_login(login, password)

    with allure.step('Поиск товара'):
        product.search("short")

    # WHEN
    with allure.step('Добавляем товар в wishlist'):
        product.add_item_in_wish_list()

    # THEN
    with allure.step('Проверяем, что товар добавился в wishlist'):
        product.name_in_wish_list.should(have.text(product.item))


@pytest.mark.search
@allure.label('layer', 'web')
@allure.label("owner", "Kostromin")
@allure.feature("Поиск")
@allure.story("Добавление товара в список 'желаний' неавторизованным пользователем")
@allure.link(base_url)
@allure.severity('Minor')
def test_chek_error_You_must_login_or_register_to_add_items_to_your_wishlist():
    # GIVEN
    with allure.step(f'Открыть главную страницу {base_url}'):
        product.open_main_page()

    with allure.step('Поиск товара'):
        product.search("short")

    # WHEN
    with allure.step('Добавляем товар в wishlist'):
        product.chek_error_You_must_login_or_register_to_add_items_to_your_wishlist()

    # THEN
    with allure.step('Проверяем, что товар не добавился и ошибка отображается'):
        product.page_title_wrapper.should(be.visible).should(have.text("Customer Login"))
        product.error_message.should(be.visible).should(
            have.text("You must login or register to add items to your wishlist."))
