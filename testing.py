from pyvectors import *

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

print(v1 ** 2)

# '''

# ''' V3

v3 = Vector3.zAxis
v4 = Vector3(3, 3, 3)

print(v4, repr(v4))
print(v3.cross(v4))
print(v3.dot(v4))
print(v3.unit)

# '''

# ''' V

v5 = Vector(1, 2, 3, 4)
v6 = Vector(1, 2, 3, 4.1, 5)
v7 = Vector(1, 2, 3, 4.1)

# print(v6 / v5) # TypeError: unsupported operand type(s) for /: 'Vector 5-components' and 'Vector 4-components'
# print(v5 <= v6) # TypeError: '>' not supported between instances of 'Vector 4-components' and 'Vector 5-components'

print(v5 == v6)
print(v5 < v7)
print(v5 >= v7)

# '''
