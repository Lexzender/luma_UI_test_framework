import time

import allure
from selene import browser, be


class Cart:

    def __init__(self):
        self.name_item = None
        self.counter_items = None
        self.empty_cart = None

    def open_main_page(self):
        browser.open('/')

    def add_item_to_cart(self):
        with allure.step("Раскрыть карточку с товаром"):
            browser.element(".product-items li").click()

        with allure.step("Выбрать размер товара"):
            browser.element(".swatch-attribute.size").element("[role='listbox']").element("[option-label='28']").click()

        with allure.step("Выбрать цвет товара"):
            browser.element(".swatch-attribute.color").element("[option-label='Green']").click()

        with allure.step("Добавить товар в корзину"):
            browser.element(".action.primary.tocart").click()

        with allure.step("Кликнуть по значку 'Корзина'"):
            time.sleep(5)
            browser.element(".action.showcart").click()

        self.name_item = browser.element(".product-item-name").with_(timeout=20.0)
        self.counter_items = browser.element(".counter-number").with_(timeout=20.0)

    def delet_item_to_cart(self):
        with allure.step("Кликнуть по значку 'Корзина'"):
            time.sleep(5)
            browser.element(".action.showcart").should(be.visible).click()

        with allure.step("Открыть страницу с корзиной"):
            browser.element(".action.viewcart").should(be.visible).click()

        with allure.step("Удалить товар из корзины"):
            browser.element(".action.action-delete").should(be.visible).click()

        self.empty_cart = browser.element(".cart-empty")
