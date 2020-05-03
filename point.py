class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

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
        return self.y/self.x

    def get_line_to(self, target):
        """Returns a tuple (a, b) that tell the coefficients
        of the line described by the point and the target.
        This method will fail if the points share the same
        x coordinate"""
        a = (target.y - self.y)/(target.x - self.x)
        b = self.y - a*self.x
        return (a, b)

def main():
    print((Point(3, 5).reflect_x()).__string__())
    print(Point(4, 10).slope_from_origin())
    print(Point(4, 11).get_line_to(Point(6, 15)))

main()