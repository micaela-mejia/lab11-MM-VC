"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# https://github.com/micaela-mejia/lab11-MM-VC
# Partner 1: Micaela Mejia
# Partner 2: Victor Corona

import math

def square_root(a): #raise ValueError if a < 0
    try:
        if a < 0:
            raise ValueError("Cannot calculate square root of 0")
        return math.sqrt(a) 
    except ValueError as e:
        raise e

def hypotenuse(a, b): #can have negative nums
    try:
        math.hypot(a, b)
    except TypeError as e:
        raise e

def add(a,b):
    return a + b

def subtract(a,b):
    return a-b

def mul(a, b):
    return a*b

def div(a,b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by 0!")
    else:
        return b/a
def logarithm(a, b):
    if b <= 0:
        raise ValueError("Logarithm argument must be positive!")
    elif a <= 0 or a == 1:
        raise ValueError("Base must be positive and greater than 1!")
    else:
        return math.log(a, b)

def exp(a, b):
    return a ** b