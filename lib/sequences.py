#!/usr/bin/env python3

def print_fibonacci(length):
    # Initialize the Fibonacci sequence list
    fibonacci = []

    # Edge cases: handle if length is 0 or 1
    if length == 0:
        print(fibonacci)
        return
    elif length == 1:
        fibonacci = [0]
        print(fibonacci)
        return

    # Start the sequence with the first two numbers
    fibonacci = [0, 1]

    # Generate the Fibonacci sequence up to the given length
    for i in range(2, length):
        next_value = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(next_value)

    # Print the resulting Fibonacci sequence
    print(fibonacci)
