# pyvectors

Python module for vectors.
This module has 2 specific vector objects ([`Vector2`](https://github.com/Willytcat/pyvectors?tab=readme-ov-file#vector2), [`Vector3`](https://github.com/Willytcat/pyvectors?tab=readme-ov-file#vector3)) inherited from a base class ([`Vector`](https://github.com/Willytcat/pyvectors?tab=readme-ov-file#vector)).

## 'Vector'
Base class. Components are not named and can be in a infinite number with a minimum of 2.
Provides all mathematical operations and comparisons, error handling, etc.

Be careful, most of methods, operations and comparisons (except '==') will throw and error if performed on vectors with a different numbers of components.

**Properties:**
- `Vector.components` tuple containing the vector components
- `Vector.magnitude` float representing the length of the vector
- `Vector.unit` vector with a magnitude of 1

**Methods:**
- `Vector.dot(other: Vector) -> float` returns the dot product of self with other
- `Vector.scale(k: int|float) -> ` returns self scaled by a scalar k
- `Vector.compatible(other: Vector)` returns True if self and other are compatible
- `Vector.copy(other: Vector)` copy data from other vector
- `Vector.ExceptionPrint() -> string` returns a str representing the vector (used for errors)


## 'Vector2'
Inherit from [`Vector`](https://github.com/Willytcat/pyvectors?tab=readme-ov-file#vector). Adds two named components (x, y) and therefore components are of a fixed size of 2.

**Class Properties:**
- `Vector2.xAxis` Vector2(1)
- `Vector2.yAxis` Vector2(0, 1)
- `Vector2.one` Vector2(1, 1)

**Properties:**
- All properties inherited from [`Vector`](https://github.com/Willytcat/pyvectors?tab=readme-ov-file#vector)
- `Vector2.x` x component of self
- `Vector2.y` y component of self
- `Vector2.vComponents` returns components as vectors (one for each axis)

**Methods:**
- All methods inherited from [`Vector`](https://github.com/Willytcat/pyvectors?tab=readme-ov-file#vector)


## 'Vector3'
Inherit from [`Vector`](https://github.com/Willytcat/pyvectors?tab=readme-ov-file#vector). Adds three named components (x, y, z) and therefore components are of a fixed size of 3.


**Class Properties:**
- `Vector3.xAxis` Vector3(1)
- `Vector3.yAxis` Vector3(0, 1)
- `Vector3.zAxis` Vector3(0, 0, 1)
- `Vector3.one` Vector3(1, 1, 1)

**Properties:**
- All properties inherited from [`Vector`](https://github.com/Willytcat/pyvectors?tab=readme-ov-file#vector)
- `Vector3.x` x component
- `Vector3.y` y component
- `Vector3.z` z component
- `Vector3.vComponents` returns components as vectors (one for each axis)

**Methods:**
- All methods inherited from [`Vector`](https://github.com/Willytcat/pyvectors?tab=readme-ov-file#vector)
- `Vector3.cross(other)` returns the cross product of self by other


