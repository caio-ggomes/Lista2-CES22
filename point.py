from test import test


class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def __eq__(self, point):
        """Checks if two points have the same coordinates"""
        if self.x == point.x and self.y == point.y:
            return True
        return False

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def __string__(self):
        return "({0}, {1})".format(self.x, self.y)
    
    def halfway(self, target):
        """ Return the halfway point between myself and 
        the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)
    
    def reflect_x(self):
        """Returns a new point which is the reflexion of 
        the given about the x-axis"""
        return Point(self.x, -self.y)

    def slope_from_origin(self):
        """Returns the slope of the line joining the origin
        to the point. This method will fail if the point lays
        on the y-axis(point.x = 0)"""
        if self.x != 0:
            return self.y/self.x
        else:
            return 'Not defined'

    def get_line_to(self, target):
        """Returns a tuple (a, b) that tell the coefficients
        of the line described by the point and the target.
        This method will fail if the points share the same
        x coordinate"""
        if self.x != target.x:
            a = (target.y - self.y)/(target.x - self.x)
            b = self.y - a*self.x
            return (a, b)
        else:
            return """It doesn\'t exist a line in the form y = ax + b"""


def test_suite():
    
    # Equality tests
    test(Point(3, 5) == Point(3, 5))
    test(Point(0, 0) == Point(0,0))
    test(not Point(0, 0) == Point(0, 1))
    # Reflexion tests
    test(Point(3, 5).reflect_x() == Point(3, -5))
    test(Point(3, 0).reflect_x() == Point(3, 0))
    test(not Point(3, 5).reflect_x() == Point(3, -4))
    test(not Point(3, 5).reflect_x() == Point(2, -5))
    # Slope tests
    test(Point(4, 10).slope_from_origin() == 2.5)
    test(not Point(4, 10).slope_from_origin() == 0.4)
    test(Point(1, 0).slope_from_origin() == 0)
    test(Point(0, 1).slope_from_origin() == 'Not defined')
    test(not Point(0, 1).slope_from_origin() == 999999999)
    # Line tests
    test(Point(4, 11).get_line_to(Point(6, 15)) == (2, 3))
    test(Point(0, 1).get_line_to(Point(0, 2)) == """It doesn\'t exist a line in the form y = ax + b""")

test_suite()