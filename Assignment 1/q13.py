num = int(input("Enter a five-digit number: "))
digit1 = (num // 10000 + 1) % 10
digit2 = (num // 1000 % 10 + 1) % 10
digit3 = (num // 100 % 10 + 1) % 10
digit4 = (num // 10 % 10 + 1) % 10
digit5 = (num % 10 + 1) % 10
new_num = digit1 * 10000 + digit2 * 1000 + digit3 * 100 + digit4 * 10 + digit5
print("New number:", new_num)
