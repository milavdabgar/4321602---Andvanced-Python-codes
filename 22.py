import turtle

# Create a turtle object
t = turtle.Turtle()

# Function to draw a color-filled square
def draw_square():
    side_length = float(input("Enter the side length of the square: "))
    color = input("Enter the fill color for the square: ")
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(side_length)
        t.left(90)
    t.end_fill()

# Function to draw a color-filled rectangle
def draw_rectangle():
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))
    color = input("Enter the fill color for the rectangle: ")
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Function to draw a color-filled circle
def draw_circle():
    radius = float(input("Enter the radius of the circle: "))
    color = input("Enter the fill color for the circle: ")
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Function to display the menu and get user choice
def display_menu():
    print("Shape Drawing Menu:")
    print("1. Square")
    print("2. Rectangle")
    print("3. Circle")
    print("4. Quit")
    choice = input("Enter your choice (1-4): ")
    return choice

# Main program loop
while True:
    choice = display_menu()

    if choice == '1':
        draw_square()
    elif choice == '2':
        draw_rectangle()
    elif choice == '3':
        draw_circle()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")

    # Move the turtle to a new position
    t.penup()
    t.goto(0, 0)
    t.pendown()

# Hide the turtle
t.hideturtle()

# Keep the window open until closed manually
turtle.done()