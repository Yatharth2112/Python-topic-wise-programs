def calculate_area(length, width):
    area = length * width
    return area

def calculate_lenghth_only_area(length , width):
    area = length * width
    return area 

l = int(input("Enter length: "))
w = int(input("Enter width: "))
print("Area of rectangle: ", calculate_area(l,w))
print("Area of rectangle using hard input of width: ", calculate_lenghth_only_area(l, 5))

