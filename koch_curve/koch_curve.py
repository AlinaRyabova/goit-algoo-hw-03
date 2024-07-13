import turtle

def koch_curve(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)

def snowflake(t, length, level):
    for _ in range(3):
        koch_curve(t, length, level)
        t.right(120)

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)

    t = turtle.Turtle()
    t.speed(0)

    length = 300  # початкова довжина сторін сніжинки
    
    while True:
        try:
            level = int(input("Enter the level of recursion (0-6): "))
            if level < 0 or level > 6:
                raise ValueError("Level must be between 0 and 6")
            break
        except ValueError as e:
            print(e)

    t.penup()
    t.goto(-length/2, length/3)
    t.pendown()

    snowflake(t, length, level)

    turtle.done()

if __name__ == "__main__":
    main()
