numbers = []
while True:
    num = input("Enter a number (or 'done' to finish): ")
    if num.lower() == 'done':
        break
    numbers.append(int(num))
if numbers:
    print(f"Range: {max(numbers) - min(numbers)}")
else:
    print("No numbers entered.")
