import arcade
import globals
from player import PlayerCharacter
from gates import Gate
from gameOver import GameOverView
import json
import random
from gameOver import GameOverView

class Director(arcade.View):

    def __init__(self, dino_color):

        # Call the parent class's init function
        super().__init__()

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.window.set_mouse_visible(False)

        # This allows us to calculate player y movement
        self.player_previous_y = 0
        self.player_speed = globals.MOVEMENT_SPEED
        self.sprint_cooldown = 0
        self.movingLeft = False
        self.movingRight = False
        # What direction the player is supposed to face
        self.facing_right = True

        self.player = None
        self.player_sprite = None
        self.player_sprinting = False
        self.dino_color = dino_color

        self.player_list = None
        self.gate_list = None

        self.physics_engine = None

        self.score = 0
        self.score_text = None
        self.total_score = 0

        self.gameOver = None

        self.timer = 45
        self.timer_text = None

        self.timer = 0
        self.timer_text = None

        self.scene = None
        self.map = None
        self.mapId = 1

        self.camera = None
        # HUD camera
        self.gui_camera = None
        self.width = globals.SCREEN_WIDTH
        self.height = globals.SCREEN_HEIGHT

        # Load sounds 
        self.sound_falling = arcade.load_sound("assets/sounds/falling.wav")
        self.sound_jump = arcade.load_sound("assets/sounds/jump.wav")
        self.sound_powerUp = arcade.load_sound("assets/sounds/powerUp.wav")
        self.sound_hurt = arcade.load_sound("assets/sounds/hurt.wav")
        # Playing the sound here at the start at 0 volume prevents the lag when the player first jumps
        arcade.play_sound(self.sound_jump, 0)

        # arcade.set_background_color(arcade.color.ASH_GREY)

    def setup(self):
        #-------------------------
        # Map stuff - Sully
        # Set up the Cameras
        self.camera = arcade.Camera(self.width, self.height)
        self.gui_camera = arcade.Camera(self.width, self.height)

        # Map 
        # self.map = Map()       

        self.map = arcade.load_tilemap(f"Map/map{self.mapId}.tmj", globals.TILE_SCALING, globals.LAYER_OPTIONS)
        self.scene = arcade.Scene.from_tilemap(self.map)

        self.scene.add_sprite_list_after("PlayerCharacter", globals.LAYER_NAME_FOREGROUND, False, self.player_list)

        #-------------------------
        # Score stuff
        self.score = 0
        self.score_text = None


        self.timer += 30

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.gate_list = arcade.SpriteList()

    
        gateLocations = []
        mapData = ""
        with open(f'Map/map{self.mapId}.tmj', "r") as map1:
            mapData = json.load(map1)
            mapData = mapData['layers'][4]['data']
            # print(self.map.width*17)
            for i in range(self.map.width*17):
                if mapData[i] != 0:
                    # print(f'[{i}] {mapData[i]}')
                    y = i / 200
                    y = 14-y
                    x = i % 200
                    # print(x,y)
                    gateLocations.append([x*32,y*32, random.randint(1, 9)])
        
        for gate in gateLocations:
            gateSprite = Gate(globals.SPRITE_SCALING/3, gate[2])
            gateSprite.center_x = gate[0] + 20
            gateSprite.center_y = gate[1] + 90
            self.gate_list.append(gateSprite)


        # Player
        self.player = PlayerCharacter(self.dino_color) # Pass color in here (red, yellow, green, blue)
        self.player_list.append(self.player)
        # Player scaling
        self.player.scale = globals.SPRITE_SCALING_PLAYER
        # Starting location for player
        self.player.center_x = globals.SCREEN_WIDTH // 5
        self.player.center_y = globals.SCREEN_HEIGHT // 4
        self.scene.add_sprite("PlayerCharacter", self.player)
        # Player number
        self.playerNumber = arcade.load_texture(f'assets/numbers/{self.player.operand}.png')


        # Physics Engine referring to the layers on the tilemap
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player,
            platforms=self.scene.get_sprite_list(globals.LAYER_NAME_PLATFORMS),
            gravity_constant=globals.GRAVITY,
            walls=self.scene[globals.LAYER_NAME_FLOOR],
        )
        arcade.set_background_color(arcade.color.BLACK) 

