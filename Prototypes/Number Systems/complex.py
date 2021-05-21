#=============================================================================#
#
#    File:   complex.py
#    Author: Jack Morgan
#    Date:   May 2021
#    Description:
#        Contains the class Complex
#        Computes arithmetic operations involving complex numbers
#
#=============================================================================#


from math import sin, cos, atan, sqrt


# __all__ = ['Complex']

class Complex():
    # subclass of number class

    """
    Operations and arithmetic involving complex numbers
    Operations include:
        + -
        * /
        == !=
        abs
        repr
        str
        conjugate
        dump
    """


    def __init__(self, *args):
        # check if defined as polar coordinates
        if len(args) == 3 and args[2] == True:
            r = args[0]
            phi = args[1]
            self.real = r * cos(phi)
            self.imag = r * sin(phi)
        # for rect coordinates
        else:
            self.real = args[0]
            self.imag = args[1] if len(args) > 1 else 0


    # make the number complex, if possible
    def _correct_type(self, number):
        if isinstance(number, (float,int)):
            number = Complex(number)
        elif not (hasattr(number, 'real') and hasattr(number, 'imag')):
            raise TypeError('number must have a real and imagiary part')
        return number


    # illegal operations for complex numbers
    def _illegal(self, op):
        print(f'Unable to compute\noperation \"{op}\" illegal for complex numbers')


    ### Arithmetic Operations ###
    def __abs__(self):
        """ abs(self) """
        return sqrt(self.real**2 + self.imag**2)


    def __add__(self, other):
        """ self + other """
        other = self._correct_type(other)
        return Complex(self.real + other.real, self.imag + other.imag)


    def __radd__(self,other):
        """ other + self """
        return self.__add__(other)


    def __sub__(self, other):
        """ self - other """
        other = self._correct_type(other)
        return Complex(self.real - other.real, self.imag - other.imag)


    def __rsub__(self, other):
        """ other - self """
        return self.__sub__(other)


    def __mul__(self, other):
        """ self * other """
        other = self._correct_type(other)
        return Complex(self.real*other.real - self.imag*other.imag, self.real*other.imag + self.imag*other.real)
        # (ac-bd) + (ad+bc)i


    def __rmul__(self, other):
        """ other - self """
        return self.__mul__(other)


    def __truediv__(self, other):
        """ self / other """
        other = self._correct_type(other)
        r = float(other.real**2 + other.imag**2)
        return Complex((self.real*other.real+self.imag*other.imag)/r, (self.imag*other.real-self.real*other.imag)/r)


    def __rtruediv__(self, other):
        """ other / self """
        return self.__truediv__(other)


    def __eq__(self, other):
        """ self == other """
        other = self._correct_type(other)
        return self.real == other.real and self.imag == other.imag


    def __ne__(self,other):
        """ self != other """
        return not(self.__eq__(other))


    def __neg__(self):
        """ -self """
        return Complex(-self.real, -self.imag)


    def __pos__(self):
        """ +self """
        return Complex(+self.real, +self.imag)


    ### printing and display ###
    def __str__(self):
        """ str(self) """
        if self.imag >= 0:
            return '(%s+%sj)' % (self.real, self.imag)
        else:
            return '(%s-%sj)' % (self.real, abs(self.imag))


    def __repr__(self):
        """ repr(self) """
        return 'Complex(%s, %s)' % (self.real, self.imag)


    ### illegal operations ###
    def __gt__(self, other):
        self._illegal('>')


    def __ge__(self, other):
        self._illegal('>=')


    def __lt__(self, other):
        self._illegal('<')


    def __le__(self, other):
        self._illegal('<=')


    ### Miscellaneous Functions ###

    # find the complex conjugate of a number
    def conjugate(self):
        """ (a+b*1j).conjugate() returns (a-b*1j) """
        return Complex(self.real, -self.imag)


    def phase(self):
         """ phase(self) """
         return atan(self.imag /  self.real)


    def dump(self):
        """ dump(self) """
        return self.__dict__


    def polar(self):
        """ polar(self) """
        return (self.__abs__(), self.phase())


print(Complex(12, 5))
print(Complex(13, 0.3, True))
