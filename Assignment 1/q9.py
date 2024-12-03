num = int(input("Enter a four-digit number: "))
first_digit = num // 1000
last_digit = num % 10
sum_digits = first_digit + last_digit
print("Sum of first and last digits:", sum_digits)