# When called, rest the map to the first level, and show the Game Over screen with stats.
    def game_over(self):
        self.mapId = 1
        self.player.kill()
        self.clear()
        game_over = GameOverView(self, self.timer, self.total_score)
        arcade.get_window().show_view(game_over)

        self.movingRight = False
        self.movingLeft = False
        self.setup()
        self.timer = 45
        self.total_score = 0

    # Camera centered on sprite until the end of the map
    def center_camera_to_player(self):
        if self.player.center_x < ((self.map.width*32) - (self.camera.viewport_width / 2)):
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
        # arcade.start_render()
        # Filter is so the image isn't blurry
        # self.player_list.draw(filter=arcade.gl.NEAREST)
        self.scene.draw(filter=arcade.gl.NEAREST)
        self.gate_list.draw_hit_boxes(arcade.color_from_hex_string('FFF'), 5)
        self.gate_list.draw()

        # Activate the GUI camera before drawing GUI elements
        self.gui_camera.use()

        # Draw our score on the screen, scrolling it with the viewport
        score_text = f"Score: {self.score}"
        arcade.draw_text(
            score_text,
            10,
            10,
            arcade.csscolor.BLACK,
            15,
        )


        # Draw our timer on the screen, scrolling it with the viewport
        timer_text = f"Timer: {self.timer}"
        arcade.draw_text(
            timer_text,
            700,
            460,
            arcade.color.BLACK,
            15
        )

        self.camera.use()

        # Draw hitbox for player
        # self.player_list.draw_hit_boxes(line_thickness=5)

        # Draw the number above the player
        self.playerNumber.draw_scaled(self.player.center_x, self.player.center_y + 50, .1)


    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """

        # See player class for animation states
        self.player.switch_animation(1)

        if key == arcade.key.UP:   
            if self.physics_engine.can_jump():
                self.player.change_y = 10
                arcade.play_sound(self.sound_jump)
        elif key == arcade.key.DOWN:
            self.player.change_y = -self.player_speed

        elif key == arcade.key.LEFT:
            self.movingRight = False
            self.movingLeft = True
            if self.sprint_cooldown > 0:
                self.player.switch_animation(4) # Sprint animation
            else:
                self.player.switch_animation(1)
            # self.player.change_x = -self.player_speed

        elif key == arcade.key.RIGHT:
            self.movingLeft = False
            self.movingRight = True
            if self.sprint_cooldown > 0:
                self.player.switch_animation(4) # Sprint animation
            else:
                self.player.switch_animation(1)
            # self.player.change_x = self.player_speed

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.movingLeft = False
        elif key == arcade.key.RIGHT:
            self.movingRight = False

        # See player class for animation states
        self.player.switch_animation(0)


    def update(self, delta_time):
        """ Movement and game logic """

        # Update physics engine
        self.physics_engine.update()
        
        # Move the player
        self.player_list.update()

        # Delta time is around 0.016 to 0.017
        if self.movingLeft:
            self.player.change_x = -self.player_speed * 50 * delta_time
            # print("moving left")
        if self.movingRight:
            self.player.change_x = self.player_speed * 50 * delta_time
        if not self.movingRight and not self.movingLeft:
            self.player.change_x = 0
        

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

        if self.player.center_y < 0:
            arcade.play_sound(self.sound_falling)
            self.game_over()

        # print(self.player_speed)
        if self.sprint_cooldown > 0:
            self.sprint_cooldown -= 1
        else:
            self.player_speed = globals.MOVEMENT_SPEED
            self.player_sprinting = False

        # Track movement velocity. There is a built in way to do this 
        # but this is simple homemade code
        self.player_previous_y = self.player.center_y

        if self.player.change_x != 0: # If the player is not standing still
            if self.sprint_cooldown > 0 and self.player_sprinting:
                self.player.switch_animation(4)
            else:
                self.player.switch_animation(1)

        # Update the players animation
        self.player_list.update_animation()
        
        
        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player, self.gate_list)
        if len(hit_list) != 0:
            for i in hit_list:
                if isinstance(i, Gate):
                    if i.value % self.player.operand == 0:
                        self.player_speed = globals.SPRINT_SPEED
                        self.sprint_cooldown = globals.SPRINT_COOLDOWN
                        arcade.play_sound(self.sound_powerUp)
                        self.player.switch_operand()
                        self.player_sprinting = True
                        self.playerNumber = arcade.load_texture(f'assets/numbers/{self.player.operand}.png')
                        self.score += 1
                        self.total_score += 1
                        print("Correct answer")
                    else:
                        self.player_speed = globals.SLOW_SPEED
                        self.sprint_cooldown = globals.SPRINT_COOLDOWN
                        arcade.play_sound(self.sound_hurt)
                        print("Wrong answer")

                    i.kill()
        # if the player reaches the end of the level or the time runs out, call the gamne over function
        if self.player.center_x > ((self.map.width*32) - (self.camera.viewport_width / 4)): 
            if self.mapId < 2:
                self.mapId+=1
                self.setup()
            else: self.game_over()


        if self.timer > 0.0:
            self.timer -= delta_time
            self.timer = round(self.timer, 2)
            self.timer_text = f"Timer: {self.timer}"
        else:
            self.game_over()



                

