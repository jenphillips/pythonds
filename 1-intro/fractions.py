def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn

    return n


class Fraction():

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return '%d/%d' % (self.num, self.den)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __add__(self, f2):
        assert(isinstance(f2, Fraction))

        common_den = self.den * f2.den
        f1num = self.num * f2.den
        f2num = f2.num * self.den

        new_num = f1num + f2num

        result = Fraction(new_num, common_den)
        # print 'result: '
        # print result

        result.reduce()

        # reduced_result = result.reduce()
        # print 'reduced result:'
        # print reduced_result

        # return reduced_result
        return result

    def __mul__(self, f2):
        assert(isinstance(f2, Fraction))

        new_num = self.num * f2.num
        new_den = self.den * f2.den

        return Fraction(new_num, new_den).reduce()

    def reduce(self):
        # Find greatest common divisor of numerator & denominator.

        g = gcd(self.num, self.den)
        self.num = self.num // g  # Why isn't it enough to just change these attributes?
        self.den = self.den // g

        # return Fraction(self.num // g, self.den // g)
