import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
import pytest
from validators import EmailValidator  # Теперь класс доступен
from converter import celsius_to_fahrenheit  # Добавь эту строку

@pytest.fixture
def validator():
    return EmailValidator()