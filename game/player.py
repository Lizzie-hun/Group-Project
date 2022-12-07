import arcade
import globals
import random

def load_texture_pair(filename):
    """Load a texture pair, with the second being a mirror image."""
    return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, flipped_horizontally=True)
    ]

class PlayerCharacter(arcade.Sprite):
    def __init__(self, color):
        # Set up parent class
        super().__init__()

        # 0 for facing right, 1 for facing left. These correspond
        # to indexes of player sprites, so either sprite[0] for left 
        # or sprite[1] for right facing
        self.facing_left = 1

        # 'color' string parameter somehow turns into a tuple eg: ('r', 'e', 'd')
        # this chunk of code slaps a bandaid on it
        self.dino_color = ''
        for letter in color:
            self.dino_color = self.dino_color + letter
        print(self.dino_color)
        self.dino_color = color

        # Used for flipping between image sequences
        self.cur_walk_texture = 0
        self.cur_idle_texture = 0
        self.cur_sprint_texture = 0
        self.scale = globals.CHARACTER_SCALING
        self.current_textures = 0
        # Adjust the collision box. Default includes too much empty space
        # side-to-side. Box is centered at sprite center, (0, 0)
        self.points = [[-22, -64], [22, -64], [22, 28], [-22, 28]]

        # This is the operand that will be used to perform the math
        self.operand = 2

        # --- Load Textures ---
        main_path = f'assets/dinos/{self.dino_color}/'

        # Load textures for idle standing
        self.idle_textures = []
        for i in range(4):
            texture = load_texture_pair(f"{main_path}idle/tile00{i}.png")
            self.idle_textures.append(texture)

        # Load textures for walking
        self.walk_textures = []
        for i in range(4,10):
            texture = load_texture_pair(f"{main_path}run/tile00{i}.png")
            self.walk_textures.append(texture)

        # Load textures for sprinting
        self.sprinting_textures = []
        for i in range(17,24):
            texture = load_texture_pair(f"{main_path}sprint/tile0{i}.png")
            self.sprinting_textures.append(texture)

        # Load textures for jumping
        self.jumping_textures = []
        up = load_texture_pair(f"{main_path}jump/tile012.png")
        down = load_texture_pair(f"{main_path}jump/tile007.png")
        self.jumping_textures.append(up)
        self.jumping_textures.append(down)


    def set_speed(self, speed):
        self.speed = speed

    def switch_animation(self, animation):
        self.current_textures = animation

    def update_animation(self, facing, delta_time: float = 1 / 60):
        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.facing_left:
            self.facing_left = False
        elif self.change_x > 0 and not self.facing_left:
            self.facing_left = True

        if self.current_textures == 0:
            # Idle animation
            self.cur_idle_texture += 1
            if self.cur_idle_texture > 3.9 * globals.IDLE_UPDATES_PER_FRAME:
                self.cur_idle_texture = 0
            frame = self.cur_idle_texture // globals.IDLE_UPDATES_PER_FRAME
            direction = not self.facing_left
            self.texture = self.idle_textures[frame][direction]
        
        elif self.current_textures == 1:
            # Walking animation
            self.cur_walk_texture += 1
            if self.cur_walk_texture > 5.9 * globals.UPDATES_PER_FRAME:
                self.cur_walk_texture = 0
            frame = self.cur_walk_texture // globals.UPDATES_PER_FRAME
            direction = not self.facing_left
            self.texture = self.walk_textures[frame][direction]

        elif self.current_textures == 2:
            direction = not self.facing_left
            self.texture = self.jumping_textures[0][direction]
        elif self.current_textures == 3:
            direction = not self.facing_left
            self.texture = self.jumping_textures[1][direction]

        elif self.current_textures == 4:
            # Sprinting animation
            self.cur_sprint_texture += 1
            if self.cur_sprint_texture > 6.9 * globals.UPDATES_PER_FRAME:
                self.cur_sprint_texture = 0
            frame = self.cur_sprint_texture // globals.UPDATES_PER_FRAME
            direction = not self.facing_left
            self.texture = self.sprinting_textures[frame][direction]
            

    def is_divisible(self, value):
        if self.operand % value == 0:
            self.operand += 1
            return True
        else:
            return False
    
    def switch_operand(self):
        self.operand = 3

    