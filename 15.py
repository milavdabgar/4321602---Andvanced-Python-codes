# Write a user-defined exception that could be raised when the text entered by a user Consists of less than 10 characters. in python

class TextTooShortError(Exception):
    """Exception raised for errors in the input text length.

    Attributes:
        text -- input text which caused the error
        message -- explanation of the error
    """

    def __init__(self, text, message="Text must be at least 10 characters long"):
        self.text = text
        self.message = message
        super().__init__(self.message)

# Example usage:
def check_text_length(text):
    if len(text) < 10:
        raise TextTooShortError(text)
    else:
        print("Text is long enough.")

# Test the function:
try:
    text_input = input("Enter your text: ")
    check_text_length(text_input)
except TextTooShortError as e:
    print(f"Error: {e.message} Your input was '{e.text}'.")
