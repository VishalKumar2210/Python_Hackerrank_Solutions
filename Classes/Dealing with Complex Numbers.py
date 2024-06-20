import math


class Complex:
    def __init__(self, real, img):
        self.r = real
        self.i = img

    def __str__(self):
        return f'{self.r:.2f}{self.i:+.2f}i'

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)

    def __sub__(self, other):
        return Complex(self.r - other.r, self.i - other.i)

    def __mul__(self, other):
        real = self.r * other.r - self.i * other.i
        img = self.r * other.i + self.i * other.r
        return Complex(real, img)

    def __truediv__(self, other):
        a, b = self, other
        real = (a.r * b.r + a.i * b.i) / (b.r ** 2 + b.i ** 2)
        img = (b.r * a.i - a.r * b.i) / (b.r ** 2 + b.i ** 2)
        return Complex(real, img)

    def mod(self):
        # by the way modulus is not a complex num
        return Complex(math.sqrt(self.r ** 2 + self.i ** 2), 0)


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')
