#!/usr/bin/python3
import sys


def get_factors(number):
    first_factor = None
    step = 2 if number % 2 == 0 else 1
    for i in reversed(range(0, 9, step)):
        if number % 10 == 0 or number % 10 == 5:
            first_factor = 5
            break
        if number % i == 0:
            first_factor = i
            break
    second_factor = int(number / first_factor)
    return first_factor, second_factor




try:
    filename = sys.argv[1]
    with open(filename, "r") as text:
        for line in text:
            try:
                line = int(line.strip())
                a, b = get_factors(line)
                print(f"{line}={a}*{b}")
            except ValueError:
                continue
except Exception:
    pass
