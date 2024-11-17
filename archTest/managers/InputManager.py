class InputManager:
    def __init__(self):
        self.keys = {}

    def key_pressed(self, event):
        self.keys[event.keysym] = True

    def key_released(self, event):
        if event.keysym in self.keys:
            del self.keys[event.keysym]

    def get_inputs(self):
        return self.keys
