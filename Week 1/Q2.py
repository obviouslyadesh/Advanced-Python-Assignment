class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rect1 = Rectangle(8, 6)
print("Area of Rectangle1:", rect1.area())
print("Perimeter of Rectangle1:", rect1.perimeter())

rect2 = Rectangle(33, 14)
print("Area of Rectangle2:", rect2.area())
print("Perimeter of Rectangle2:", rect2.perimeter())
