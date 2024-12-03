days_late = int(input("Enter the number of days late: "))

if days_late <= 5:
    fine = days_late * 0.5
    print("Fine:", fine, "rupees")
elif days_late <= 10:
    fine = (5 * 0.5) + (days_late - 5) * 1
    print("Fine:", fine, "rupees")
elif days_late <= 30:
    fine = (5 * 0.5) + (5 * 1) + (days_late - 10) * 5
    print("Fine:", fine, "rupees")
else:
    print("Membership canceled")
