"""
Defines the perform_operation function to execute basic arithmetic operations.
"""

def perform_operation(num1: float, num2: float, operation: str) -> float or str:
    """
    Performs a basic arithmetic operation (add, subtract, multiply, or divide) 
    on two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The operation to perform. Accepts 'add', 'subtract', 
                         'multiply', or 'divide'.

    Returns:
        float or str: The result of the operation, or the string 
                      "Division by zero is not allowed" for division by zero.
    """
    
    # Normalize the operation string to handle potential casing differences
    operation = operation.strip().lower()
    
    if operation == 'add':
        return num1 + num2
    
    elif operation == 'subtract':
        return num1 - num2
        
    elif operation == 'multiply':
        return num1 * num2
        
    elif operation == 'divide':
        # Handle division by zero
        if num2 == 0:
            # Return a specific string for the main.py script to display
            return "Division by zero is not allowed"
        else:
            return num1 / num2
            
    else:
        # Handle unsupported operations gracefully
        return f"Unsupported operation: {operation}"

# Note: The provided main.py script will be used for testing this function.
# Example of how it works:
# result = perform_operation(10, 5, 'divide')  # result is 2.0
# result_zero = perform_operation(10, 0, 'divide') # result_zero is "Division by zero is not allowed"
    