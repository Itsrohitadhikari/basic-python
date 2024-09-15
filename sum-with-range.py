# Sum of a Current Number and a Previous number
# Write a Python code to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number
# modified a bit to support user provided range

a = int(input("Enter the First Range Number: "))
b = int(input("Enter the Last Range Number: "))

numbers = range(a,b+1)
prev_number = 0



for number in numbers:
        print(f"Sum of {prev_number} + {number} = {prev_number + number}")
        prev_number = number
