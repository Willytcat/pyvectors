import math

class vector2():
    """Two-dimension vector object"""

    x: float
    y: float
    magnitude: float

    def __init__(self, x=0, y=0):
        if isinstance(x, vector2):
            return self._copy(x)

        self.x = x
        self.y = y

        self._mag()


    def __add__(self, other):
        if isinstance(other, vector2):
            self.x = self.x + other.x
            self.y = self.y + other.y
        
        elif type(other) == int or type(other) == float:
            self.x = self.x + other
            self.y = self.y + other

        else:
            raise TypeError(f"trying to perform add on vector2 and {type(other)}")

        self._mag()

        return self

    def __sub__(self, other):
        if isinstance(other, vector2):
            self.x = self.x - other.x
            self.y = self.y - other.y
        
        elif type(other) == int or type(other) == float:
            self.x = self.x - other
            self.y = self.y - other

        else:
            raise TypeError(f"trying to perform sub on vector2 and {type(other)}")

        self._mag()

        return self

    def __mul__(self, other):
        if isinstance(other, vector2):
            self.x = self.x * other.x
            self.y = self.y * other.y
        
        elif type(other) == int or type(other) == float:
            self.x = self.x * other
            self.y = self.y * other

        else:
            raise TypeError(f"trying to perform mul on vector2 and {type(other)}")

        self._mag()

        return self
    
    def __truediv__(self, other):
        if isinstance(other, vector2):
            self.x = self.x / other.x
            self.y = self.y / other.y
        
        elif type(other) == int or type(other) == float:
            self.x = self.x / other
            self.y = self.y / other

        else:
            raise TypeError(f"trying to perform div on vector2 and {type(other)}")

        self._mag()

        return self

    def __floordiv__(self, other):
        if isinstance(other, vector2):
            self.x = self.x // other.x
            self.y = self.y // other.y
        
        elif type(other) == int or type(other) == float:
            self.x = self.x // other
            self.y = self.y // other

        else:
            raise TypeError(f"trying to perform floordiv on vector2 and {type(other)}")

        self._mag()

        return self

    def __mod__(self, other):
        if isinstance(other, vector2):
            self.x = self.x % other.x
            self.y = self.y % other.y
        
        elif type(other) == int or type(other) == float:
            self.x = self.x % other
            self.y = self.y % other

        else:
            raise TypeError(f"trying to perform mod on vector2 and {type(other)}")

        self._mag()

        return self


    def __len__(self):
        return self.magnitude

    def __abs__(self):
        return self.magnitude


    def __str__(self):
        return f"{self.x}, {self.y}"

    def __repr__(self):
        return f"vector2: x={self.x} y={self.y}"


    # Private methods
    def _copy(self, other):
        self.x = other.x
        self.y = other.y
        self.magnitude = other.magnitude

    def _mag(self):
        self.magnitude = math.sqrt((self.x**2 + self.y ** 2))


    # API methods
    def XY(self):
        return (self.x, self.y)

    def YX(self):
        return (self.y, self.x)

    def dot(self, other):
        if not isinstance(other, vector2):
            raise TypeError(f"Trying to perform dot product on vector2 and {type(other)}")
        
        return (self.x * other.x) + (self.y * other.y)

    def unit(self):
        return vector2(self) / self.magnitude



class vector3():
    """Three-dimension vector object"""

    x: float
    y: float
    z: float
    magnitude: float


    def __init__(self, x=0, y=0, z=0):
        if isinstance(x, vector3):
            return self._copy(x)

        self.x = x
        self.y = y
        self.z = z

        self._mag()

    def __add__(self, other):
        if isinstance(other, vector3):
            self.x = self.x + other.x
            self.y = self.y + other.y
            self.z = self.z + other.z
        elif type(other) == int or type(other) == float:
            self.x = self.x + other
            self.y = self.y + other
            self.z = self.z + other
        else:
            raise TypeError(f"Trying to perform add on vector3 and {type(other)}")

        self._mag()

        return self

    def __sub__(self, other):
        if isinstance(other, vector3):
            self.x = self.x - other.x
            self.y = self.y - other.y
            self.z = self.z - other.z
        elif type(other) == int or type(other) == float:
            self.x = self.x - other
            self.y = self.y - other
            self.z = self.z - other
        else:
            raise TypeError(f"Trying to perform sub on vector3 and {type(other)}")

        self._mag()

        return self

    def __mul__(self, other):
        if isinstance(other, vector3):
            self.x = self.x * other.x
            self.y = self.y * other.y
            self.z = self.z * other.z
        elif type(other) == int or type(other) == float:
            self.x = self.x * other
            self.y = self.y * other
            self.z = self.z * other
        else:
            raise TypeError(f"Trying to perform mul on vector3 and {type(other)}")

        self._mag()

        return self

    def __truediv__(self, other):
        if isinstance(other, vector3):
            self.x = self.x / other.x
            self.y = self.y / other.y
            self.z = self.z / other.z
        elif type(other) == int or type(other) == float:
            self.x = self.x / other
            self.y = self.y / other
            self.z = self.z / other
        else:
            raise TypeError(f"Trying to perform div on vector3 and {type(other)}")

        self._mag()

        return self

    def __floordiv__(self, other):
        if isinstance(other, vector3):
            self.x = self.x // other.x
            self.y = self.y // other.y
            self.z = self.z // other.z
        elif type(other) == int or type(other) == float:
            self.x = self.x // other
            self.y = self.y // other
            self.z = self.z // other
        else:
            raise TypeError(f"Trying to perform floordiv on vector3 and {type(other)}")

        self._mag()

        return self

    def __mod__(self, other):
        if isinstance(other, vector3):
            self.x = self.x % other.x
            self.y = self.y % other.y
            self.z = self.z % other.z
        elif type(other) == int or type(other) == float:
            self.x = self.x % other
            self.y = self.y % other
            self.z = self.z % other
        else:
            raise TypeError(f"Trying to perform mod on vector3 and {type(other)}")

        self._mag()

        return self

    
    def __len__(self):
        return self.magnitude

    def __abs__(self):
        return self.magnitude
    
    
    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}"

    def __repr__(self):
        return f"vector3: x={self.x} y={self.y} z={self.z}"

    
    # Private methods
    def _copy(self, other):
        self.x = other.x
        self.y = other.y
        self.z = other.z

        self.magnitude = other.magnitude

    def _mag(self):
        self.magnitude = math.sqrt(self.x**2 + self.y**2 + self.z**2)

    
    # API methods
    def XYZ(self):
        return (self.x, self.y, self.z)

    def ZYX(self):
        return (self.z, self.y, self.x)

    def unit(self):
        return vector3(self) / self.magnitude

    def dot(self, other):
        if not isinstance(other, vector3):
            raise TypeError(f"Trying to perform dot product on Vector3 and {type(other)}")

        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def cross(self, other):
        if not isinstance(other, vector3):
            raise TypeError(f"Trying to perform cross product on Vector3 and {type(other)}")

        return vector3(
            self.y*other.z - self.z*other.y, 
            self.z*other.x - self.x*other.z, 
            self.x*other.y - self.y*other.x
        )


