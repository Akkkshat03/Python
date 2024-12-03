year = int(input("Enter a year: "))
days_passed = (year - 1900) + ((year - 1900) // 4) - ((year - 1900) // 100) + ((year - 1600) // 400)
day = (days_passed + 1) % 7

if day == 0:
    print("Monday")
elif day == 1:
    print("Tuesday")
elif day == 2:
    print("Wednesday")
elif day == 3:
    print("Thursday")
elif day == 4:
    print("Friday")
elif day == 5:
    print("Saturday")
else:
    print("Sunday")
