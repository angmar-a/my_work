#      - utils.py
#          * Create helper functions, e.g., convert cm^2 to m^2
#          * Compare areas of two shapes
def cm2_to_m2(area_cm2: float) -> float:
    
    return area_cm2 / 10000.0


def compare_areas(shape1, shape2) -> str:
    area1 = shape1.area()
    area2 = shape2.area()
    if area1 > area2:
        return f"The first shape is larger with an area of {area1} cm² compared to {area2} cm²."
    elif area2 > area1:
        return f"The second shape is larger with an area of {area2} cm² compared to {area1} cm²."
    else:
        return f"Both shapes have the same area of {area1} cm²."
    