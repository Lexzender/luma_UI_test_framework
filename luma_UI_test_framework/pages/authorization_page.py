from selene import browser, have, be
import allure
class Authorization:

    def __init__(self):
        self.login = browser.element('.logged-in').with_(timeout=10.0)

    def open_main_page(self):
        browser.open('/')

    def user_login(self,login,password):
        with allure.step("Нажать на кнопку 'Sign in'"):
            browser.element(".authorization-link").click()

        with allure.step("Ввести 'login' в поле 'Email'"):
            browser.element("#email").click().type(login)

        with allure.step("Ввести 'password' в поле 'Password'"):
            browser.element("#pass").click().type(password)

        with allure.step("Нажать на кнопку 'Sign in'"):
            browser.element(".primary[type='submit']").with_(timeout=10.0).should(be.visible).click()