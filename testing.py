from vector import *

# ''' V2

v1 = Vector2(4, 4.1)
v2 = Vector2(2.1, 2)

print(v1 + v2)
print(v1 - v2)

print(v1 * v2)
print(3 * v2)
print(v1 / v2)
print(v1 / 3)

print(v1 // v2)
print(v1 // 3)
print(v1 % v2)
print(v1 % 3)

# '''

# ''' V3

v3 = Vector3.zAxis
v4 = Vector3(3, 3, 3)

print(repr(v3))
print(v3.cross(v4))

# '''

# ''' V

v5 = Vector(1, 2, 3, 4)
v6 = Vector(1, 2, 3, 4.1, 5)

print(v6 / v5)

print(v5 == v6)
print(v5 < v6)
print(v5 >= v6)
print(v6 + (-v5))

# '''
