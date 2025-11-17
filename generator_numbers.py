import re

def generator_numbers(text: str):
    # Шукаємо дійсні числа, відокремлені пробілами
    pattern = r"\b\d+\.\d+\b"
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func):
    total = 0.0
    for num in func(text):
        total += num
    return total
