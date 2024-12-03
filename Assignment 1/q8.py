num = int(input("Enter a five-digit number: "))
reversed_num = (num % 10) * 10000 + (num // 10 % 10) * 1000 + (num // 100 % 10) * 100 + (num // 1000 % 10) * 10 + (num // 10000)
print("Reversed number:", reversed_num)
