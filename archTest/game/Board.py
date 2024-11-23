from game.ship import Element, Enemy, Weapon, Ship
from divers.Vector import Vector 
class Board:
    def __init__(self, width, height, loadManager, stage = 0):
        self.width = width
        self.height = height
        self.entities = []
        self.col = []
        self.numStage = stage
        self.load_manager = loadManager
        
    def remove(self, entity):
        self.entities.remove(entity)
        
    def newEntity(self, entity):
        self.entities.append(entity)
        
    def manageCollisions(self):
        col = []
        for i in range(len(self.entities) -1):
            for j in range(i + 1, len(self.entities)):
                if Element.touched(self.entities[i],  self.entities[j]):
                    col.append([self.entities[i],  self.entities[j]])
        self.col = col
        
    def colided(self, element):
        for i in self.col:
            if element in i:
                return True
            
    def colidedBy(self, element):
        for i in self.col:
            if element in i:
                return i[((i.index(element))-1)**2]
            
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
        
