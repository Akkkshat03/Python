subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))
subject4 = float(input("Enter marks for subject 4: "))
subject5 = float(input("Enter marks for subject 5: "))
aggregate_marks = subject1 + subject2 + subject3 + subject4 + subject5
percentage_marks = (aggregate_marks / 500) * 100
print("Aggregate Marks:", aggregate_marks)
print("Percentage Marks:", percentage_marks)
