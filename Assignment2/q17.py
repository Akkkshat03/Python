time = float(input("Enter the time taken by the worker (in hours): "))

if 2 <= time <= 3:
    print("Highly efficient")
elif 3 < time <= 4:
    print("Needs to improve speed")
elif 4 < time <= 5:
    print("Needs training to improve speed")
else:
    print("Worker has to leave the company")
