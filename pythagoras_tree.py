import turtle


def draw_pifagoras_tree(t, order, size):
    if order == 0:
        return
    else:
        t.forward(size)
        t.left(45)
        draw_pifagoras_tree(t, order - 1, size * 0.6)
        t.right(90)
        draw_pifagoras_tree(t, order - 1, size * 0.6)
        t.left(45)
        t.backward(size)


def get_user_input():
    while True:
        try:
            order = int(input("Введіть рівень рекурсії (ціле число більше 0): "))
            if order > 0:
                return order
            else:
                print("Будь ласка, введіть додатне число.")
        except ValueError:
            print("Будь ласка, введіть коректне ціле число.")


def main():
    order = get_user_input()

    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Дерево Піфагора")

    tree_turtle = turtle.Turtle()
    tree_turtle.speed(0)

    turtle.tracer(0, 0)

    tree_turtle.goto(0, 0)
    tree_turtle.setheading(90)

    draw_pifagoras_tree(tree_turtle, order, 200)

    turtle.update()

    window.exitonclick()


if __name__ == "__main__":
    main()
