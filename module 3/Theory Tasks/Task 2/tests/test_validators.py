import pytest
from validators import is_valid_username, is_valid_phone

def test_is_valid_username_none():
    result = is_valid_username('')
    assert result == False

def test_is_valid_username_two_sybs():
    result = is_valid_username('ab')
    assert result == False

def test_is_valid_username_22_sybs():
    result = is_valid_username('ababababababababababab')
    assert result == False

def test_is_valid_username_spec_sybs():
    result = is_valid_username('!@#$%^&*()')
    assert result == False

def test_is_valid_username_valid():
    result = is_valid_username('Username_123')
    assert result == True