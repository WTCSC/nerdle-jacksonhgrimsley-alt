import random

def generate_numbers_for_addition():
    answer = random.randint(20, 99) #Ensures answer can't be over 99
    num1 = random.randint(10, answer-10)
    num2 = answer - num1
    return (num1, num2, answer)

def generate_numbers_for_subtraction():
    answer = random.randint(-89, 99) 
    if answer >= 0:
        num1 = random.randint(answer+10, 99)
        num2 = answer - num1
        return (num1, num2, answer)
    else:
        num1 = random.randint(0, 99-answer)
        num2 = answer + num1
        return (num1, num2, answer)

def generate_numbers_for_multiplication():
    answer = random.randint(10, 99)
    num1 = random.randint(0, answer-9, answer)
    if num1 == 0:
        num1 = 1
    num2 = answer/num1
    return (num1, num2, answer)

def generate_numbers_for_division():
    answer = random.randint(1, 9)
    num1 = random.randint(int(99/answer) + 1, 99)
    num2 = num1*answer
    return (num1, num2, answer)
    
################################################################################
#  DO NOT EDIT BELOW THIS LINE, THESE FUNCTIONS ARE ALREADY COMPLETED FOR YOU  #
################################################################################

def generate_equation():
    """
    Generate a random math equation for the Nerdle game.
    
    Returns:
        str: A string representing a math equation (exactly 8 characters)
        
    Example return values:
        "12+34=46"
        "56-23=33" 
        "9*12=108" (Wait, this is 8 chars! 9*12=108)
        "84/4=21 " (This is 7 chars, need to pad or adjust)
    
    The equation will always be exactly 8 characters long and mathematically correct.
    """
    # Choose a random operation
    operations = ['+', '-', '*', '/']
    operation = random.choice(operations)
    
    # Generate numbers based on the operation
    if operation == '+':
        num1, num2, result = generate_numbers_for_addition()
        equation = f"{num1}+{num2}={result}"
    elif operation == '-':
        num1, num2, result = generate_numbers_for_subtraction()
        equation = f"{num1}-{num2}={result}"
    elif operation == '*':
        num1, num2, result = generate_numbers_for_multiplication()
        equation = f"{num1}*{num2}={result}"
    else:  # operation == '/'
        num1, num2, result = generate_numbers_for_division()
        equation = f"{num1}/{num2}={result}"
    
    # Ensure the equation is exactly 8 characters
    # If it's 7 characters, we might need to try again or adjust
    if len(equation) != 8:
        # For now, let's try again with a different operation
        return generate_equation()
    
    return equation

def validate_equation(equation):
    """
    Check if a given equation string is mathematically correct.
    
    Args:
        equation (str): The equation to validate (e.g., "12+34=46")
        
    Returns:
        bool: True if the equation is mathematically correct, False otherwise
        
    Example:
        validate_equation("12+34=46") returns True
        validate_equation("12+34=50") returns False
    """
    # Check if input is a string
    if not isinstance(equation, str):
        return False
        
    # Check if equation has the right format and length
    if len(equation) != 8:
        return False
    
    # Check if equation contains an equals sign
    if '=' not in equation:
        return False
    
    try:
        # Split the equation at the equals sign
        left_side, right_side = equation.split('=')
        
        # The right side should be the result
        expected_result = int(right_side)
        
        # Evaluate the left side of the equation
        # We need to be careful about the operation
        if '+' in left_side:
            parts = left_side.split('+')
            if len(parts) == 2:
                actual_result = int(parts[0]) + int(parts[1])
            else:
                return False
        elif '-' in left_side:
            parts = left_side.split('-')
            if len(parts) == 2:
                actual_result = int(parts[0]) - int(parts[1])
            else:
                return False
        elif '*' in left_side:
            parts = left_side.split('*')
            if len(parts) == 2:
                actual_result = int(parts[0]) * int(parts[1])
            else:
                return False
        elif '/' in left_side:
            parts = left_side.split('/')
            if len(parts) == 2:
                # Check for division by zero
                if int(parts[1]) == 0:
                    return False
                # Check if division is exact (no remainder)
                if int(parts[0]) % int(parts[1]) != 0:
                    return False
                actual_result = int(parts[0]) // int(parts[1])
            else:
                return False
        else:
            return False
        
        # Check if the calculated result matches the given result
        return actual_result == expected_result
        
    except ValueError:
        # If we can't convert strings to integers, the equation is invalid
        return False
    except ZeroDivisionError:
        # Division by zero is invalid
        return False