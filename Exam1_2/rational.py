# this code may not produce correct result format for grader
"""
2 4 1 3
"""


class Rational:
    def __init__(self, n=1, d=1):
        self.n = n
        self.d = d
        self.sn, self.sd = self.simplest_form()

    def simplest_form(self):
        if self.n == self.d:
            return 1, 1
        else:
            for i in range(max(self.d, self.n), 1, -1):
                if self.n % i == 0 and self.d % i == 0:
                    return self.n//i, self.d//i
            return self.n, self.d

    def __str__(self):
        if self.n == 0:
            return '0'
        elif self.n == self.d:
            return '1'
        else:
            return f'{self.n}/{self.d}'

    def __lt__(self, other):
        return self.n/self.d < other.n/other.d

    def __gt__(self, other):
        return self.n/self.d > other.n/other.d

    def __ge__(self, other):
        return self.n/self.d >= other.n/other.d

    def __le__(self, other):
        return self.n/self.d <= other.n/other.d

    def __eq__(self, other):
        return self.n/self.d == other.n/other.d

    def __ne__(self, other):
        return self.n/self.d != other.n/other.d

    def __add__(self, other):
        rn = (self.sn*other.sd) + (other.sn*self.sd)
        rd = self.sd*other.sd
        if rn == 0:
            return 0
        elif rn == rd:
            return 1
        else:
            result = Rational(rn, rd)
            return f'{result.sn}/{result.sd}'

    def __sub__(self, other):
        rn = (self.sn * other.sd) - (other.sn * self.sd)
        rd = self.sd * other.sd
        if rn == 0:
            return 0
        elif rn == rd:
            return 1
        else:
            result = Rational(rn, rd)
            return f'{result.sn}/{result.sd}'

    def __mul__(self, other):
        rn = self.sn * other.sn
        rd = self.sd * other.sd
        result = Rational(rn, rd)
        return f'{result.sn}/{result.sd}'

    def __truediv__(self, other):
        rn = self.sn * other.sd
        rd = self.sd * other.sn
        result = Rational(rn, rd)
        return f'{result.sn}/{result.sd}'

    def __floordiv__(self, other):
        rn = self.sn * other.sd
        rd = self.sd * other.sn
        return rn//rd


def grader():
    print(" *** Rational Calculator ***")
    print(" *        A = n1/d1        *")
    print(" *        B = n2/d2        *")
    print(" ***************************\n")

    str_in = input("Enter n1 d1 n2 d2 : ")
    n1, d1, n2, d2 = [int(e) for e in str_in.split()]
    a = Rational(n1, d1)
    b = Rational(n2, d2)
    c = Rational()  # 1/1
    print("A =", a, "\tB =", b, "\tC =", c)
    print("A < B ==> ", a < b)
    print("A > B ==> ", a > b)
    print("A <= B ==> ", a <= b)
    print("A >= B ==> ", a >= b)
    print("A == B ==> ", a == b)
    print("A != B ==> ", a != b)
    print("A + B ==> ", a + b)
    print("A - B ==> ", a - b)
    print("A * B ==> ", a * b)
    print("A / B ==> ", a / b)
    print("A // B ==> ", a // b)
    print("A + C ==> ", a + c)


if __name__ == '__main__':
    grader()
    # a = Rational(2, 4)
    # print(a.simplest_form())
