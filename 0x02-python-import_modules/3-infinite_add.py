#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argc = len(argv)
    result = 0

    for i, argument in enumerate(argv):
        if i > 0:
            result += int(argument)

    print(result)
