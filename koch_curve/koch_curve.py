import turtle

def koch_curve(t, order, size):
    """Функція для малювання кривої Коха за допомогою черепашки.

    Args:
        t (turtle.Turtle): Об'єкт черепашки для малювання.
        order (int): Поточний рівень рекурсії.
        size (float): Довжина сторони кривої на поточному рівні рекурсії.

    """
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def snowflake(t, order, size):
    #Функція для малювання сніжинки Коха.
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

def main():
    #Головна функція програми для малювання сніжинки Коха.
    screen = turtle.Screen()
    screen.setup(width=800, height=800)

    t = turtle.Turtle()
    t.speed(0)  # Налаштування швидкості черепашки (0 - максимальна швидкість)

    length = 300  # Початкова довжина сторін сніжинки
    
    while True:
        try:
            level = int(input("Введіть рівень рекурсії (0-6): "))
            if level < 0 or level > 6:
                raise ValueError("Рівень має бути від 0 до 6")
            break
        except ValueError as e:
            print(e)

    t.penup()
    t.goto(-length/2, length/3)
    t.pendown()

    snowflake(t, level, length)

    turtle.done()

if __name__ == "__main__":
    main()
