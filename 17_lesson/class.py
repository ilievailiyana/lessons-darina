# Class - data structure to bundle data and functionality together
# Class is like a blueprint for creating objects, which are instances of the class
# Classes can have attributes (variables) and methods (functions).

# Example - class Dog
# Class content is optional, you need at least 1 thing to create a class
class Dog:
    # class attribute - optional
    species = "Poodle"

    # Constructor method (initializer) - optional
    def __init__(self, name, age, gender):
        # Instance attributes
        self.name = name
        self.age = age
        # Private attribute (not accessible outside of the class)
        self._gender = gender
    
    # Instance methods / functions - optional
    def bark(self):
        return "Woof!"
    
    def eat(self, food):
        return "I'm eating " + food
    
    # Public method to get the gender
    def get_gender(self):
        return self._gender
    
    # static method - you can use the method without creating an object of type Dog
    @staticmethod
    def sleep(hours):
        return f"All dogs sleeping for {hours}"

# Create an instance of the Dog class
my_dog = Dog(name="Buddy", age=3, gender="female")
print(type(my_dog))
other_dog = Dog("Milo", 5, "male")

# Species value will be the same for all objects of the Dog class
print(my_dog.species)
print(other_dog.species)

print(my_dog.name)
print(other_dog.name)

print(my_dog.bark())
print(my_dog.eat("meat"))
print(my_dog.eat("strawberries"))

# Trying to access private attribute
print(other_dog.get_gender())

# calling static method
print(Dog.sleep(5))