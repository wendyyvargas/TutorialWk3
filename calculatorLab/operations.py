# operations.py
from calculatorLab.utils import log_call

#TODO: define add, sub, mul, div functions
@log_call
def add(a, b):
    return a + b  

@log_call
def sub(a, b):
    return a - b

@log_call
def mul(a, b):
    return a * b

@log_call
def div(a, b):
    #add a case for dividing by zero
    if (b == 0) : return "undefined"
       # raise ValueError("Cannot divide by zero") 
    return a / b