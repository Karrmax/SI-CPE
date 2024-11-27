from game.Elements.ennemies.EnemyClassic import EnemyClassic
from game.Elements.ennemies.EnemyShooter import EnemyShooter
from game.Elements.ennemies.EnemyBoss import EnemyBoss
from game.Elements.Weapon import Weapon
from divers.Vector import Vector 
from game.Elements.wall import Wall

class Stage:
    def __init__(self, board, enemySprites):
        self.board = board
        # self.ennemies = []
        self.numStage = 0
        
        self.enemySprites = enemySprites
        # self.weaponSprite = weaponSprite

        
    def generateStage(self):
        self.removeALLExceptShip()
        eMatrix = [[None for j in range(5)] for i in range(3)]
        # creates ennemies evenly separated on the screen with a speed function of numStage    
        if self.numStage == 0:
            eMatrix = self.generateStage0(eMatrix)
        elif self.numStage == 1:
            eMatrix = self.generateStage1(eMatrix)
        elif self.numStage == 2:
            eMatrix = self.generateStage2(eMatrix)
        elif self.numStage == 3:
            eMatrix = self.generateStage3(eMatrix)
        else:
            eMatrix = self.generateClassicStage(eMatrix)
        if self.numStage != 0:
            self.board.walls.append(Wall(self.board, Vector(600 + 100, self.board.height * 4/5), Vector(150, 42), self.board.load_manager.resources['wall'])) 
        self.board.ennemiesMatrix = eMatrix
                
    def generateStage0(self, matrix):
        # matrix = matrix
        enemyWeapon = Weapon(1, self.enemySprites['fireDown'])
        for i in range(3):
            for j in range(5):
                e = EnemyClassic(self.board, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), enemyWeapon, Vector(3, 0))
                if i == 2:
                    e.canShoot = True
                matrix[i][j] = e
        return matrix
        
    def generateStage1(self, matrix):
        # matrix = matrix
        enemyWeapon = Weapon(1, self.enemySprites['fireDown'])
        for i in range(3):
            for j in range(5):
                if i == 1:
                    e = EnemyShooter(self.board, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), enemyWeapon, Vector(3, 0), self.calculateProbability())
                    e.canShoot = True
                else:
                    e = EnemyClassic(self.board, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), enemyWeapon, Vector(3, 0))
                matrix[i][j] = e
        return matrix
    
    def generateStage2(self, matrix):
        # matrix = matrix
        enemyWeapon = Weapon(1, self.enemySprites['fireDown'])
        bossWeapon = Weapon(2, self.enemySprites['fireDown'])
        for i in range(3):
            for j in range(5):
                if i == 0 and j == 2:
                    print('boss')
                    e = EnemyBoss(self.board, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), bossWeapon, Vector(3, 0), self.calculateProbability())
                    e.canShoot = True
                elif i == 1:
                    e = EnemyShooter(self.board, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), enemyWeapon, Vector(3, 0), self.calculateProbability())
                    e.canShoot = True
                else:
                    e = EnemyClassic(self.board, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), enemyWeapon, Vector(3, 0))
                matrix[i][j] = e
        return matrix
    
    def generateStage3(self, matrix):
        # matrix = matrix
        enemyWeapon = Weapon(1, self.enemySprites['fireDown'])
        bossWeapon = Weapon(2, self.enemySprites['fireDown'])
        for i in range(3):
            for j in range(5):
                if i == 0 and j == 2 or i == 0 and j == 3 or i == 0 and j == 1:
                    print('boss')
                    e = EnemyBoss(self.board, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), bossWeapon, Vector(3, 0), self.calculateProbability())
                    e.canShoot = True
                elif i == 1:
                    e = EnemyShooter(self.board, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), enemyWeapon, Vector(3, 0), self.calculateProbability())
                    e.canShoot = True
                else:
                    e = EnemyClassic(self.board, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), enemyWeapon, Vector(3, 0))
                matrix[i][j] = e
        return matrix
    
    def generateClassicStage(self, matrix):
        enemyWeapon = Weapon(1, self.enemySprites['fireDown'])
        bossWeapon = Weapon(2, self.enemySprites['fireDown'])
        for i in range(3):
            for j in range(5):
                if i == 0 :
                    # print('boss')
                    e = EnemyBoss(self.board, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), bossWeapon, self.calculateSpeed(), self.calculateProbability())
                    e.canShoot = True
                elif i == 1:
                    e = EnemyShooter(self.board, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), enemyWeapon, self.calculateSpeed(), self.calculateProbability())
                    e.canShoot = True
                else:
                    e = EnemyClassic(self.board, Vector(j * 100 + 50, i * 100 + 50), Vector(40, 40), enemyWeapon, self.calculateSpeed())
                matrix[i][j] = e
        return matrix
                
    def calculateProbability(self):
        return 0.005 + self.numStage * 0.007
    
    def calculateSpeed(self):
        return Vector(self.numStage, 0)
    
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