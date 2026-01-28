import pytest
from playwright.sync_api import sync_playwright

def test_login_page():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")
        username_input = page.locator('#user-name')
        password_input = page.locator('#password')
        submit_button = page.locator('#login-button')

        assert username_input.is_visible()
        assert password_input.is_visible()
        assert submit_button.is_visible()

        assert "Swag Labs" in page.title()
        browser.close()

def test_login_positive_submit():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        page.locator('#user-name').fill("standard_user")
        page.locator('#password').fill("secret_sauce")
        page.locator('#login-button').click()

        assert "inventory.html" in page.url

        browser.close()

def test_product_count():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        page.locator('#user-name').fill("standard_user")
        page.locator('#password').fill("secret_sauce")
        page.locator('#login-button').click()


        page.wait_for_selector(".inventory_item")
        count = page.locator(".inventory_item").count()
        print(f"Найдено товаров: {count}")
        assert count == 6, f"Ожидалось 6 товаров, найдено {count}"
        browser.close()

def test_wrong_pass_error_message():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        page.locator('#user-name').fill("standard_user")
        page.locator('#password').fill("wrong_password")
        page.locator('#login-button').click()
        
        error_locator = page.locator(".error-message-container")
        error_locator.wait_for(state="visible")
        error_text = error_locator.text_content()  # ← Весь текст контейнера
        
        print(f"🔍 Полный текст ошибки: '{error_text}'")
        
        assert "do not match any user" in error_text.lower()
        browser.close()

def test_null_username_message():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")

        page.locator('#user-name').fill("")
        page.locator('#password').fill("wrong_password")
        page.locator('#login-button').click()

        error_locator = page.locator(".error-message-container")
        error_locator.wait_for(state="visible")
        error_text = error_locator.text_content()  # ← Весь текст контейнера
        
        print(f"🔍 Полный текст ошибки: '{error_text}'")
        
        assert "username is required" in error_text.lower()
        browser.close()