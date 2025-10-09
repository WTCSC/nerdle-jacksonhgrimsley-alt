import random
import re

# -------------------------------
# Equation Generators
# -------------------------------

def generate_numbers_for_addition():
    while True:
        a = random.randint(0, 999)
        b = random.randint(0, 999)
        result = a + b
        equation = f"{a}+{b}={result}"
        if len(equation) == 8:
            return equation

def generate_numbers_for_subtraction():
    while True:
        a = random.randint(0, 999)
        b = random.randint(0, a)  # ensures non-negative result
        result = a - b
        equation = f"{a}-{b}={result}"
        if len(equation) == 8:
            return equation

def generate_numbers_for_multiplication():
    while True:
        a = random.randint(1, 99)
        b = random.randint(1, 99)
        result = a * b
        equation = f"{a}*{b}={result}"
        if len(equation) == 8:
            return equation

def generate_numbers_for_division():
    while True:
        b = random.randint(1, 99)
        result = random.randint(1, 99)
        a = b * result  # ensure clean division
        equation = f"{a}/{b}={result}"
        if len(equation) == 8:
            return equation

# -------------------------------
# Game Engine - Validation Logic
# -------------------------------

def is_valid_guess(guess: str) -> bool:
    # 1. Must be exactly 8 characters
    if len(guess) != 8:
        return False

    # 2. Only valid characters: digits, + - * / =
    if not re.fullmatch(r"[0-9+\-*/=]{8}", guess):
        return False

    # 3. Must have exactly one '='
    if guess.count('=') != 1:
        return False

    # 4. Split into left and right side of equation
    left, right = guess.split('=')

    # 5. Ensure both sides are not empty
    if not left or not right:
        return False

    # 6. Validate mathematical correctness
    try:
        # Evaluate left side (e.g., 12+34)
        left_result = eval(left)
        # Right side must be an integer
        right_result = int(right)
        return left_result == right_result
    except:
        return False

# -------------------------------
# Optional: Game Simulation (for Testing)
# -------------------------------

if __name__ == "__main__":
    print("Welcome to Nerdle (Console Version)")
    
    # Pick a random equation
    generators = [
        generate_numbers_for_addition,
        generate_numbers_for_subtraction,
        generate_numbers_for_multiplication,
        generate_numbers_for_division
    ]
    target_equation = random.choice(generators)()

    # Uncomment the line below for debugging/cheating
    # print(f"[DEBUG] Secret Equation: {target_equation}")

    attempts = 6
    while attempts > 0:
        guess = input(f"\nAttempt {7 - attempts}/6 - Enter your 8-char equation: ").strip()

        if not is_valid_guess(guess):
            print("Invalid guess! Ensure it's 8 characters, uses valid math, and is correct format.")
            continue

        if guess == target_equation:
            print("Correct! You guessed the equation!")
            break
        else:
            print("Valid equation, but not correct.")
            attempts -= 1

    if attempts == 0:
        print(f"Out of attempts! The correct equation was: {target_equation}")
