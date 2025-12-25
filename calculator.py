def add(a, b):
    return a + b

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
