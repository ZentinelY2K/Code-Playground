# Animal Inheritance in Code (6.3.3)
 
# Animal Parent Class
class Animal:
    # TODO: Initialize attributes
    def __init__(self,name,type,age):
        self.name = name
        self.type = type
        self.age = age
    # TODO: Code sleep() method
    def sleep(self):
        print(f"{self.name} is doing da' zZzZzZzZ")
    # TODO: Code eat() method
    def eat(self):
        print(f"{self.name} nom nom")
    
    def info(self):
        print(f"Hi my name is {self.name} and im a {self.type} and im {self.age} years old")


# Dog Child Class
class Dog(Animal):
    # Todo: Initialize attributes, explicitly call parent class
    def __init__(self,name,type,age,breed):
        Animal.__init__(self,name,type,age)
        self.breed = breed
    def make_sound(self):
        if self.type == "Dog":
            print("Woof")
    
    #  Todo: Code dog-specific make_sound() method

# Cat Child Class
class Cat(Animal):
    # Todo: Initialize attributes, explicitly call parent class
    def __init__(self,name,type,age,fur):
        Animal.__init__(self,name,type,age)
        self.name = name
        self.type = type
        self.age = age
        self.fur = fur
    # Todo: Code cat-specific make_sound() method
    def make_sound(self):
        print("Meow")

def main():
    # Todo: Create dog and cat objects
    animal = Animal("Anastacia","Unknown","5")
    # Dog Template: some_dog = Dog(name, age, breed)
    dog = Dog("Max","Dog","5","Chihuahua")
    # Cat Template: some_cat = Cat(name, age, fur_color)
    cat = Cat("Furball","Cat","4","White")
    # Todo: Use inherited methods
    dog.sleep()
    cat.sleep()
    dog.eat()
    cat.eat()
    # Todo: Use make_sound() (for both dogs and cats)
    dog.make_sound()
    cat.make_sound()
main()