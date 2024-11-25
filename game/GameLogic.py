from managers.InputManager import InputManager
from managers.RenderManager import RenderManager
from game.ship import Ship, Weapon, Enemy
from game.wall import Wall
from divers.Vector import Vector
from game.Board import Board
from game.StageManager import Stage
import time

## TODO : 
## BUG la partie continue apres la fin du jeu

class GameLogic:
    def __init__(self, screen, load_manager,callback_endSequence, target_fps = 60):
        self.canvas = screen.canvas
        
        self.callback_endSequence = callback_endSequence
        self.load_manager = load_manager
        self.inputManager = InputManager()
        self.renderManager = RenderManager(self.canvas, self.load_manager.get_resource('background'))
        
        self.board = Board(self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(), self.load_manager)
        
        self.stage_manager = Stage(self.board,self.load_manager.get_resource('enemy1'), self.load_manager.get_resource('fireDown'))
        self.running = False

        self.points = 0
        
        self.target_fps = target_fps
        self.frame_time = 1 / self.target_fps

        # Bind input events
        self.bindAll(screen)
        screen.focus_set()
        
    def bindAll(self, screen):
        screen.bind("<KeyPress>", self.inputManager.key_pressed)
        screen.bind("<KeyRelease>", self.inputManager.key_released)
    
    def start(self):
        self.running = True
        
        ## ajout du vaisseau main
        
        self.loadShip()
        self.loadWals()
        self.stage_manager.generateStage()
        # print(self.board.ennemiesMatrix)
        self.game_loop()
        
    def stop(self):
        self.running = False

    def game_loop(self):
        start_time = time.time()


            # return
        if self.running:

            self.changeState()
            self.update()
            self.render()
            
            if not self.board.noEnemies() and self.board.isGameFinished():
                self.endSequence()
            
            
            
            # print(self.board.isGameFinished())
            


        # Calculate time taken for this frame
        elapsed_time = time.time() - start_time
        sleep_time = max(0, self.frame_time - elapsed_time)

        # Wait until the next frame
        self.canvas.after(int(sleep_time * 1000), self.game_loop)


    def changeState(self):
        inputs = self.inputManager.get_inputs()
        self.stage_manager.changeStates()
        for entity in self.board.getEntities():
            entity.changeState(inputs)
            
    def update(self):
        self.board.manageCollisions()
        for entity in self.board.getEntities():
            entity.update()

    def render(self):
        self.renderManager.render(self.board.getEntities(), self.board)
        self.renderManager.renderInfos(self.board.points, self.stage_manager.numStage, self.board.mainShip.HP)
        
    def loadWals(self):
        wallSprite = self.load_manager.get_resource('wall')
        for i in range(3):
            self.board.walls.append(Wall(self.board, Vector(i*600 + 100, self.board.height * 4/5), Vector(150, 42), wallSprite))  
    
    def loadShip(self):
        weaponsprite = self.load_manager.get_resource('fire')
        mainWeapon = Weapon(1, weaponsprite)
        myMainSprite = self.load_manager.get_resource('ship')
        
        mainShip = Ship(self.board, 3, Vector(100, 100), Vector(60, 60), mainWeapon, myMainSprite)
        mainShip.pos.x = self.board.width/2
        mainShip.pos.y = self.board.height * 7/8
        
        self.board.mainShip = mainShip
        
    def reset(self):
        self.board.reset()
        self.stage_manager.reset()
        # print(self.stage_manager.numStage)
        self.running = False
        
    def cheatCode(self, code):
        print(code)
        if(code == "999"):
            # self.stage_manager.deletAll() 
            self.stage_manager.numStage = 10
            self.stage_manager.nextStage()
        if(code == "222"):
            self.board.mainShip.HP += 1
            
        if(code == "700"):
            self.stage_manager.numStage = 26
            self.stage_manager.nextStage()
        
    def pause(self):
        self.running = False
        
    def unPause(self):
        self.running = True
        
    def __del__(self):
        self.stop()
        del self.board
        del self.render_manager
            
    def endSequence(self):
        # print("test")
        # self.pause()
        self.callback_endSequence(self.board.points)
        
    def get_points(self):
        # print(self.board.points)
        return self.board.points
    
    def get_stage(self):
        return self.stage_manager.numStage
