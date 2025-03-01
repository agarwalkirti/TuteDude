#Task 1: Calculate Factorial Using a Function
#Problem Statement: Write a Python program that:
#1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
#2.   Returns the calculated factorial.
#3.   Calls the function with a sample number and prints the output.
#factorial [ n!=n*(n-1)!  , 0! = 1, 1!=1, 2!=2 3!=6 4!=24 ]
def factorial(N):
    if(N<2):
        return 1
    else:
        return N*factorial(N-1)
N=int(input("Enter a number: "))
result = factorial(N)
print("Factorial of",N, "is",result)
#Task 2: Using the Math Module for Calculations

#Problem Statement: Write a Python program that:
#1.   Asks the user for a number as input.
#2.   Uses the math module to calculate the:
#   Square root of the number
#   Natural logarithm (log base e) of the number
#   Sine of the number (in radians)
#3.   Displays the calculated results.

import math
n=int(input("Enter a number: "))
sqrt=math.sqrt(n)
log=math.log(n) #base=e
sin=math.sin(n)
print("Square root:",sqrt,"\nLogarithm:",log,"\nSine:",sin)
