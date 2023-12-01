#!/usr/bin/python3
# 100-my_calculator.py
# Ifeanyi I Ekezie
import sys
from calculator_1 import add, sub, mul, div

def calculator():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if operator not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    c = 0
    if operator == '+':
        c = add(a, b)
    elif operator == '-':
        c = sub(a, b)
    elif operator == '*':
        c = mul(a, b)
    elif operator == '/':
        c = div(a, b)

    print(f"{a} {operator} {b} = {c}")

if __name__ == "__main__":
    calculator()
