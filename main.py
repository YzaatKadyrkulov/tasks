# import math
"""
1. Переменные и типы данных (int, float, str, bool)
«Привет, имя!»: Запросите у пользователя имя и выведите: "Привет, [имя]".
Конвертер валют: Переведите сумму в рублях в доллары (используя фиксированный курс).
Обмен значений: Даны две переменные
 и
. Поменяйте их значения местами, не используя третью переменную.
Площадь круга: Запросите радиус и вычислите площадь круга (
).
"""

# name = input("Enter your name:")
# print('Hello:', name)
#
# rub = float(input("Введите сумму в рублях: "))
# usd = rub / 90
# print("В долларах: ", usd)
#
# name = 23
# your = 31
#
# name, your = your, name
# print(name, your)
#
# r = float(input("Enter radius: "))
# s = math.pi * r ** 2
#
# print("Площадь круга: ", s)

"""
2. Условные операторы (if, elif, else)
Четное или нечетное: Проверьте, является ли 
введенное число четным.
Високосный год: Определите, является ли год, 
введенный пользователем, високосным.
Максимум из трех: Запросите три числа и выведите 
наибольшее из них.
Калькулятор: Запросите два числа и знак операции 
(+, -, *, /). Выведите результат, обработав деление на ноль.
"""

# num = int(input("Enter a number: "))
#
# if num % 2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")


# year = int(input("Enter a year: "))
#
# if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
#
# if a >= b and a >=c:
#     print("Max:", a)
# elif b >= a and b >= c:
#     print("Max:", b)
# else:
#     print("Max:", c)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# op = input("Enter operation (+, -, *, /): ")
#
# if op == "+":
#     print(a + b)
# elif op == "-":
#     print(a - b)
# elif op == "*":
#     print(a * b)
# elif op == "/":
#     if a == 0 or b == 0:
#         print("You cannot divide by zero!")
#     else:
#         print(a / b)
# else:
#     print("Invalid operation")

"""
3. Циклы (for, while)
Таблица умножения: Выведите таблицу умножения для 
заданного числа.
Сумма чисел: Посчитайте сумму чисел от 1 до n
с помощью цикла while.
Пирамида: Выведите пирамиду из звездочек * или 
чисел.
Угадай число: Программа загадывает число, а 
пользователь пытается его угадать (используйте while и if).
"""
# num = int(input("Enter a number: "))
#
# for i in range(1, 11):
#     print(num, "*", i, "=", i * num)
# y
# n = int(input("Enter a number: "))
#
# i = 1
# sum = 0
#
# while i <= n:
#     sum += i
#     i += 1
#
# print("Sum: ", sum)

# n = int(input("Введите количество строк: "))
#
# for i in range(1, n + 1):
#     print("*" * i)

# import random
#
# secret = random.randint(1, 10)
#
# guess = 0
#
# if guess != secret:
#     guess = int(input("Угайдай число от 1 до 10: "))
#
#     if guess > secret:
#         print("Слишком большое: ")
#     elif guess < secret:
#         print("Слишком маленькое: ")
#     else:
#         print("ты угадал!")

"""
4. Строки
Палиндром: Проверьте, является ли введенная строка палиндромом 
(читается одинаково в обоих направлениях, например, "шалаш").
Анализ строки: Посчитайте количество гласных и согласных букв в строке.
"""

# s = input("Enter a word: ")
#
# if s == s[::-1]:
#     print("Это палиндром")
# else:
#     print("Это не палиндром")

# word = input("Enter a word: ")
#
# vowels = "аеёиоуыэюя"
# v = 0
# c = 0
#
# for i in word:
#     if i in vowels:
#         v += 1
#     elif i.isalpha():
#         c += 1
#
# print("Гласных: ", v)
# print("Согласных: ", c)

"""
5. Списки (Lists)
Общие элементы: Даны два списка. Создайте новый список, состоящий из 
элементов, общих для этих двух списков (исключив дубликаты).
Максимум и минимум: Найдите наибольший и наименьший элемент в списке, 
не используя встроенные функции max() и min(). 
"""

# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
#
# result = []
#
# for el in list1:
#     if el in list2 and el not in result:
#         result.append(el)
#            #el not in result нужен чтобы не было повторов (дубликатов).
# print(result)

