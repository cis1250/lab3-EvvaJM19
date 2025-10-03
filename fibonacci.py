#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

def fibonacci_sequence():
    while True:
        user_input = input("how many terms of the fibonacci sequence do you want? ")
        if user_input.isdigit() and int(user_input) > 0:
            n = int(user_input)
            break
        else:
            print("Please enter a positive integer")

    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

fibonacci_sequence()
