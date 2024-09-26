class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def set_width(self, width):
        self._width = width
    
    def set_height(self, height):
        self._height = height
    
    def area(self):
        return self._width * self._height
    
    def perimeter(self):
        return self._width * 2 + self._height * 2
    




new_rectangle = Rectangle(2, 4)

print(new_rectangle.perimeter())
print(new_rectangle.area())




        