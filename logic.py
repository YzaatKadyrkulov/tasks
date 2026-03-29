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
"""

import random
from config import MIN_NUMBER, MAX_NUMBER

def generate_secret_number() -> int:
    """Pick a random secret number within the configured range."""
    return random.randint(MIN_NUMBER, MAX_NUMBER)


def validate_bet(bet: int, equity) -> str | None:
    """Return an error message if the bet is invalid, otherwise None."""
    if bet <= 0:
        return "Bet must be a positive number."
    if bet > equity:
        return f'Bet cannot exceed your current equity (${equity}).'
    return None


def validate_guess(guess: int) -> str | None:
    """Return an error message if the guess is out of range, otherwise None."""
    if not(MIN_NUMBER <= guess <= MAX_NUMBER):
        return f'Guess must be between {MIN_NUMBER} and {MAX_NUMBER}.'
    return None

def resolve_round(guess: int, secret: int, bet: int, equity: int) -> tuple[int, str]:
    """
    Compare the guess against the secret number.

    Returns:
        (new_equity, result_message)
        - Correct guess -> equity doubles the bet (equity + bet)
        - Wrong guess -> equity loses the bet     (equity - bet)
    """
    if guess == secret:
        new_equity = equity + bet
        message = f'Correct! You won ${bet}. New equity: ${new_equity}.'
    else:
        new_equity = equity - bet
        hint = 'Too low!' if guess < secret else 'Too high!'
        message = f'Wrong! {hint} You lost ${bet}. New equity: ${new_equity}.'
    return new_equity, message


def is_game_over(equity: int, attempts_left: int) -> tuple[bool, str]:
    """
    Decide whether the game should end.

    Returns:
        (should_end, reason_message)
    """
    if equity <= 0:
        return True, 'You ran out of money. Game over!'
    if attempts_left <= 0:
        return True, 'No attempts left. Game over!'
    return False, ""


def build_status(equity: int, attempts_left: int) -> str:
    """Return a formatted status line shown before each turn."""
    return (
        f'\n{'-' * 40}\n'
        f'  Equity: ${equity}  |  Attempts left: ${attempts_left}\n'
        f'  Range: {MIN_NUMBER}-{MAX_NUMBER}\n'
        f'{'-' * 40}'
    )