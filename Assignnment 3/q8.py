decimal = int(input("Enter a decimal number: "))
octal = ""
while decimal > 0:
    octal = str(decimal % 8) + octal
    decimal //= 8
print(f"Octal equivalent: {octal}")
