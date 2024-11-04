class Vector:
    def __init__(self,x, y) -> None:
        self.x = x
        self.y = y
    
    def prods(vector1,vector2):
        return vector1.x*vector2.x + vector1.y*vector2.y