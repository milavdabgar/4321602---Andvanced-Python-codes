import turtle

# Create a turtle object
t = turtle.Turtle()

# Function to draw a square
def draw_square():
    side_length = float(input("Enter the side length of the square: "))
    for _ in range(4):
        t.forward(side_length)
        t.left(90)

# Function to draw a rectangle
def draw_rectangle():
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

# Function to draw a circle
def draw_circle():
    radius = float(input("Enter the radius of the circle: "))
    t.circle(radius)

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