// Interface definition
class Drawable:
  def draw(self):
    pass

// Base class (abstract)
class Shape(Drawable):
  def __init__(self, color):
    self.color = color

  // Abstract method (must be overridden by subclasses)
  def get_area(self):
    pass

// Subclass inheriting from Shape and implementing Drawable
class Square(Shape):
  def __init__(self, color, side_length):
    super().__init__(color)  // Call parent constructor
    self.side_length = side_length

  def draw(self):
    print(f"Drawing a square with color {self.color} and side length {self.side_length}")

  // Override inherited method
  def get_area(self):
    return self.side_length * self.side_length

// Function to read data from a file and create a Square object
def create_square_from_file(filename):
  with open(filename, 'r') as file:
    lines = file.readlines()
    color = lines[0].strip()
    side_length = int(lines[1].strip())
  return Square(color, side_length)

// Example usage
square1 = create_square_from_file("square_data.txt")
square1.draw()
print(f"Area of the square: {square1.get_area()}")

// Loop example: Print areas of 5 squares with random side lengths
from random import randint
for _ in range(5):
  side_length = randint(1, 10)
  square = Square("blue", side_length)
  print(f"Area of square with side length {side_length}: {square.get_area()}")
