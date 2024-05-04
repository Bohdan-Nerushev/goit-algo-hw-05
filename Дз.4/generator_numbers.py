from typing import Callable
import re

def generator_numbers(text: str):
    """Функція-генератор, яка шукає дійсні числа у тексті і повертає їх по одному."""
    pattern = r'\b\d+\.\d+\b'  # Регулярний вираз для пошуку дійсних чисел
    for match in re.finditer(pattern, text):
        yield float(match.group())  # Повертаємо кожне знайдене число як float

def sum_profit(text: str, func: Callable):
    """Функція, яка обчислює суму всіх дійсних чисел у тексті."""
    total = 0
    # Викликаємо функцію-генератор для отримання дійсних чисел
    for number in func(text):
        total += number
    return total

# Приклад використання:
text = "Загальний дохід працівника складається 77.0 з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
