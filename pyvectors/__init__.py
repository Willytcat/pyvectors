import math
from types import GeneratorType


def isnumber(n) -> bool:
    return type(n) is int or type(n) is float

class Vector():
    """ Vector object """

    components: tuple
    magnitude: float

    def __init__(self, x=0, y=0, *components):
        if type(x) is type(self):
            return self.copy(x)

        vec = (x, y) + components
        if type(x) is GeneratorType:
            vec = tuple(x)
        
        for comp in vec:
            if not isnumber(comp):
                raise TypeError(f"invalid component type for 'Vector': {comp.__class__.__name__}, must be int / float")

        self.components = vec
        self.magnitude = math.hypot(*vec)


    # Comparisons
    def __eq__(self, other):
        if not self.compatible(other):
            return False
        
        for i, comp in enumerate(self.components):
            if comp != other.components[i]:
                return False

        return True

    # > <
    def __gt__(self, other):
        if not self.compatible(other):
            self.RaiseCoException('>', other)

        return self.magnitude > other.magnitude

    def __lt__(self, other):
        if not self.compatible(other):
            self.RaiseCoException('<', other)

        return self.magnitude < other.magnitude

    # >= <=
    def __ge__(self, other):
        if not self.compatible(other):
            self.RaiseCoException('>=', other)

        return self.magnitude >= other.magnitude

    def __le__(self, other):
        if not self.compatible(other):
            self.RaiseCoException('<=', other)

        return self.magnitude <= other.magnitude


    #Operators
    # -Vector
    def __neg__(self):
        return self.scale(-1)
    
    # +
    def __add__(self, other):
        if not self.compatible(other):
            self.RaiseOpException("+", other)
        
        bComp = other.components
        return type(self)(comp + bComp[i] for i, comp in enumerate(self.components))

    # -
    def __sub__(self, other):
        if not self.compatible(other):
            self.RaiseOpException("-", other)
        
        bComp = other.components
        return type(self)(comp - bComp[i] for i, comp in enumerate(self.components))

    # *
    def __mul__(self, other):
        if self.compatible(other):
            return type(self)(comp * other.components[i] for i, comp in enumerate(self.components))

        return self.scale(other)
    
    # int * Vector
    def __rmul__(self, other):
        return self.scale(other)
    
    # /
    def __truediv__(self, other):
        if not isnumber(other):
            if other == 1: return self
            return type(self)(comp / other for comp in self.components)

        elif not self.compatible(other):
            self.RaiseOpException("/", other)
        
        bComps = other.components
        return type(self)(comp / bComps[i] for i, comp in enumerate(self.components))

    # //
    def __floordiv__(self, other):
        if not isnumber(other):
            return type(self)(comp // other for comp in self.components)

        elif not self.compatible(other):
            self.RaiseOpException("//", other)
        
        bComps = other.components
        return type(self)(comp // bComps[i] for i, comp in enumerate(self.components))

    # %
    def __mod__(self, other):
        if not isnumber(other):
            return type(self)(comp % other for comp in self.components)

        elif not self.compatible(other):
            self.RaiseOpException("%", other)
        
        bComps = other.components
        return type(self)(comp % bComps[i] for i, comp in enumerate(self.components))

    
    # Other
    def __abs__(self):
        return self.magnitude
    
    def __len__(self):
        return len(self.components)

    def __str__(self):
        return ", ".join(str(comp) for comp in self.components)

    def __repr__(self):
        return f"{self.__class__.__name__}=({str(self)})"

    def __delattr__(self, attr: str):
        if not hasattr(type(self), attr):
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{attr}'")
        else:
            raise AttributeError(f"cannot delete '{self.__class__.__name__}' attribute")


    def ExceptionPrint(self):
        return f"Vector {len(self)}-components"

    def RaiseCoException(self, co, other):
        if isinstance(other, Vector):
            raise TypeError(" ".join((
                f"'{co}' not supported between instances of",
                f"'{self.ExceptionPrint()}' and '{other.ExceptionPrint()}'"))
            )
        else:
            raise TypeError(" ".join((
                f"'{co}' not supported between instances of",
                f"'{self.ExceptionPrint()}' and '{other.__class__.__name__}'"))
            )

    def RaiseOpException(self, op, other):
        if isinstance(other, Vector):
            raise TypeError(
                " ".join((f"unsupported operand type(s) for {op}:",
                f"'{self.ExceptionPrint()}'", 
                f"and '{other.ExceptionPrint()}'")
            ))
        
        else:
            raise TypeError(
                " ".join((f"unsupported operand type(s) for {op}:",
                f"'{self.ExceptionPrint()}'", 
                f"and '{other.__class__.__name__}'")
            ))

    
    # Public methods
    def copy(self, other):
        otherComp = other.components

        self.components = (otherComp[i] for i in range(len(self.components)))
        self.magnitude = other.magnitude

    def compatible(self, other):
        """ returns True if 'other' is a Vector 
        and has not the same number of components 
        """
        return type(self) is type(other) and len(self) == len(other)

        

    def scale(self, k):
        """ scales the vector by a scalar k """
        if not isnumber(k):
            self.RaiseOpException("*", k)

        if k == 1:
            return self
        else:
            return type(self)(comp * k for comp in self.components)

    def dot(self, other):
        """ dot product between self and 'other' vector """

        if type(self) is not type(other):
            raise TypeError(
                f"trying to perfom dot product on: '{self.__class__.__name__}' and '{other.__class__.__name__}'"
            )

        aComps = self.components
        bComps = other.components

        if len(aComps) != len(bComps):
            raise ArithmeticError(" ".join((
                    f"trying to perform dot product on '{self.__class__.__name__}s'",
                    "with different number of components"))
                )
        
        return sum(aComps[i] * bComps[i] for i in range(len(aComps)))

    @property
    def unit(self):
        """ return self with a magnitude of 1 """
        return self / self.magnitude


class Vector2(Vector):
    """ Two-dimension vector object """

    x: float
    y: float
    
    def __init__(self, x=0, y=0):
        if isinstance(x, Vector2):
            return self.copy(x)

        vec = (x, y)
        if isinstance(x, GeneratorType):
            vec = tuple(x)

        for comp in vec:
            if not isnumber(comp):
                raise TypeError(f"invalid component type for 'Vector2': {comp.__class__.__name__}, must be int / float")
        
        self.x, self.y = vec
        self.components = vec
        self.magnitude = math.hypot(*vec)


    def ExceptionPrint(self):
        return "Vector2"


    # Public methods
    def copy(self, other):
        self.x, self.y = other.x, other.y
        self.magnitude = other.magnitude
        self.components = other.components

    @property
    def vComponents(self) -> list:
        return [
            Vector2(self.x),
            Vector2(0, self.y)
        ]


class Vector3(Vector):
    """ Three-dimension vector object """

    x: float
    y: float
    z: float

    def __init__(self, x=0, y=0, z=0):
        if isinstance(x, Vector3):
            self.copy(x)

        vec = (x, y, z)
        if isinstance(x, GeneratorType):
            vec = tuple(x)

        for comp in vec:
            if not isnumber(comp):
                raise TypeError(f"invalid component type for 'Vector': {comp.__class__.__name__}, must be int / float")
            
        
        self.x, self.y, self.z = vec
        self.components = vec
        self.magnitude = math.hypot(*vec)


    def ExceptionPrint(self):
        return "Vector3"
    
    
    # Public methods
    def copy(self, other):
        self.x, self.y, self.z = other.components
        self.components = other.components
        self.magnitude = other.magnitude

    
    def cross(self, other):
        if not isinstance(other, Vector3):
            raise TypeError(" ".join((
                "trying to perform cross product on:",
                f"'Vector3' and '{other.__class__.__name__}'"))
                )

        return Vector3(
            self.y*other.z - self.z*other.y, 
            self.z*other.x - self.x*other.z, 
            self.x*other.y - self.y*other.x
        )
    
    @property
    def vComponents(self) -> list:
        return [
            Vector3(self.x),
            Vector3(0, self.y),
            Vector3(0, 0, self.z)
        ]

Vector2.xAxis = Vector2(1)
Vector2.yAxis = Vector2(0, 1)
Vector2.one = Vector2(1, 1)

Vector3.xAxis = Vector3(1)
Vector3.yAxis = Vector3(0, 1)
Vector3.zAxis = Vector3(0, 0, 1)
Vector3.one = Vector3(1, 1, 1)
