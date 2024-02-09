# Write a python program to demonstrate exception handling.
def divide_numbers():
    try:
        # Ask the user for two numbers
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        
        # Attempt to divide the numbers
        result = numerator / denominator
        
        # Display the result
        print(f"The result is {result}")
        
    except ZeroDivisionError:
        # Handle division by zero
        print("Error: Cannot divide by zero.")
        
    except ValueError:
        # Handle if the input is not a number
        print("Error: Please enter a valid number.")
        
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Call the function to demonstrate exception handling
divide_numbers()
