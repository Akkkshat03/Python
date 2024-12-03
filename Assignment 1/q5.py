length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
radius = float(input("Enter the radius of the circle: "))

area_rectangle = length * breadth
perimeter_rectangle = 2 * (length + breadth)
area_circle = 3.14159 * radius * radius
circumference_circle = 2 * 3.14159 * radius

print("Area of Rectangle:", area_rectangle)
print("Perimeter of Rectangle:", perimeter_rectangle)
print("Area of Circle:", area_circle)
print("Circumference of Circle:", circumference_circle)
