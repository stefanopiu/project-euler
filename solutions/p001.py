"""
Author: Stefano Piu

Project Euler - Problem 001

Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

tot = 0 # The int that will contain the sum

# A loop that checks whether a number is a multiple of 3 or 5 and creates the sum
# and adds it to the total if it ise of integers from 1 to 1000
for number in range(1,1000):
    if number % 3 == 0 or number % 5 == 0:
        tot += number
        
print("Problem 001:", tot)
