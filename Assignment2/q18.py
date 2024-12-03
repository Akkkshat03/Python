health = input("Enter health (excellent/poor): ").lower()
age = int(input("Enter age: "))
location = input("Enter location (city/village): ").lower()
sex = input("Enter sex (male/female): ").lower()

if health == "excellent" and 25 <= age <= 35 and location == "city":
    if sex == "male":
        print("Premium: Rs. 4 per thousand")
        print("Maximum policy amount: Rs. 2,00,000")
    elif sex == "female":
        print("Premium: Rs. 3 per thousand")
        print("Maximum policy amount: Rs. 1,00,000")
    else:
        print("Invalid input")
elif health == "poor" and 25 <= age <= 35 and location == "village" and sex == "male":
    print("Premium: Rs. 6 per thousand")
    print("Maximum policy amount: Rs. 10,000")
else:
    print("Not insured")
