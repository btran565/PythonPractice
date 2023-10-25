class Rectangle:
    def __init__(self, width, height):          #constructor
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod         #classmethod decorator
    def new_square(cls, side_length):
        return cls(side_length, side_length)            #passes arguments to constructor

square = Rectangle.new_square(5)
print(square.calculate_area())