#!/usr/bin/python3
import sys
from functools import reduce


def factors(n):
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__,
                      ([i, n//i]
                       for i in range(1, int(n**0.5) + 1, step)
                       if n % i == 0)))


try:
    filename = sys.argv[1]
    with open(filename, "r") as text:
        for line in text:
            try:
                line = int(line.strip())
                my_factors = factors(line)
                primes = []
                for num in my_factors:
                    if num > 1:
                        for i in range(2, int(num/2)+1):
                            if (num % i) == 0:
                                break
                        else:
                            primes.append(num)
                for i in primes:
                    found = False
                    for j in primes:
                        if i * j == line:
                            print(f"{line}={i}*{j}")
                            found = True
                            break
                    if found:
                        break
            except ValueError:
                continue
except Exception:
    pass
