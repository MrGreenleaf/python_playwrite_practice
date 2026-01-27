import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def browser():
    """Фикстура для браузера"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    """Фикстура для страницы"""
    page = browser.new_page()
    yield page
    page.close()