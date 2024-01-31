def greedy_algorithm(food_items, budget_amount):
    sorted_items = sorted(
        food_items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )
    selected_items = []
    total_cost = 0
    total_calories = 0

    for item_name, item_info in sorted_items:
        if total_cost + item_info["cost"] <= budget_amount:
            selected_items.append(item_name)
            total_cost += item_info["cost"]
            total_calories += item_info["calories"]

    return selected_items, total_calories


def dynamic_programming(food_items, budget_amount):
    dp_table = [[0] * (budget_amount + 1) for _ in range(len(food_items) + 1)]

    for i, (item_name, item_info) in enumerate(food_items.items(), start=1):
        for w in range(budget_amount + 1):
            if item_info["cost"] <= w:
                dp_table[i][w] = max(
                    dp_table[i - 1][w],
                    dp_table[i - 1][w - item_info["cost"]] + item_info["calories"],
                )
            else:
                dp_table[i][w] = dp_table[i - 1][w]

    result = []
    w = budget_amount
    for i in range(len(food_items), 0, -1):
        if dp_table[i][w] != dp_table[i - 1][w]:
            item_name = list(food_items.keys())[i - 1]
            result.append(item_name)
            w -= food_items[item_name]["cost"]

    result.reverse()
    return result, dp_table[len(food_items)][budget_amount]


if __name__ == "__main__":
    food_items = {
        "Pizza": {"cost": 50, "calories": 300},
        "Hamburger": {"cost": 40, "calories": 250},
        "Hot-Dog": {"cost": 30, "calories": 200},
        "Pepsi": {"cost": 10, "calories": 100},
        "Cola": {"cost": 15, "calories": 220},
        "Potato": {"cost": 25, "calories": 350},
    }

    budget_amount = 80

    greedy_result, greedy_total_calories = greedy_algorithm(food_items, budget_amount)
    print(
        f"Жадібний Алгоритм: Вибрані страви - {greedy_result}, Загальні Калорії - {greedy_total_calories}, Бюджет - {budget_amount}"
    )

    dp_result, dp_total_calories = dynamic_programming(food_items, budget_amount)
    print(
        f"Динамічне програмування: Оптимальні страви - {dp_result}, Загальні Калорії - {dp_total_calories}, Бюджет - {budget_amount}"
    )
