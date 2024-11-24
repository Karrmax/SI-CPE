from game.ship import Enemy, Weapon, Ship
from divers.Vector import Vector 

class Stage:
    def __init__(self, board, enemySprite, weaponSprite):
        self.board = board
        # self.ennemies = []
        self.numStage = 0
        
        self.enemySprite = enemySprite
        self.weaponSprite = weaponSprite

        
    def generateStage(self):
        self.removeALLExceptShip()
        eMatrix = [[None for j in range(5)] for i in range(3)]
        # creates ennemies evenly separated on the screen with a speed function of numStage    

        enemyWeapon = Weapon(1, self.weaponSprite)
        for i in range(3):
            for j in range(5):
                e = Enemy(self.board, 1, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), enemyWeapon, self.enemySprite, self.calculateSpeed(), self.calculateProbability())
                if i == 2:
                    e.canShoot = True
                eMatrix[i][j] = e
                
        self.board.ennemiesMatrix = eMatrix
                # self.ennemies.append(e)
                
    def calculateProbability(self):
        return 0.005 + self.numStage * 0.007
    
    def calculateSpeed(self):
        return Vector(3 + self.numStage, 0)
    
    def removeALLExceptShip(self):
        self.board.ennemiesMatrix = None
        self.fire = {'ennemie':[], 'mainship':[]}
        
    
    def manageEnemiesMoves(self):
        e = self.board.getEnnemiesList()
        for i in e:
            if i.outOfBoard():
                self.reversALLMovement(e)
                self.ALLgoDown(e)
                return
            
    def reversMovement(self, e):
            e.speed = -e.speed
            
    def reversALLMovement(self, tab):
        for i in tab:
            self.reversMovement(i)
            
            
    def goDown(self, e):
            e.pos.y += e.size.y
            
    def ALLgoDown(self, tab):
        for i in tab:
            self.goDown(i)
            
    def isStageFinished(self):
        return  self.board.getEnnemiesList() == []
    

    def nextStage(self):
        self.numStage += 1
        self.generateStage()
        
        
    def changeStates(self):
        self.manageEnemiesMoves()
        if self.isStageFinished():
            self.nextStage()
            
    # def getAllEnemies(self):
    #     res = []
    #     for i in self.board.getEntities():
    #         if isinstance(i, Enemy):
    #             res.append(i)
    #     return res
    
    def reset(self):
        """
        Réinitialise le gestionnaire de stage.
        """
        self.numStage = 0
        self.generateStage()
        
    # def deletAll(self):
    #     self.ennemies = []
    #     self.ennemiesMatrix = []
    #     self.board.removeALLExceptShip()