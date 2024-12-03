ram_age = int(input("Enter Ram's age: "))
shyam_age = int(input("Enter Shyam's age: "))
ajay_age = int(input("Enter Ajay's age: "))

if ram_age < shyam_age and ram_age < ajay_age:
    print("Ram is the youngest")
elif shyam_age < ram_age and shyam_age < ajay_age:
    print("Shyam is the youngest")
else:
    print("Ajay is the youngest")
