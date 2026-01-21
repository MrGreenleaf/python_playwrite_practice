# test_email_validator.py
from email_validator import validate_email

def test_valid_email():
    # Подготовка
    email = "john@example.com"
    
    # Действие
    result = validate_email(email)
    
    # Проверка
    assert result == True

def test_email_without_at_sign():
    result = validate_email("johnexample.com")
    assert result == False

def test_email_without_dot_in_domain():
    result = validate_email("john@examplecom")
    assert result == False

def test_empty_email():
    result = validate_email("")
    assert result == False

def test_email_with_multiple_at_signs():
    result = validate_email("john@example@com")
    assert result == False