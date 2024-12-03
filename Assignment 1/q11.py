amount = int(input("Enter amount to withdraw (in multiples of 10): "))
notes_100 = amount // 100
amount = amount % 100
notes_50 = amount // 50
amount = amount % 50
notes_10 = amount // 10
print("Number of 100 notes:", notes_100)
print("Number of 50 notes:", notes_50)
print("Number of 10 notes:", notes_10)
