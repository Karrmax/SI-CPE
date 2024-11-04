class vector:
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    
    def prods(self,vector2):
        return self.x+vector2[0],self.y+vector2[1]