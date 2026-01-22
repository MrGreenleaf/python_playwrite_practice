import pytest
from converter import convert_to_usd, convert_to_eur, convert_to_gbp

class TestConvertToUSD:
    """Тесты для convert_to_usd (1 USD = 78.46 RUB)"""
    
    def test_usd_normal(self):
        """Нормальная сумма: 1000 RUB → ~12.74 USD"""
        assert convert_to_usd(1000) == pytest.approx(12.744, abs=0.001)
    
    def test_usd_zero(self):
        """Нулевая сумма: 0 RUB → 0 USD"""
        assert convert_to_usd(0) == 0
    
    def test_usd_large(self):
        """Большая сумма: 100000 RUB → ~1274 USD"""
        assert convert_to_usd(100000) == pytest.approx(1274.44, abs=0.01)
    
    def test_usd_precise(self):
        """Точная проверка: 78.46 RUB → 1 USD"""
        assert convert_to_usd(78.46) == pytest.approx(1.0, abs=0.0001)

class TestConvertToEUR:
    """Тесты для convert_to_eur (1 EUR = 91.40 RUB)"""
    
    def test_eur_normal(self):
        """Нормальная сумма: 1000 RUB → ~10.94 EUR"""
        assert convert_to_eur(1000) == pytest.approx(10.937, abs=0.001)
    
    def test_eur_zero(self):
        """Нулевая сумма: 0 RUB → 0 EUR"""
        assert convert_to_eur(0) == 0
    
    def test_eur_large(self):
        """Большая сумма: 100000 RUB → ~1093 EUR"""
        assert convert_to_eur(100000) == pytest.approx(1093.69, abs=0.01)
    
    def test_eur_precise(self):
        """Точная проверка: 91.40 RUB → 1 EUR"""
        assert convert_to_eur(91.40) == pytest.approx(1.0, abs=0.0001)

class TestConvertToGBP:
    """Тесты для convert_to_gbp (1 GBP = 106.16 RUB)"""
    
    def test_gbp_normal(self):
        """Нормальная сумма: 1000 RUB → ~9.42 GBP"""
        assert convert_to_gbp(1000) == pytest.approx(9.421, abs=0.001)
    
    def test_gbp_zero(self):
        """Нулевая сумма: 0 RUB → 0 GBP"""
        assert convert_to_gbp(0) == 0
    
    def test_gbp_large(self):
        """Большая сумма: 100000 RUB → ~942 GBP"""
        assert convert_to_gbp(100000) == pytest.approx(942.11, abs=0.01)
    
    def test_gbp_precise(self):
        """Точная проверка: 106.16 RUB → 1 GBP"""
        assert convert_to_gbp(106.16) == pytest.approx(1.0, abs=0.0001)