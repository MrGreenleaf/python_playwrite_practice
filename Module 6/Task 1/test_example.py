import pytest


def test_visit_example(page):
    """Проверка заголовка страницы"""
    page.goto("https://example.com")
    assert "Example Domain" in page.title()


def test_page_title_exact(page):
    """Точная проверка заголовка"""
    page.goto("https://example.com")
    assert page.title() == "Example Domain"


def test_find_h1_heading(page):
    """Проверка наличия и текста h1"""
    page.goto("https://example.com")
    
    # Находим h1
    heading = page.locator("h1")
    
    # Проверяем текст
    assert heading.text_content() == "Example Domain"


def test_h1_is_visible(page):
    """Проверка видимости h1"""
    page.goto("https://example.com")
    
    heading = page.locator("h1")
    assert heading.is_visible()


def test_page_contains_text(page):
    """Проверка что страница содержит нужный текст"""
    page.goto("https://example.com")
    
    assert "This domain is for use in documentation examples" in page.content()


def test_count_paragraphs(page):
    """Проверка количества параграфов"""
    page.goto("https://example.com")
    
    paragraphs = page.locator("p")
    assert paragraphs.count() == 2


def test_first_paragraph_text(page):
    """Проверка текста первого параграфа"""
    page.goto("https://example.com")
    
    first_p = page.locator("p").first
    assert "This domain is for use in documentation examples" in first_p.text_content()


def test_all_elements_visible(page):
    """Проверка видимости всех элементов"""
    page.goto("https://example.com")
    
    # Проверяем видимость h1
    assert page.locator("h1").is_visible()
    
    # Проверяем видимость всех p
    assert page.locator("p").first.is_visible()
    assert page.locator("p").last.is_visible()