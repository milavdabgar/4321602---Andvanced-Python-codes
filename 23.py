import turtle

# Function to draw a smiling face emoji
def draw_face():
    # Draw face
    turtle.penup()
    turtle.goto(0, -100)
    turtle.pendown()
    turtle.circle(100)

    # Draw eyes
    turtle.penup()
    turtle.goto(-40, 30)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(40, 30)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()

    # Draw mouth
    turtle.penup()
    turtle.goto(-40, -10)
    turtle.pendown()
    turtle.setheading(-60)
    turtle.circle(45, 120)

# Function to draw a rainbow
def draw_rainbow():
    # Draw the rainbow
    turtle.penup()
    turtle.goto(-300, -300)
    turtle.pendown()
    turtle.width(10)
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    for color in colors:
        turtle.color(color)
        turtle.circle(300, 60)
        turtle.right(90)

def main():
    turtle.speed(0)
    turtle.bgcolor('lightblue')
    turtle.title("Smiling Face Emoji & Rainbow")

    while True:
        print("Choose what to draw:")
        print("1. Smiling Face Emoji")
        print("2. Rainbow")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            turtle.clear()
            draw_face()
        elif choice == '2':
            turtle.clear()
            draw_rainbow()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    turtle.done()

if __name__ == "__main__":
    main()
