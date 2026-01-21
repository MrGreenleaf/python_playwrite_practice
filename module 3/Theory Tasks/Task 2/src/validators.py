import re
def is_valid_username(username):

    pattern = r"^[a-zA-Z0-9_]+$"

    # Проверяем пустоту
    if username is None or username == "":
        return False

    # Проверяем длину
    if len(username) < 3 or len(username) > 20:
        return False

    # Проверяем символы
    if not re.match(pattern, username):
        return False

    # ВСЕ проверки прошли
    return True

def is_valid_phone(phone):
    # """
    # Проверяет, что номер телефона валидный (для России).
    
    # Требования:
    # - Содержит 11 цифр
    # - Начинается с 7 или 8
    
    # Args:
    #     phone: Строка для проверки (может быть с пробелами, дефисами)
        
    # Returns:
    #     bool: True если валидно, False если нет
    # """
    
    # Проверка на пустоту
    if phone is None or phone == "":
        print("❌ Номер телефона не может быть пустым")
        return False
    
    # Удаляем пробелы, дефисы, скобки (если они есть)
    # +7 (999) 123-45-67 → 79991234567
    clean_phone = re.sub(r"[\s\-()]+", "", phone)
    
    # Проверка что остались только цифры
    if not clean_phone.isdigit():
        print("❌ Номер телефона должен содержать только цифры, пробелы, дефисы и скобки")
        return False
    
    # Проверка количества цифр (11 цифр)
    if len(clean_phone) != 11:
        print(f"❌ Номер телефона должен содержать 11 цифр (текущо: {len(clean_phone)})")
        return False
    
    # Проверка что начинается с 7 или 8
    if clean_phone[0] not in ["7", "8"]:
        print(f"❌ Номер телефона должен начинаться с 7 или 8 (текущо начинается с {clean_phone[0]})")
        return False
    
    # Все проверки пройдены
    print(f"✅ Номер телефона '{phone}' валидный")
    return True