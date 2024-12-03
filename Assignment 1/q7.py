num = int(input("Enter a five-digit number: "))
sum_digits = (num % 10) + (num // 10 % 10) + (num // 100 % 10) + (num // 1000 % 10) + (num // 10000)
print("Sum of digits:", sum_digits)
