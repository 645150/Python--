# 运算符重载和str方法（toString）重载
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y
    
v1 = Vector(2, 3)
v2 = Vector(4, 5)
print(v1 + v2)
print(v1 - v2)
print(v1 * v2)

"""
相加（+）
p1 + p2
p1 .__ add __（p2）

相减（-）
p1-p2
p1 .__ sub __（p2）

相乘（*）
p1 * p2
p1 .__ mul __（p2）

求幂（**）
p1 ** p2
p1 .__ pow __（p2）

相除（/）
p1 / p2
p1 .__ truediv __（p2）

整除（//）
p1 // p2
p1 .__ floordiv __（p2）

求模 （%）
p1％p2
p1 .__ mod __（p2）

按位左移（<<）
p1 << p2
p1 .__ lshift __（p2）

按位右移（>>）
p1 >> p2
p1 .__ rshift __（p2）

按位与（and）
p1 and p2
p1 .__ and __（p2）

按位或（or）
p1 | 2
p1 .__ or __（p2）

按位异或（^）
p1 ^ p2
p1 .__ xor __（p2）

按位否（~）
〜p1
p1 .__ invert __()
"""