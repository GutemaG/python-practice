# to add two object (x+y) __add__
# to initializie the obj x  __init__
#x() calling object ex p1(p2) use __call__
class Polynomial:
    def __init__(self,*coeffs):
        self.coeffs=coeffs
    def __repr__(self):
        return 'polynomial(*{!r})'.format(self.coeffs)
    def __add__(self,other):
        return Polynomial(*(x+y for x,y in zip(self.coeffs,other.coeffs)))
    def __len__(self):
        return len(self.coeffs)

p1=Polynomial(1,2,3)
p2=Polynomial(3,4,3)
