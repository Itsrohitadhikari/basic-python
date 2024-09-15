def sum(numbers):
        a = 0
        for number in numbers:
                a = a + number
        return a

total = int(input("Enter the max number: "))
numbers = []
x = 0
i = 0
while(i<total):
        x = int(input(f"Enter Number in {i+1} place: "))
        numbers.append(x)
        i += 1

added = sum(numbers)
print(f"The Sum is {added}")
