basic_salary = float(input("Enter basic salary: "))
dearness_allowance = basic_salary * 40 / 100
house_rent_allowance = basic_salary * 20 / 100
gross_salary = basic_salary + dearness_allowance + house_rent_allowance
print("Gross Salary:", gross_salary)

