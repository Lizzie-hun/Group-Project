# The gates that go inside of the levels.
import random
import arcade

class Gate(arcade.Sprite):
    def __init__(self, scaling, value):
        number_sprite_list = []
        
        super().__init__(f'assets/numbers/0.png', scaling)
        self.value = value

    def draw(self, *args, filter=None, pixelated=None, blend_function=None):
        print("hello")
        super.draw(args, filter, pixelated, blend_function)
