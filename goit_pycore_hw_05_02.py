import re
from typing import Callable

def generator_numbers(text: str):
    for word in text.split():
        match = re.search(r"\d+\.\d{2}", word)
        if match:
            yield float(match.group())

def sum_profit(text: str, func: Callable):
    profit = 0.0
    for number in func(text):
        profit += number
    return profit

def main():
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income:0.2f}")

if __name__ == '__main__':
    main()