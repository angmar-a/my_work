#      - main.py
#          * Import classes from shapes.py
#          * Import helper functions from utils.py

#          * Allow user to create shapes (input dimensions)
#          * Print area and descriptions

from shapes import Rectangle, Circle, Triangle
from utils import cm2_to_m2, compare_areas

def create_shape():
    shape_type = input("Enter shape type (rectangle, circle, triangle): ").strip().lower()
    
    if shape_type == "rectangle":
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
        return Rectangle(width, height)
    
    elif shape_type == "circle":
        radius = int(input("Enter radius: "))
        return Circle(radius)
    
    elif shape_type == "triangle":
        base = int(input("Enter base: "))
        height = int(input("Enter height: "))
        return Triangle(base, height)
    
    else:
        print("Unknown shape type.")
        return None
def main():
    shapes = []
    
    while True:
        shape = create_shape()
        if shape:
            shapes.append(shape)
            shape.describe()
            print(f"Area in m²: {cm2_to_m2(shape.area())}")
        
        cont = input("Do you want to add another shape? (yes/no): ").strip().lower()
        if cont != "yes":
            break
    
    if len(shapes) >= 2:
        print(compare_areas(shapes[0], shapes[1]))
    
    print("Thank you for using the Shape Toolkit!")
