#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import sub, add, mul, div

    argc = len(sys.argv) - 1
    if argc != 3:
        print("./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a, b, operator = int(sys.argv[1]), int(sys.argv[3]), sys.argv[2]
    if operator not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    elif argc == 3:
        if operator == '+':
            print("{} {} {} = {}".format(a, operator, b, add(a, b)))
        elif operator == '-':
            print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
        elif operator == '*':
            print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
        elif operator == '/':
            print("{} {} {} = {}".format(a, operator, b, div(a, b)))
