# -*- coding: utf-8 -*-
"""
Develop a program that asks the user for an integer 4-digit number and calculates the sum of its constituent digits. 
For example, if the user enters the number 3141, the program should output the following result:
3 + 1 + 4 + 1 = 9


"""

def sum_of_digits():
    number = input("Enter a 4-digit number: ")
    if len(number) == 4 and number.isdigit():
        digits = [int(digit) for digit in number]
        total_sum = sum(digits)
        print(" + ".join(number) + " = " + str(total_sum))
    else:
        print("Please enter a valid 4-digit number.")

sum_of_digits()
