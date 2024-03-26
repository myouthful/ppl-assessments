class Person:
  """
  This class represents a person with attributes for name, age, and gender.
  """

  def __init__(self, name, age, gender):
    """
    This constructor initializes the Person object with the given attributes.
    """
    self.name = name
    self.age = age
    self.gender = gender

  def introduce(self):
    """
    This method prints a message introducing the person with their information.
    """
    print(f"Hello, my name is {self.name}. I am {self.age} years old and identify as {self.gender}.")

# Create an instance of the Person class
person1 = Person("Alice", 30, "female")

# Call the introduce method to display person1's information
person1.introduce()
