# pyvectors

Python module for vectors.
This module has 2 specific vector objects ('Vector2', 'Vector3') inherited from a base class ('Vector').

## Vector object
Base class. Components are not named and can be in a infinite number with a minimum of 2.
Provides all mathematical operations and comparisons, error handling, etc.

Be careful, most of methods, operations and comparisons (except '==') will throw and error if performed on vectors with a different numbers of components.

Properties:
- `Vector.components` tuple containing the vector components
- `Vector.magnitude` float representing the length of the vector
- `Vector.unit` vector with a magnitude of 1

Methods:
- `Vector.dot(other: Vector) -> float` returns the dot product of self with other
- `Vector.scale(k: int|float) -> ` returns self scaled by a scalar k
- `Vector.compatible(other: Vector)` returns True if self and other are compatible
- `Vector.copy(other: Vector)` copy data from other vector
- `Vector.ExceptionPrint() -> string` returns a str representing the vector (used for errors)

## Vector2 object
Inherit from vector. Adds two named components (x, y) and therefore components are of a fixed size of 2.

Properties:
- All properties inherited from Vector
- `Vector2.x` x component of self
- `Vector2.y` y component of self
- `Vector2.vComponents` returns components as vectors (one for each axis)

Methods:
- All methods inherited from Vector
