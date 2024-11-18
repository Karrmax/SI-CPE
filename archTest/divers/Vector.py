class Vector:
    
    def __init__(self,x, y) -> None:
        self.x = x
        self.y = y
    
    def prods(vector1,vector2):
        return vector1.x*vector2.x + vector1.y*vector2.y
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __add__(self, vect):
        return Vector(self.x + vect.x, self.y + vect.y)
    
    def __min__(self, vect):
        return Vector(self.x - vect.x, self.y - vect.y)
    
    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(self.x * other, self.y * other)
        
    def __rmul__(self, other):
        return self * other
        
    # def __copy__(self):
    #     cls = self.__class__
    #     result = cls.__new__(cls)
    #     result.__dict__.update(self.__dict__)
    #     return result
    #     return Vector(self.x, self.y)
        
    
NULLVECTOR = Vector(0, 0)
    