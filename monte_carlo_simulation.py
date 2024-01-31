"""

Завдання 7: Використання методу Монте-Карло

Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків.
Обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.
Створіть симуляцію, де два кубики кидають велику кількість разів.
Для кожного кидка визначте суму чисел, які випали на обох кубиках.
Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції.
Використовуючи ці дані, обчисліть імовірність кожної суми.

Створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.

"""

import random
import matplotlib.pyplot as plt
from collections import Counter
from tabulate import tabulate


def throw_dice():
    """Симуляція кидка кубика."""
    return random.randint(1, 6)


def simulate_dice_rolls(num_trials):
    """Метод Монте-Карло для симуляції кидка двох кубиків."""
    results = [throw_dice() + throw_dice() for _ in range(num_trials)]
    counter = Counter(results)
    probabilities = {key: value / num_trials * 100 for key, value in counter.items()}
    return counter, probabilities


def display_results(results, probabilities, num_trials):
    """Виведення результатів симуляції."""
    table_data = []
    for total in sorted(probabilities.keys()):
        probability = probabilities[total]
        table_data.append(
            [total, f"{probability:.2f}% ({results[total]}/{num_trials})"]
        )

    headers = ["Сума", "Імовірність"]
    print(tabulate(table_data, headers, tablefmt="grid"))


def plot_results(probabilities):
    """Побудова графіку імовірностей."""
    fig, ax = plt.subplots()
    bars = ax.bar(
        probabilities.keys(), probabilities.values(), color="skyblue", edgecolor="black"
    )

    for bar in bars:
        yval = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            yval,
            f"{yval:.2f}%",
            ha="center",
            va="bottom",
        )

    plt.xlabel("Сума")
    plt.ylabel("Імовірність")
    plt.title("Імовірності сум при киданні двох кубиків (Метод Монте-Карло)")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show(block=False)


def get_num_trials():
    """Отримати кількість кидків кубиків від користувача."""
    while True:
        try:
            num_trials = int(input("Введіть кількість кидків кубиків: "))
            if num_trials > 0:
                return num_trials
            else:
                print("Будь ласка, введіть додатне число.")
        except ValueError:
            print("Будь ласка, введіть ціле число.")


def main():
    num_trials = get_num_trials()
    results, probabilities = simulate_dice_rolls(num_trials)
    display_results(results, probabilities, num_trials)
    plot_results(probabilities)


if __name__ == "__main__":
    main()
