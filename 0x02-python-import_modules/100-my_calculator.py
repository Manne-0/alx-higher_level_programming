#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as cal
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])
    if operator == '+':
        print(f"{a} {operator} {b} = {cal.add(a, b)}")
    elif operator == '-':
        print(f"{a} {operator} {b} = {cal.sub(a, b)}")
    elif operator == '*':
        print(f"{a} {operator} {b} = {cal.mul(a, b)}")
    elif operator == '/':
        print(f"{a} {operator} {b} = {cal.div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
