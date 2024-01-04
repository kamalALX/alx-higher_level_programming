#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1

    argc = len(sys.argv) - 1
    if argc != 3:
        print("./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a, b, operator = int(sys.argv[1]), int(sys.argv[3]), sys.argv[2]
    if operator not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    elif argc == 3:
        if operator == '+':
            print("{} {} {} = {}".format(a, operator, b, a + b))
        elif operator == '-':
            print("{} {} {} = {}".format(a, operator, b, a + b))
        elif operator == '*':
            print("{} {} {} = {}".format(a, operator, b, a + b))
        elif operator == '/':
            print("{} {} {} = {}".format(a, operator, b, a + b))
