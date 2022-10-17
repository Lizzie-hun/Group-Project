import arcade
import globals


class Director(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        print("drawing actors")

    def update(self, delta_time):
        print(f"updating actors with delta time of {delta_time}")

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

