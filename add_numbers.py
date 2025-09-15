def add_two_numbers(num1, num2):
    """
    Function to add two numbers
    
    Args:
        num1: First number
        num2: Second number
    
    Returns:
        Sum of the two numbers
    """
    return num1 + num2

def main():
    # Get input from user
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        
        # Calculate sum
        result = add_two_numbers(number1, number2)
        
        # Display result
        print(f"The sum of {number1} and {number2} is: {result}")
        
    except ValueError:
        print("Please enter valid numbers!")

if __name__ == "__main__":
    main()