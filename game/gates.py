# The gates that go inside of the levels.
import random
import arcade

class Gate(arcade.Sprite):
    def __init__(self, scaling, value):        
        digit1_filename = f'assets/numbers/{str(value)[0]}.png'
        digit2_filename = f'assets/numbers/{str(value)[1]}.png'
        
        number_sprite_list = [digit1_filename, digit2_filename]

        super().__init__(number_sprite_list, scaling)
        self.value = value

    def draw(self, *args, filter=None, pixelated=None, blend_function=None):
        print("hello")
        super().draw(args, filter, pixelated, blend_function)
