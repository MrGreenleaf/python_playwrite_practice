# ### Задание 2 (Среднее): Работа с https://www.python-requests.org/

# **Что нужно сделать:**

# 1. Открой https://httpbin.org/ (тестовый сервис для HTTP запросов)

# 2. Напиши тесты:
#    - Проверить, что страница загружается
#    - Найти все ссылки на странице и проверить, что их больше 1
#    - Проверить наличие текста "httpbin"
#    - Сняться скриншот страницы

# 3. Используй DevTools (F12) для поиска селекторов



import pytest

def test_find_all_links(page):
    page.goto("https://httpbin.org/", timeout=60000)
    title = page.title()
    links = page.locator("a")
    count = links.count()

    assert count > 1

    assert "httpbin" in page.content()

    page.screenshot(path="screenshot.png")