import arcade
import globals
from level import Level
from player import PlayerCharacter
from map import Map


class Director(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        # This allows us to calculate player y movement
        self.player_previous_y = 0

        # What direction the player is supposed to face
        self.facing_right = True

        self.player = None
        self.player_sprite = None

        self.player_list = None
        self.gate_list = None

        self.physics_engine = None

        self.score = 0
        self.score_text = None

        self.scene = None
        self.map = None

        self.camera = None
        # HUD camera
        self.gui_camera = None

        arcade.set_background_color(arcade.color.ASH_GREY)

    def setup(self):
        #-------------------------
        # Map stuff - Sully
        # Set up the Cameras
        self.camera = arcade.Camera(self.width, self.height)
        self.gui_camera = arcade.Camera(self.width, self.height)

        # Map 
        # self.map = Map()
        self.map = arcade.load_tilemap("Map/map1..tmj", globals.TILE_SCALING, globals.LAYER_OPTIONS)
        self.scene = arcade.Scene.from_tilemap(self.map)

        self.scene.add_sprite_list_after("PlayerCharacter", globals.LAYER_NAME_FOREGROUND, False, self.player_list)

        print(self.map)
        #-------------------------
        # Score stuff
        self.score = 0
        self.score_text = None

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.gate_list = arcade.SpriteList()

        #-------test wall------
        # self.wall_list = arcade.SpriteList()
        #------remove this-----

        # Player
        self.player = PlayerCharacter()
        self.player_list.append(self.player)
        # Player scaling
        self.player.scale = globals.SPRITE_SCALING_PLAYER
        # Starting location for player
        self.player.center_x = globals.SCREEN_WIDTH // 4
        self.player.center_y = globals.SCREEN_HEIGHT // 4
        self.scene.add_sprite("PlayerCharacter", self.player)

        #--------Test Wall------------
        # wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", globals.SPRITE_SCALING)
        # wall.center_x = 350
        # wall.center_y = 150
        # self.wall_list.append(wall)
        #-------Remove this-----------

        # The level the gates and their sprites.
        self.level = Level(1)
        self.level.create_gates()
        for gate in self.level.get_gates():
            print(gate.get_gate())
            gate_sprite = arcade.Sprite("assets/dino_blue/sprint/blue_sprint_00.png", 1)

            gate_sprite.center_x = 30
            gate_sprite.center_y = 40

            self.gate_list.append(gate_sprite)

        # Physics Engine
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player,
            platforms=self.scene.get_sprite_list(globals.LAYER_NAME_PLATFORMS),
            gravity_constant=globals.GRAVITY,
            walls=self.scene[globals.LAYER_NAME_FLOOR],
        )
        arcade.set_background_color(arcade.color.ASH_GREY) 

    
    # Camera centered on sprite
    def center_camera_to_player(self):
        screen_center_x = self.player.center_x - (self.camera.viewport_width / 2)
        screen_center_y = -(self.camera.viewport_height / 2)
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered)


    def on_draw(self):
        """ Called whenever we need to draw the window. """

        # Clear the screen and start next frame render
        self.clear()
        arcade.start_render()

        # Filter is so the image isn't blurry
        # self.player_list.draw(filter=arcade.gl.NEAREST)
        self.scene.draw(filter=arcade.gl.NEAREST)

        self.camera.use()

        # Draw hitbox for player
        # self.player_list.draw_hit_boxes(line_thickness=5)

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """

        # See player class for animation states
        self.player.switch_animation(1)

        if key == arcade.key.UP:   
            if self.physics_engine.can_jump():
                self.player.change_y = 10
        elif key == arcade.key.DOWN:
            self.player.change_y = -globals.MOVEMENT_SPEED

        elif key == arcade.key.LEFT:
            self.player.change_x = -globals.MOVEMENT_SPEED

        elif key == arcade.key.RIGHT:
            self.player.change_x = globals.MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:
            KEY_UP = False
            self.player.change_y = 0

        if key == arcade.key.UP:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0

        # See player class for animation states
        self.player.switch_animation(0)


    def update(self, delta_time):
        """ Movement and game logic """

        # Update physics engine
        self.physics_engine.update()
        
        # Move the player
        self.player_list.update()

        # Camera Moving
        self.center_camera_to_player()

        # Player is in the rising jump state
        # Buffer of 3 units because the players center y has minor fluctuations 
        if self.player.center_y - self.player_previous_y > 3:
            self.player.switch_animation(2)
        # Player is in the falling jump state
        elif self.player.center_y - self.player_previous_y < -3:
            self.player.switch_animation(3)
        # Player is not moving and is idle
        elif self.player.velocity == [0.0, 0.0]:
            self.player.switch_animation(0)

        # Track movement velocity. There is a built in way to do this 
        # but this is simple homemade code
        self.player_previous_y = self.player.center_y

        # Update the players animation
        self.player_list.update_animation()

        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player, self.gate_list)

                

