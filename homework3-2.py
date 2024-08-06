import turtle

def draw_koch_segment(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_koch_segment(t, length, level - 1)
        t.left(60)
        draw_koch_segment(t, length, level - 1)
        t.right(120)
        draw_koch_segment(t, length, level - 1)
        t.left(60)
        draw_koch_segment(t, length, level - 1)

def draw_koch_snowflake(t, length, level):
    for _ in range(3):
        draw_koch_segment(t, length, level)
        t.right(120)

def main():
    try:
        level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        return

    # Налаштування turtle
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    t = turtle.Turtle()
    t.speed("fastest")
    t.penup()
    t.goto(-200, 100)
    t.pendown()

    length = 400  # Довжина сторони початкового трикутника

    draw_koch_snowflake(t, length, level)

    # Завершення
    screen.mainloop()  # Замість turtle.done()

if __name__ == "__main__":
    main()

