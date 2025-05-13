

# input below
x1 = float(input("Enter x1 coordinate: "))
y1 = float(input("Enter y1 coordinate: "))
x2 = float(input("Enter x2 coordinate: "))
y2 = float(input("Enter y2 coordinate: "))

# processing below :
# calculate the power off sections first

dx_squared = (x2 - x1) ** 2
dy_squared = (y2 - y1) ** 2

# Add the squared sections together
distance_squared = dx_squared + dy_squared

# apply the sqrt for the distance squared

distance = distance_squared ** 0.5

# output
print(f"The distance between two points is : {distance}")
print("The distance between two points is: ", distance)

