class InputManager:
    def __init__(self):
        self.keys = {}

    def key_pressed(self, event):
        if event.keysym == "Caps_Lock" or event.keysym == "Caps_Lock" or event.keysym == "Alt_L" or event.keysym == "Alt_R" or event.keysym == "Shift_R" or event.keysym == "Shift_L":
            self.keys = {}    
        self.keys[event.keysym] = True

    def key_released(self, event):
        if event.keysym in self.keys:
            del self.keys[event.keysym]

    def get_inputs(self):
        # print(self.keys)
        return self.keys
