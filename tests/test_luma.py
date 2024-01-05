import time

from selene import browser
from selene import be, have, query

from luma_UI_test_framework.pages.authorization_page import Authorization

base_url = "https://magento.softwaretestingboard.com/"
login = "xichnek123@gmail.com"
password = "qwerty123Q"

authorization = Authorization()

# def test_login():
#     browser.open("https://magento.softwaretestingboard.com/")
#
#     # browser.element(".authorization-link").click()
#     # browser.element("#email").click().type(login)
#     # browser.element("#pass").click().type(password)
#     # browser.element(".primary[type='submit']").should(be.visible).click()
#     authorization.user_authorization(login,password)
#
#     authorization.login.should(have.text("Welcome, Aleksei Kost!"))
#     # browser.element('.logged-in').should(have.text("Welcome, Aleksei Kost!"))
#
#     time.sleep(5)

# def test_search():
#     browser.open("https://magento.softwaretestingboard.com/")
#
#     browser.element(".search").click()
#     browser.element("[type='text']").type("short").press_enter()
#     browser.element('.base').should(have.text("Search results for: 'short'"))
#     items = browser.all(".product-items li")
#     assert len(items) == 12

# def test_search_coasr_filter():
#     browser.open("https://magento.softwaretestingboard.com/")
#
#     browser.element(".search").click()
#     browser.element("[type='text']").type("short").press_enter()
#     browser.element('.base').should(have.text("Search results for: 'short'"))
#     browser.element("#sorter").click()
#     browser.all("#sorter option").element_by(have.text("Price")).click()
#     price_item_1 = float(browser.all(".product-items li .price")[0].get(query.text).strip("$"))
#     price_item_12 = float(browser.all(".product-items li .price")[11].get(query.text).strip("$"))
#
#     assert price_item_1 > price_item_12

# def test_add_item_in_wish_list():
#     browser.open("https://magento.softwaretestingboard.com/")
#     browser.element(".authorization-link").click()
#     browser.element("#email").click().type(login)
#     browser.element("#pass").click().type(password)
#     browser.element(".primary[type='submit']").click()
#     browser.element(".search").click()
#     browser.element("[type='text']").type("short").press_enter()
#     browser.element(".product-items li").click()
#     item = browser.element(".page-title").get(query.text)
#     browser.element(".action.towishlist").click()
#     browser.element(".page-title").should(have.text("My Wish List")).should(be.visible)
#     browser.element(".product-items").should(have.text(item))


# def test_add_item_to_cart():
#     browser.open("https://magento.softwaretestingboard.com/")
#     browser.element(".authorization-link").click()
#     browser.element("#email").click().type(login)
#     browser.element("#pass").click().type(password)
#     browser.element(".primary[type='submit']").click()
#     browser.element(".search").click()
#     browser.element("[type='text']").type("Erika Running Short").press_enter()
#     browser.element(".swatch-attribute.size").element("[role='listbox']")
#     browser.element(".product-items li").click()
#     browser.element(".swatch-attribute.size").element("[role='listbox']").element("[option-label='28']").click()
#     browser.element(".swatch-attribute.color").element("[option-label='Green']").click()
#     browser.element(".action.primary.tocart").click()
#     browser.element(".action.showcart").click()
#     browser.element(".product-item-name").should(have.text("Erika Running Short")).should(be.visible)

# def test_delet_item_to_cart():
#     browser.open("https://magento.softwaretestingboard.com/")
#     browser.element(".authorization-link").click()
#     browser.element("#email").click().type(login)
#     browser.element("#pass").click().type(password)
#     browser.element(".primary[type='submit']").click()
#     browser.element(".counter-number").with_(timeout=20.0).should(be.visible).should(have.text("1"))
#     browser.element(".action.showcart").should(be.visible).click()
#     browser.element(".action.viewcart").should(be.visible).click()
#     browser.element(".action.action-delete").should(be.visible).click()
#     browser.element(".cart-empty").should(be.visible).should(have.text("You have no items in your shopping cart."))

# def test_chek_error_You_must_login_or_register_to_add_items_to_your_wishlist():
#     browser.open("https://magento.softwaretestingboard.com/")
#     browser.element(".search").click()
#     browser.element("[type='text']").type("short").press_enter()
#     browser.element(".product-items li").click()
#     browser.element(".action.towishlist").click()
#     browser.element(".page-title-wrapper").should(be.visible).should(have.text("Customer Login"))
#     browser.element(".page.messages").should(be.visible).should(have.text("You must login or register to add items to your wishlist."))