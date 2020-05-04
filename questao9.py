class GenericObject:
    
    def method(self):
        raise NotImplementedError

class GenericObject2(GenericObject):
    
    def method(self):
        raise NotImplementedError


try:
    class GenericObject4(GenericObject, GenericObject2):

        def method(self):
            raise NotImplementedError

except Exception:
    print("""Não foi possível criar um MRO consistente para bases
    GenericObject e GenericObject2\n""")


class Shape(GenericObject):
    geometric_type = 'Generic Shape'

    def area(self): # This acts as placeholder for the interface
        raise NotImplementedError

    def get_geometric_type(self):
        return self.geometric_type

class Plotter(GenericObject2):

    def plot(self, ratio, topleft):
        #Imagine some nice plotting logic here...


        print('Plotting at {}, ratio{}.'.format(
            topleft, ratio))

class Polygon(Shape, Plotter, GenericObject2):  # base class for polygons
    geometric_type = 'Polygon'

class RegularPolygon(Polygon):  # Is-A Polygon
    geometric_type = 'Regular Polygon'

    def __init__(self, side):
        self.side = side

class RegularHexagon(RegularPolygon):   # Is-A RegularPolygon
    geometric_type = 'RegularHexagon'

    def area(self):
        return 1.5 * (3 ** .5 * self.side ** 2)

class Square(RegularPolygon):   # Is-A RegularPolygon
    geometric_type = 'Square'

    def area(self):
        return self.side * self.side

def main():
    print(Square.__mro__)

main()