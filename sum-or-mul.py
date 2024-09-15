# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

def product(x, y):
        product = x*y
        if (product > 1000):
                return x + y
        else:
                return product

x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))

s = product(x,y)
print(s)
