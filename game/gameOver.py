import arcade
import globals

class GameOverView(arcade.View):
    def __init__(self, game, time_taken, score):
        super().__init__()
        self.Game_View = game
        self.time_taken = time_taken
        self.score = score

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, globals.SCREEN_WIDTH - 1, 0, globals.SCREEN_HEIGHT - 1)

    def on_draw(self):
        """ Draw this view """
        self.clear()
        """
        Draw "Game over" across the screen.
        """
        arcade.draw_text("Game Over", globals.SCREEN_WIDTH / 2, globals.SCREEN_HEIGHT / 2 + 50, arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click to restart", globals.SCREEN_WIDTH / 2 - 100 , globals.SCREEN_HEIGHT/2 - 50, arcade.color.WHITE, 24)

        time_taken_formatted = f"{round(self.time_taken, 1)} seconds"
        arcade.draw_text(f"Time taken: {time_taken_formatted}",
                         globals.SCREEN_WIDTH -120,
                         10,
                         arcade.color.GRAY,
                         font_size=15,
                         anchor_x="center")

        output_total = f"Total Score: {self.score}"
        arcade.draw_text(output_total, 10, 10, arcade.color.WHITE, 14)

    # def on_mouse_press(self, _x, _y, _button, _modifiers):
    #     self.mapId
        
