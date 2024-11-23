from managers.InputManager import InputManager
from managers.RenderManager import RenderManager
from game.ship import Ship, Weapon, Enemy
from divers.Vector import Vector
from game.Board import Board
from game.StageManager import Stage
import time

class GameLogic:
    def __init__(self, screen, load_manager, target_fps = 60):
        self.canvas = screen.canvas
        
        self.load_manager = load_manager
        self.inputManager = InputManager()
        self.renderManager = RenderManager(self.canvas)
        
        self.board = Board(self.canvas.winfo_reqwidth(), self.canvas.winfo_reqheight(), self.load_manager)
        
        
        
        
        
        self.stage_manager = Stage(self.board,self.load_manager.get_resource('enemy'), self.load_manager.get_resource('fire'))
        self.running = False

        
        self.target_fps = target_fps
        self.frame_time = 1 / self.target_fps

        # Bind input events
        screen.bind("<KeyPress>", self.inputManager.key_pressed)
        screen.bind("<KeyRelease>", self.inputManager.key_released)
        screen.focus_set()

    def start(self):
        self.running = True
        
        ## ajout du vaisseau main
        
        self.loadShip()
        self.game_loop()

    def stop(self):
        self.running = False

    def game_loop(self):
        start_time = time.time()
        
        if self.running:
            self.changeState()
            self.update()
            self.render()


        # Calculate time taken for this frame
        elapsed_time = time.time() - start_time
        sleep_time = max(0, self.frame_time - elapsed_time)

        # Wait until the next frame
        self.canvas.after(int(sleep_time * 1000), self.game_loop)


    def changeState(self):
        
        inputs = self.inputManager.get_inputs()
        # changeState game state based on inputs
        # self.board.manageEnemiesMoves()
        self.stage_manager.changeStates()
        
        # if self.board.isStageFinished():
        #     self.board.nextStage()
        for entity in self.board.entities:
            entity.changeState(inputs)
            
    def update(self):
        
        self.board.manageCollisions()
        # print(self.board.col)
        # Update game state based on state
        for entity in self.board.entities:
            entity.update()

    def render(self):
        self.renderManager.render(self.board.entities)
        
        
    def loadShip(self):
        weaponsprite = self.load_manager.get_resource('fire')
        mainWeapon = Weapon(10, weaponsprite)
        myMainSprite = self.load_manager.get_resource('ship')
        
        mainShip = Ship(self.board, 100, Vector(100, 100), Vector(60, 60), mainWeapon, myMainSprite)
        mainShip.pos.x = self.board.width/2
        mainShip.pos.y = self.board.height * 4/5
        
        self.board.entities.append(mainShip)
        
    def reset(self):
        self.board.reset()
        self.stage_manager.reset()
        print(self.stage_manager.numStage)
        self.running = False
        
        def __del__(self):
            self.stop()
            del self.board
            del self.render_manager
