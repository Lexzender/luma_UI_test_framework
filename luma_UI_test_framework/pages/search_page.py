from selene import browser, have, be, query
import allure

class SearchItem:

    def __init__(self):
        self.items = browser.all(".product-items li")
        self.item = None
        self.name_in_wish_list = None
        self.page_title_wrapper = None
        self.error_message = None
        self.price_item_first = None
        self.price_item_last = None
        self.result_search = None

    def open_main_page(self):
        browser.open('/')

    def search(self,item):
        with allure.step('Кликнуть по полю "Поиск"'):
            browser.element(".search").click()

        with allure.step(f'Ввести в поле "Поиск" {item}'):
            browser.element("[type='text']").type(item).press_enter()

        self.result_search = browser.element('.base')


    def sort_by(self,value):
        with allure.step('Кликнуть по фильтру'):
            browser.element("#sorter").click()

        with allure.step(f'Выбрать фильтр {value}'):
            browser.all("#sorter option").element_by(have.text(value)).click()

        self.price_item_first = float(browser.all(".product-items li .price")[0].get(query.text).strip("$"))
        self.price_item_last = float(browser.all(".product-items li .price")[11].get(query.text).strip("$"))


    def add_item_in_wish_list(self):
        with allure.step('Кликнуть по карточке с товаром'):
            browser.element(".product-items li").click()

        self.item = browser.element(".page-title").get(query.text)

        with allure.step('Добавить товар в wishlist'):
            browser.element(".action.towishlist").click()

        with allure.step('Проверяем что открыта страница "My Wish List"'):
            browser.element(".page-title").should(have.text("My Wish List")).should(be.visible)

        self.name_in_wish_list = browser.element(".product-items").element(".product-item-name")

    # def add_item_in_wish_list(self):
    #     with allure.step('Кликнуть по карточке с товаром'):
    #         browser.element(".product-items li").click()
    #
    #     self.item = browser.element(".page-title").get(query.text)
    #     browser.element(".action.towishlist").click()
    #     browser.element(".page-title").should(have.text("My Wish List")).should(be.visible)
    #     self.name_in_wish_list = browser.element(".product-items").element(".product-item-name")

    def chek_error_You_must_login_or_register_to_add_items_to_your_wishlist(self):
        with allure.step('Кликнуть по карточке с товаром'):
            browser.element(".product-items li").click()

        with allure.step('Добавить товар в wishlist'):
            browser.element(".action.towishlist").click()

        self.page_title_wrapper = browser.element(".page-title-wrapper")#.should(be.visible).should(have.text("Customer Login"))
        self.error_message = browser.element(".page.messages")#.should(be.visible).should(
            #have.text("You must login or register to add items to your wishlist."))

