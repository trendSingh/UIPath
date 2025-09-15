# A simple Python program to add two numbers provided by the user

def add_two_numbers():
    try:
        # Get user input for the two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Calculate the sum of the two numbers
        sum = num1 + num2

        # Print the result
        print(f"The sum of {{num1}} and {{num2}} is {{sum}}.")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    add_two_numbers()
