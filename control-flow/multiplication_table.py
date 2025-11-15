# Multiplication table from 1 to 10

number = int(input("Enter a number: "))

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
