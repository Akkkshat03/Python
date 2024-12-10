positive = negative = zeros = 0
while True:
    num = int(input("Enter a number (or -999 to stop): "))
    if num == -999:
        break
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zeros += 1
print(f"Positive: {positive}, Negative: {negative}, Zeros: {zeros}")
