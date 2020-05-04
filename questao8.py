import math
import abc


class Circle(object):
    __metaclass__ = abc.ABCMeta

    radius = 0

    def __init__(self, radius = 0, center = (0, 0)):
        self.center = center
        self.radius = radius

    def __repr__(self):
        return (f'Circle({self.radius!r}), ('
                f'{self.center[0]!r}, '
                f'{self.center[1]!r})')
    
    def area(self):
        return self.static_area(self.radius)

    @classmethod
    def class_area(cls):
        return cls.radius**2 * math.pi
    
    @staticmethod
    def static_area(r):
        return r**2 * math.pi
    
    @abc.abstractmethod
    def get_colour(self):
        """Returns the colour of the circle"""


class Orangecircle(Circle):
    def get_colour(self):
        return ('orange')


def main():
    c = Circle(2, (0, 0))
    # In an instance method, each object can have different
    # outputs from the function, even if they are from the 
    # same class. The instance method requires an object to
    # be called.
    print("INSTANCE METHODS TESTS")
    print(c.area())
    try:
        print(Circle.area())
    except Exception:
        print("Deu erro")
        pass
    # A class method doesn't require the object to be executed, 
    # only the class. It doesn't matter if the objects are 
    # distinct, it will always be able to return its value. It
    # can acess information from the class but not from 
    # specific objects from that class.
    print("CLASS METHODS TESTS")
    print(c.class_area())
    print(Circle.class_area())
    # A static method doesn't require the object to be executed.
    # They don't have acess to class nor object information, 
    # working as regular functions.
    print("STATIC METHODS TESTS")
    print(c.static_area(1))
    print(Circle.static_area(1))
    # An abstract method, is a method that is not implemented 
    # in the class, but rather in those which inherit from the 
    # class
    print("ABSTRACT METHODS TESTS")
    oc = Orangecircle(1, (0, 0))
    print(c.get_colour())
    print(oc.get_colour()) 


main()