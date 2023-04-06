from selene import browser
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
    browser.element('.login-form [name=email]').type('qagurubot@gmail.com')
