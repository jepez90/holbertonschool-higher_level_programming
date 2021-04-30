#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    if 4 != len(sys.argv):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]

    operations = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
        }

    if op in operations:
        print("{} {} {} = {}".format(a, op, b, operations.get(op)(a, b)))
        quit(0)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        quit(1)
