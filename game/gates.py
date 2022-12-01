# The gates that go inside of the levels.
import random
import arcade

class Gate(arcade.Sprite):
    def __init__(self, file, scaling, value):
        super().__init__(file, scaling)
        self.value = value