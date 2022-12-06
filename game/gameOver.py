import arcade
import globals

class GameOverView(arcade.View):
    """ View to show when game is over """

    def __init__(self):
        """ This is run once when we switch to this view """
        super().__init__()
        self.texture = arcade.load_texture("assets/youWin.png")

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, globals.SCREEN_WIDTH - 1, 0, globals.SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        self.texture.draw_sized(globals.SCREEN_WIDTH / 2, globals.SCREEN_HEIGHT / 2,
                                globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT)

    # def on_mouse_press(self, _x, _y, _button, _modifiers):
    #     """ If the user presses the mouse button, re-start the game. """
    #     game_view = GameView()
    #     game_view.setup()
    #     self.window.show_view(game_view)