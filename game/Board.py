from game.ship import Element, Enemy, Weapon, Ship, Projectile
from divers.Vector import Vector 
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
        # self.wallZone = height - 25
        
        # self.setAllShooterEnnemies()
    
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
        
    # def newEntity(self, entity):
    #     self.entities.append(entity)
        
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
        
        # for i in range(len(self.ennemiesMatrix)):
        #     for j in range(len(self.ennemiesMatrix[i])):
        #         if self.ennemiesMatrix[j][i] != None:
        #             yield self.ennemiesMatrix[j][i]
        
        # reverse row and column of a matrix the matrix is not square nor rectangular
        
        
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
        # p = self.getDownestPointAliens()
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
        
    # def __del__(self):
    #     del self.width
    #     del self.height
    #     del self.entities
    #     del self.col
    #     del self.load_manager
            
    # def loadStage(self):
    #     self.removeALLExceptMainShip()
    #     if self.numStage == 0:
    #         weaponsprite = self.load_manager.get_resource('fire')
    #         enemyWeapon = Weapon(10, weaponsprite)
    #         enemySprite = self.load_manager.get_resource('enemy')
    #         for i in range(3):
    #             for j in range(6):
    #                 e = Enemy(self, 1, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), enemyWeapon, enemySprite, Vector(3, 0))
    #                 self.entities.append(e)
                    
    #     if self.numStage == 1:
    #         weaponsprite = self.load_manager.get_resource('fire')
    #         enemyWeapon = Weapon(10, weaponsprite)
    #         enemySprite = self.load_manager.get_resource('enemy')
    #         for i in range(3):
    #             for j in range(6):
    #                 e = Enemy(self, 1, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), enemyWeapon, enemySprite)
    #                 self.entities.append(e)
            
    # def loadEnemies(self, enemies):
    #     pass
        
        
    # def removeALLExceptMainShip(self):
    #     for i in self.entities:
    #         if not isinstance(i, Ship):
    #             self.remove(i)
                
    # # def isStageFinished(self):
    # #     for i in self.entities:
    # #         if isinstance(i, Enemy):
    # #             return 
    # #     return True
    
    # # def nextStage(self):
    # #     self.numStage += 1
    # #     self.loadStage()
        
    # def getAllEnemies(self):
    #     res = []
    #     for i in self.entities:
    #         if isinstance(i, Enemy):
    #             res.append(i)
    #     return res
        
