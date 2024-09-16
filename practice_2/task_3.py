# -*- coding: utf-8 -*-
"""
Write a program to calculate the body mass index (BMI) of a person. The user must enter their height and weight, after which you use one of the formulas below to determine the index.
BMI = weight/height**2 
"""

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height**2)

print(f"Your Body Mass Index (BMI) is: {bmi:.2f}")
