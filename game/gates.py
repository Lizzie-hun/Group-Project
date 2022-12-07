# The gates that go inside of the levels.
import random
import arcade

class Gate(arcade.Sprite):
    def __init__(self, scaling, value):        
        digit_filename = f'assets/numbers/{str(value)[0]}.png'
        
        super().__init__(digit_filename, scaling)
        self.value = value

