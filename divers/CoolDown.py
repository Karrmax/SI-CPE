import time        
        
class CoolDown():
    def __init__(self, CD):
        self.CD = CD
        self.lastTime = time.time()
        
        ## will time and enable the action only when lastTime = time 
        
    def isEnable(self):
        return (time.time() - self.lastTime) >= self.CD
    
    def set(self):
        self.lastTime = time.time()
        
    def reset(self):
        self.lastTime = time.time(0)