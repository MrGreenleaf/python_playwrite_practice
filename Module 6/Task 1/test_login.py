# ### Задание 3 (Сложное): Интерактивный тест

# **Что нужно сделать:**

# 1. Найди любой сайт с простой формой (например, форму логина или поиска)

# 2. Напиши тест, который:
#    - Перейдёт на сайт
#    - Найдёт форму
#    - Заполнит поля
#    - Нажмёт кнопку отправки
#    - Проверит результат

# **Подсказки:**
# - Используй DevTools для поиска селекторов
# - Используй `fill()` для заполнения полей
# - Используй `click()` для кнопок
# - Проверь URL или текст страницы после отправки

import pytest

def test_login_positive(page):
    page.goto('https://www.saucedemo.com/')
    page.locator("#user-name").fill("standard_user")  #user-name
    page.locator("#password").fill("secret_sauce") #password
    page.locator("#login-button").click() #login-button

    assert "inventory.html" in page.url

