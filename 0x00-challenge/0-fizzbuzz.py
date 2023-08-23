#!/usr/bin/python3
""" FizzBuzz
"""
import sys


def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n according to FizzBuzz rules.

    - For multiples of three print "Fizz" instead of the number.
    - For multiples of five print "Buzz".
    - For numbers which are multiples of both three and five print "FizzBuzz".
    - Otherwise, print the number itself.
    """
    if n < 1:
        return

    for i in range(1, n + 1):
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)
