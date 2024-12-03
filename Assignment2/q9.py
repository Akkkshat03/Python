length = float(input("Enter length of the rectangle: "))
breadth = float(input("Enter breadth of the rectangle: "))

area = length * breadth
perimeter = 2 * (length + breadth)

if area > perimeter:
    print("Area is greater than perimeter")
else:
    print("Area is not greater than perimeter")
