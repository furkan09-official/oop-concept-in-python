# A user can create and view 2D cordinate

class point:
    def __init__(self , x , y):
        self.x_cord = x
        self.y_cord = y
        # self.eucliden_distance()
    def __str__(self):
        return "<{},{}>".format(self.x_cord , self.y_cord)
    
#user can find out the distance between two points
    def eucliden_distance(self , other):
        return ((self.x_cord - other.x_cord)**2 + (self.y_cord - other.y_cord)**2)**0.5
# A user can find the distance from the origin
    def origin_distance(self):
        return (self.x_cord**2 + self.y_cord**2)**0.5
        # return self.eucliden_distance(point(0,0))    #class ke ander hi class ka ek object bna ke exicute kiya hai -> smart tarika

# p1 = point(0, 0)
# p2 = point(10,10)
# print(p1.eucliden_distance(p2))
# print(p1.origin_distance())


class Line:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
    def __str__(self):
        return '{}x + {}y + {} = 0'.format(self.A ,self.B ,self.C)
    
    def lies_on_line(Line , point):
        if Line.A*point.x_cord + Line.B * point.y_cord + Line.C == 0:
            return "Point lies on the line"
        else:
            return "Point not lies on the line"
        
    def sortest_distance(Line , point):
        return abs(Line.A*point.x_cord + Line.B*point.y_cord + Line.C)/(Line.A**2 + Line.B**2)**0.5



l1 = Line(2,1,-2)
p1 = point(1,1)

print(l1)
print(p1)
print(l1.lies_on_line(point(2,1)))     #either you can privide the p1 object or directly provide the point class parameters
        
print(l1.sortest_distance(point(3,1))) 