# numbers = [5, 6, 2, 7]
#
# max_num = numbers[0]
# min_num = numbers[0]
#
# for el in numbers:
#     if el > max_num:
#         max_num = el
#     if el < min_num:
#         min_num = el
#
# print(max_num)
# print(min_num)

"""
6. Словари (Dictionaries)
Частотный словарь: Подсчитайте количество вхождений каждого слова в 
предложении.
"""

# text = input("Enter sentence: ")
#
# words = text.split()
#
# freq = {}
#
# for word in words:
#     if word in freq:
#         freq[word] += 1
#     else:
#         freq[word] = 1
#
# print(freq)

"""
Необходимо в вашем репозитории с домашними заданиями создать ветку hw_5 в ней выполнить 
домашнее задание и затем слить в ветку master.
1. Создайте игру "Угадай число", в которой игрок должен угадать случайное число в заданном 
диапазоне, делая ставки на каждое число. Если игрок угадывает число, он удваивает ставку, если нет, 
он теряет ставку. Диапазон чисел, количество попыток для угадывания и начальный капитал должны считываться из конфигурационного файла. 
2. Программа должна быть разделена на несколько модулей.
3. Установите библиотеку python-decouple в виртуальную среду вашего проекта.
4. Создайте файл requirements.txt и зафиксируйте зависимости проекта с помощью команды pip freeze.
5. Создайте файл settings.ini и укажите в нем диапазон чисел, количество попыток и начальный капитал.
6. Создайте основной модуль для запуска игры (main.py).
7. Создайте модуль с логикой игры (logic.py).

main.py — entry point for the Guess the Number betting game.
 
Rules:
  - A secret number is chosen within [MIN_NUMBER, MAX_NUMBER].
  - Each turn the player places a bet, then guesses the number.
  - Correct guess → equity increases by the bet amount.
  - Wrong guess   → equity decreases by the bet amount.
  - The game ends when the player runs out of attempts, runs out of money,
    or correctly guesses the number.
"""

from config import INITIAL_EQUITY, MAX_ATTEMPTS
from logic import(
    generate_secret_number,
    validate_bet,
    validate_guess,
    resolve_round,
    is_game_over,
    build_status,
)


def get_int_input(prompt: str) -> int | None:
    """Prompt the user for an integer; return None on non-numeric input."""
    raw = input(prompt).strip()
    try:
        return int(raw)
    except ValueError:
        print('Please enter a whole number.')
        return None


def play_game() -> None:
    print("\n========================================")
    print("   Welcome to Guess the Number!")
    print("========================================")
    print(f"  Starting equity : ${INITIAL_EQUITY}")
    print(f"  Attempts        : {MAX_ATTEMPTS}")
    print("  Double your bet on a correct guess,")
    print("  lose your bet on a wrong guess.\n")

    secret = generate_secret_number()
    equity = INITIAL_EQUITY
    attempts_left = MAX_ATTEMPTS

    while True:
        # Show current status
        print(build_status(equity, attempts_left))

        # --- Collect bet ---
        bet = None
        while bet is None:
            bet = get_int_input(' Enter your bet: $')
            if bet is not None:
                error = validate_bet(bet, equity)
                if error:
                    print(f' {error}')
                    bet = None

        # --- Collect guess ---
        guess = None
        while guess is None:
            guess = get_int_input(' Enter your guess: ')
            if guess is not None:
                error = validate_guess(guess)
                if error:
                    print(f' {error}')
                    guess = None

        # --- Resolve the round ---
        equity, message = resolve_round(guess, secret, bet, equity)
        print(f' \n {message}')
        attempts_left -= 1

        # --- Check game-over conditions ---
        ended, reason = is_game_over(equity, attempts_left)
        if ended:
            print(f'\n  {reason}')
            print(f'  The secret number was: {secret}')
            print(f'  Final equity: ${equity}')
            break

    print("\n========================================\n")


def main() -> None:
    while True:
        play_game()
        again = input('Play again? (y/n): ').strip().lower()
        if again != 'y':
            print('Thanks for playing! Goodbye.')
            break


if __name__ == '__main__':
    main()