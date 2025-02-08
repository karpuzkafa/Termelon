#Copyright 2025 Hasan Agit Ünal





import subprocess
import os
import random

def GetDir():
    """
    get project folder directory as str
    """
    os.path.dirname(os.path.abspath(__file__))

def whiteline():
    """
    Print a beautiful line.
    """
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")


def clear():
    """
    Clear the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def is_odd(number):
    """
    Check if a number is odd.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is odd, False otherwise.
    """
    return number % 2 == 1


def run(file):
    """
    Run a Python file using subprocess.

    Args:
        file (str): Path to the Python file.
    """
    subprocess.run(["python", file])


def randomize(num1, num2):
    """
    Generate a random integer between two numbers.

    Args:
        num1 (int): The lower bound.
        num2 (int): The upper bound.

    Returns:
        int: A random number between num1 and num2.
    """
    return random.randint(num1, num2)


