side1 = float(input("Enter the first side: "))
side2 = float(input("Enter the second side: "))
side3 = float(input("Enter the third side: "))

if side1 == side2 == side3:
    print("Equilateral triangle")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles triangle")
elif (side1 ** 2 == side2 ** 2 + side3 ** 2 or 
      side2 ** 2 == side1 ** 2 + side3 ** 2 or 
      side3 ** 2 == side1 ** 2 + side2 ** 2):
    print("Right-angled triangle")
else:
    print("Scalene triangle")
