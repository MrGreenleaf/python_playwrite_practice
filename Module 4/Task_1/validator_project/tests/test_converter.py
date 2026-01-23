import pytest
from converter import celsius_to_fahrenheit   # если функция в src/converter.py

@pytest.mark.parametrize(
    "celsius, fahrenheit",
    [
        (0, 32),
        (100, 212),
        (-40, -40),
        (50, 122),
    ],
    ids=["1", "2", "3", "4"]
)

def test_celsius_to_fahrenheit(celsius, fahrenheit):
    assert celsius_to_fahrenheit(celsius) == fahrenheit