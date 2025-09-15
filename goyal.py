def multiply_numbers(num1, num2):
    """
    Function to multiply two numbers
    
    Args:
        num1: First number
        num2: Second number
    
    Returns:
        Product of the two numbers
    """
    return num1 * num2

# Example usage
if __name__ == "__main__":
    # Get input from user
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))
        
        # Calculate the product
        result = multiply_numbers(number1, number2)
        
        # Display the result
        print(f"The product of {number1} and {number2} is: {result}")
        
    except ValueError:
        print("Please enter valid numbers!")