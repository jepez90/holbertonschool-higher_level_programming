#!/usr/bin/python3
""" 4-main """

import sys
import os
sys.path.append(os.path.abspath('..'))
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(4, 6)
    r1.display()

    print("---")

    r1 = Rectangle(2, 2)
    r1.display()

    print("---")

    r2 = Rectangle(1, 1)
    r2.display()
