from fib_cache import caching_fibonacci
from generator_numbers import generator_numbers, sum_profit
from assistant import assistant_main

def main() -> None:
    #Точка входу.
    fib = caching_fibonacci()
    print(fib(10))   # 55
    print(fib(15))   # 610

    text = (
    "Загальний дохід працівника складається з декількох частин: "
    "1000.01 як основний дохід, "
    "доповнений додатковими надходженнями 27.45 і 324.00."
    )

    income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {income}")

# Перевіряємо, що запущено напряму
if __name__ == "__main__":
    main()
    assistant_main()
