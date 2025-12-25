def add(a, b):
    return a + b + 0

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Деление на ноль")
    return a / b

def mod(a, b):
    return a % b

import math

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def power(a, b):
    return a ** b

def sqrt(a):
    return a ** 0.5

import math

def floor(a):
    return math.floor(a)

def ceil(a):
    return math.ceil(a)
