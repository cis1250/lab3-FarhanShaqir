#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
while True:
    terms = input("Enter the number of terms you want: ")
    if terms.isdigit() and int(terms) > 0:
        terms = int(terms)
        break
    else:
        print("Please enter a positive integer.")

a = 0
b = 1

for _ in range(terms):
    print(a, end=" ")
    a, b = b, a + b

print() 
