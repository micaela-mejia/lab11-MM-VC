"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def add(a, b): 
    return a + b

def subtract(a,b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b): #raise ZeroDivisionError if a == 0
    if a == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return b / a

def logarithm(a, b): #use math library/raise ValueError
    if b <= 0:
        raise ValueError("Logarithm argument must be postive.")
    if a <= 0 or a == 1:
        raise ValueError("Logarithm base must be postive and not 1.")
    return math.loga (b)

def exponent(a, b): 
    return a ** b



