#      - shapes.py
#          * Define at least three classes: Rectangle, Circle, Triangle
#          * Each class should have attributes, area() method, and describe() method

class Rectangle:
    """
    A rectangle shape defined by width and height.

    Attributes:
        width (int): how wide the rectangle is
        height (int): how tall the rectangle is
    """

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def areaR(self) -> int:
        """
        Compute the area of this rectangle.

        Returns:
            int: the area (width * height)
        """
        return self.width * self.height

    def describe(self) -> None:
        """
        Print a description of the rectangle.

        Returns:
            None
        """
        print(f"Rectangle {self.width} by {self.height} has area {self.areaR()}")
class Circle:
    """
    A circle shape defined by radius.

    Attributes:
        radius (int): the radius of the circle
    """

    def __init__(self, radius: int):
        self.radius = radius

    def area(self) -> int:
        """
        Compute the area of this rectangle.

        Returns:
            int: the area (width * height)
        """
        return self.radius * self.radius * 3.14

    def describe(self) -> None:
        """
        Print a description of the circle.

        Returns:
            None
        """
        print(f"Circle of radius {self.radius()} has area {self.area()}")
class Triangle:
    """
    A triangle shape defined by base and height.

    Attributes:
        base (int): the base of the triangle
        height (int): the height of the triangle
    """

    def __init__(self, base: int, heightT: int):
        self.base = base
        self.height = heightT

    def area(self) -> int:
        """
        Compute the area of this rectangle.

        Returns:
            int: the area (width * height)
        """
        return 0.5 * self.base * self.heightT

    def describe(self) -> None:
        """
        Print a description of the triangle.

        Returns:
            None
        """
        print(f"Triangle with base {self.base} and height {self.heightT} has area {self.area()}")