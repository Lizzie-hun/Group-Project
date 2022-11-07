import arcade
import globals
from level import Level


class Director(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        self.player_list = None
        self.gate_list = None

        # Score stuff
        self.score = 0
        self.score_text = None

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.gate_list = arcade.SpriteList()

        # Player sprite stuff
        self.player_sprite = arcade.Sprite("assets\\dino_blue\\idle\\tile000.png", 0.5)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_list.append(self.player_sprite)

        # The level the gates and their sprites.
        self.level = Level(1)
        self.level.create_gates()
        for gate in self.level.get_gates():
            print(gate.get_gate())
            gate_sprite = arcade.Sprite("assets\\dino_blue\\sprint\\blue_sprint_00.png", 1)

            gate_sprite.center_x = 30
            gate_sprite.center_y = 40

            self.gate_list.append(gate_sprite)

        arcade.set_background_color(arcade.color.ASH_GREY) 


    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        print("drawing actors")

    def update(self, delta_time):
        print(f"updating actors with delta time of {delta_time}")

        colliding = arcade.check_for_collision_with_list(self.player_sprite, self.gate_list)
        

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """

        # Call Keyboard services
        if key == arcade.key.LEFT:
            print("pressing left")
        elif key == arcade.key.RIGHT:
            print("pressing right") 

    def on_key_release(self, key, modifiers):

        #call keyboard services
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            print("key up")

