from game.ship import Enemy, Weapon
from divers.Vector import Vector 

class Stage:
    def __init__(self, board, enemySprite, weaponSprite):
        self.board = board
        # self.ennemies = []
        self.numStage = 0
        
        self.enemySprite = enemySprite
        self.weaponSprite = weaponSprite

        
    def generateStage(self):
        # create ennemies evenly separated on the screen with a speed function of numStage    
        # weaponsprite =
        enemyWeapon = Weapon(10, self.weaponSprite)
        # enemySprite = self.load_manager.get_resource('enemy')
        for i in range(3):
            for j in range(5):
                e = Enemy(self.board, 1, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), enemyWeapon, self.enemySprite, self.calculateSpeed())
                self.board.entities.append(e)
                # self.ennemies.append(e)
                
    def calculateSpeed(self):
        return Vector(3 + self.numStage, 0)
    
    
    def manageEnemiesMoves(self):
        e = self.getAllEnemies()
        # print(len(e))
        for i in e:
            print(i.outOfBoard())
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
        return self.getAllEnemies() == []
    

    def nextStage(self):
        self.numStage += 1
        self.generateStage()
        
        
    def changeStates(self):
        self.manageEnemiesMoves()
        if self.isStageFinished():
            self.nextStage()
            
    def getAllEnemies(self):
        res = []
        for i in self.board.entities:
            if isinstance(i, Enemy):
                res.append(i)
        return res
    
    def reset(self):
        """
        Réinitialise le gestionnaire de stage.
        """
        self.numStage = 0
        self.generateStage()