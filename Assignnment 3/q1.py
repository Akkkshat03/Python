for i in range(10):
    hours_worked = int(input(f"Enter hours worked by employee {i + 1}: "))
    overtime_hours = max(0, hours_worked - 40)
    overtime_pay = overtime_hours * 12
    print(f"Employee {i + 1}: Overtime Pay = Rs. {overtime_pay}")
