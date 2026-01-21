def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def divide(a, b):
    if a == 0:  # ← ЭТА ПРОВЕРКА ВАЖНА!
        raise ValueError("Деление на 0 невозможно!")
    elif b == 0:
        raise ValueError("Деление на 0 невозможно!")
    return a / b