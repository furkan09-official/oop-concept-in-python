class Fraction:
    def __init__(self , x, y):    #this is the megic method
        self.num = x
        self.den = y
    def __str__(self):
        return '{}/{}'.format(self.num , self.den)

fr = Fraction(3, 4)
print(fr)

