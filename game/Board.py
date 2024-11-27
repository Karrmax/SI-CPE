from game.Elements.Enemy import Enemy
from game.Elements.Element import Element
from game.Elements.Projectile import Projectile

class Board:
    def __init__(self, width, height, loadManager):
        self.width = width
        self.height = height
        
        self.ennemiesMatrix = None
        self.mainShip = None
        self.fire = {'ennemy':[], 'mainShip':[]}
        self.walls = []
        
        self.col = []
        self.load_manager = loadManager
        self.points = 0
        
        self.allayZone = height - 175
    
    def isInAllayZone(self, element):
        return element.pos.y > self.allayZone
    
    def getEntities(self):
        return self.getEnnemiesList() + self.fire['ennemy'] + self.fire['mainShip'] + [self.mainShip] + self.walls
    
    def getEnnemiesList(self):
        return [j for sub in self.ennemiesMatrix for j in sub]
    
    
    def remove(self, entity):
        if isinstance(entity, Enemy):
            for i in self.ennemiesMatrix:
                for j in i:
                    if j == entity:
                        i.remove(j)
                        self.setAllShooterEnnemies()
                    
        if isinstance(entity, Projectile):
            if entity.fromMainShip:
                self.fire['ennemy'].remove(entity)
            else:
                self.fire['mainShip'].remove(entity)
        
        
    def manageCollisions(self):
        col = []
        entities = self.getEntities()
        for i in range(len(entities) -1):
            for j in range(i + 1, len(entities)):
                if Element.touched(entities[i], entities[j]):
                    col.append([entities[i], entities[j]])
        self.col = col
        
    def colided(self, element):
        for i in self.col:
            if element in i:
                return True
            
    def colidedBy(self, element):
        for i in self.col:
            if element in i:
                return i[((i.index(element))-1)**2]
            
    def reset(self):
        self.ennemiesMatrix = None
        self.mainShip = None
        self.fire = {'ennemie':[], 'mainship':[]}
        self.col = []
        
    def getAllLastsEnnemiesByColumn(self):       
        matCol = self.matRowToMatColumn(self.ennemiesMatrix)
        for i in matCol:
            yield i[-1]
  
        
    def matRowToMatColumn(self, list_of_lists):
        """
        Transforms a list of lists into columns. Handles uneven row lengths.

        :param list_of_lists: A 2D list where rows may have varying lengths.
        :return: A list of lists representing columns.
        """
        columns = []
        max_length = max(len(row) for row in list_of_lists)  # Find the longest row
        for col_index in range(max_length):
            column = []
            for row in list_of_lists:
                if col_index < len(row):  # Check if the column exists in this row
                    column.append(row[col_index])
            columns.append(column)
        return columns
       
    def setAllShooterEnnemies(self): 
        for i in self.getAllLastsEnnemiesByColumn():
            i.canShoot = True
            
    def isGameFinished(self):
        return self.aliensTooDown() or not self.mainShip.isAlive()
        
        
    def aliensTooDown(self):
        return self.getDownestPointAliens().y > self.allayZone
    
    def getDownestAliens(self):
        matCol = self.matRowToMatColumn(self.ennemiesMatrix)
        lengthMax = max([len(matCol[i]) for i in range(len(matCol))])
        
        for i in matCol:
            if len(i) == lengthMax:
                return i[-1]
            
    def getDownestPointAliens(self):
        alien = self.getDownestAliens()
        return alien.pos + alien.size
    
    def noEnemies(self):
        for i in self.ennemiesMatrix:
            for j in i:
                if isinstance(j, Enemy):
                    return False
                
        return True   
