from selene import browser, have
import pytest


# Открытие и закрытие браузера
@pytest.fixture
def brow():
    browser.open('https://qa.guru/cms/system/login')
    print('Открытие браузера')
    yield
    browser.close()
    print('Закрытие браузера')


# Ввод данных
def test_login(brow):
    browser.element('.login-form [name=email]').set_value('qagurubot@gmail.com')
    browser.element('.login-form [name=password]').set_value('qagurupassword').press_enter()
    browser.element('.main-header_login').click()
